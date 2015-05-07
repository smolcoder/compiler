from ast import CYCLES, BaseASTListener, TerminalASTNode


class MiddleCode:
    def __repr__(self):
        return str(self)


class ThreeAC(MiddleCode):
    def __init__(self, t1, t2, op, t3, resType, ast=None):
        self.t1 = t1
        self.t2 = t2
        self.op = op
        self.t3 = t3
        self.ast = ast
        self.type = resType

    def __str__(self):
        return '{} := {} {} {}'.format(self.t1, self.t2, self.op, self.t3)


class TwoAC(MiddleCode):
    def __init__(self, t1, t2, resType, ast=None):
        self.t1 = t1
        self.t2 = t2
        self.ast = ast
        self.type = resType

    def __str__(self):
        return '{} := {}'.format(self.t1, self.t2)


class TwoACOp(MiddleCode):
    def __init__(self, t1, op, t2, resType, ast=None):
        self.t1 = t1
        self.op = op
        self.t2 = t2
        self.ast = ast
        self.type = resType

    def __str__(self):
        return '{} := {} {}'.format(self.t1, self.op, self.t2)


class Label(MiddleCode):
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return '.label {}'.format(self.label)


class Push(MiddleCode):
    def __init__(self, variable):
        self.var = variable

    def __str__(self):
        return '.push {}'.format(self.var)


class PushBoolConst(MiddleCode):
    def __init__(self, f):
        self.f = f

    def __str__(self):
        return '.push {}'.format(self.f)


class TestCondition(MiddleCode):
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return '.test {}'.format(self.label)


class GoTo(MiddleCode):
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return '.goto {}'.format(self.label)


class CreateRecord(MiddleCode):
    def __init__(self, var, name, types):
        self.t1 = var
        self.name = name
        self.types = types

    def __str__(self):
        return '{} := .create {}'.format(self.t1, self.name)


class NewRecord(MiddleCode):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '.new {}'.format(self.name)


class CallFunction(MiddleCode):
    def __init__(self, var, name):
        self.var = var
        self.name = name

    def __str__(self):
        return '{} := .call {}'.format(self.var, self.name)


class AccessRecordField(MiddleCode):
    def __init__(self, t1, t2, t3, _type):
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.type = _type

    def __str__(self):
        return '{} := {} -> {}'.format(self.t1, self.t2, self.t3)


class IfNeEq(MiddleCode):
    def __init__(self, var, label, op):
        self.label = label
        self.var = var
        self.op = op

    def __str__(self):
        return '.if {} {} 0 goto {}'.format(self.var, self.op, self.label)


class TACEntity:
    pass


class Const(TACEntity):
    def __init__(self, value, _type):
        self.value = value
        self.type = _type

    def getByteCode(self):
        if self.type == 'Bool':
            if self.value == 'true':
                return ['iconst_1']
            return ['iconst_0']
        if self.value in [0, 1, 2, 3, 4, 5]:
            return ['iconst_{}'.format(self.value)]
        return ['ldc {}'.format(self.value)]

    def __str__(self):
        if self.type == 'Str':
            return 'const."{}"'.format(self.value)
        return 'const.{}'.format(self.value)


class Variable(TACEntity):
    def __init__(self, name, _type, status='mid', ast=None):
        self.name = name
        self.status = status
        self.ast = ast
        self.type = _type

    def isMiddle(self):
        return self.status == 'mid'

    def isLocal(self):
        return self.status == 'loc'

    def __str__(self):
        return '{}.{}'.format(self.status, self.name)


class NameGenerator:
    counter = 0

    def nextVariable(self, _type):
        var = '__t{}'.format(self.counter)
        self.counter += 1
        return Variable(var, _type)


class LabelGenerator:
    counter = 0

    def nextLabel(self):
        var = 'Label{}'.format(self.counter)
        self.counter += 1
        return var


LABEL_GENERATOR = LabelGenerator()


class BuildMiddleCodeListener(BaseASTListener):
    def __init__(self, globalEnv):
        self.globalEnv = globalEnv
        self.ng = NameGenerator()

    def exitExpression(self, ast):
        # todo refactoring is needed
        fc = ast.getFirstChild()
        op = ast.getOperator().value if ast.getOperator() else None

        if fc.name == 'literal':
            ast.var = self.ng.nextVariable(ast.type)
            resType = fc.getFirstChild().type
            ast.addCode([TwoAC(ast.var, Const(ast.getDeepest().value, resType), resType)])

        elif fc.name == 'leftHandSide':
            if ast.parent.name in ['recordFieldInitializer', 'argumentList']:
                ast.var = Variable(fc.var.name, fc.var.type, 'loc')
            else:
                ast.var = fc.var
            if ast.var.status == 'loc':
                ast.addCode([Push(ast.var)])
        elif fc.name == 'functionInvocation':
            ast.var = fc.var
        elif op:
            ast.var = self.ng.nextVariable(ast.type)
            if ast.isUnaryOperation():
                ast.addCode([TwoACOp(ast.var, op, ast.getLastChild().var, ast.type)])
            else:
                left = fc.var
                right = ast.getLastChild().var
                if op in ['&&', '||']:
                    lAst = fc
                    rAst = ast.getLastChild()
                    condLabel = LABEL_GENERATOR.nextLabel()
                    endLabel = LABEL_GENERATOR.nextLabel()
                    jmpOp = '==' if op == '&&' else '!='
                    lAst.addCodeAfter([IfNeEq(left, condLabel, jmpOp)])
                    rAst.addCodeAfter([IfNeEq(right, condLabel, jmpOp)])
                    const1 = op == '&&'
                    const2 = op == '||'
                    ast.addCodeAfter([PushBoolConst(const1),
                                      GoTo(endLabel),
                                      Label(condLabel),
                                      PushBoolConst(const2),
                                      Label(endLabel)])
                else:
                    ast.addCode([ThreeAC(ast.var, left, op, right, ast.type)])
        elif fc.name == 'recordInitializer':
            ast.var = fc.var

    def exitFunctionInvocation(self, ast):
        ast.var = self.ng.nextVariable(ast.type)
        ast.addCode([CallFunction(ast.var, ast.getFirstChild().value)])

    def enterRecordInitializer(self, ast):
        ast.var = self.ng.nextVariable(ast.type)
        ast.addCodeBefore([NewRecord(ast.getFirstChild().value)])

    def exitRecordInitializer(self, ast):
        types = []
        if not isinstance(ast.getLastChild(), TerminalASTNode):
            types = [f.getLastChild().type for f in ast.getLastChild().getChildren()]
        ast.addCode([CreateRecord(ast.var, ast.getFirstChild().value, types)])

    def exitLeftHandSide(self, ast):
        fc = ast.getFirstChild()
        if fc.name == 'Identifier':
            ast.var = Variable(fc.value, ast.type, status='loc')
        elif fc.name == 'recordFieldAccess':
            ast.var = self.recordAccessCode(fc)

    def exitAssignment(self, ast):
        left = ast.getFirstChild().var
        op = ast.getChild(1).value
        right = ast.getLastChild().var
        if op in ['+=', '-=', '/=', '%=']:
            ast.addCode([ThreeAC(left, left, op[0], right, ast.getFirstChild().type)])
        else:
            ast.addCode([TwoAC(left, right, ast.getFirstChild().type)])

    def exitVariableDeclaration(self, ast):
        expr = ast.getLastChild()
        if expr.name == 'expression':
            ast.addCode([TwoAC(Variable(ast.getChild(1).value, expr.type, status='loc'), expr.var, expr.type)])

    def enterIf(self, ast):
        ast.endLabel = LABEL_GENERATOR.nextLabel()

    def exitIf(self, ast):
        block = ast.getBlockIfTrue()

        if not ast.getElifs() and not ast.getElse():
            block.addCodeBefore([TestCondition(ast.endLabel)])
            block.addCodeAfter([Label(ast.endLabel)])
        else:
            l = LABEL_GENERATOR.nextLabel()
            block.addCodeBefore([TestCondition(l)])
            block.addCodeAfter([GoTo(ast.endLabel), Label(l)])

    def exitElse(self, ast):
        ast.addCodeAfter([Label(ast.parent.endLabel)])

    def exitElif(self, ast):
        block = ast.getBlock()
        l = LABEL_GENERATOR.nextLabel()
        block.addCodeBefore([TestCondition(l)])
        block.addCodeAfter([GoTo(ast.parent.endLabel), TestCondition(l)])

    def enterWhileStatement(self, ast):
        ast.startLabel = LABEL_GENERATOR.nextLabel()
        ast.endLabel = LABEL_GENERATOR.nextLabel()

    def exitWhileStatement(self, ast):
        expr = ast.getFirstChild()
        block = ast.getLastChild()
        expr.addCodeBefore([Label(ast.startLabel)])
        expr.addCodeAfter([TestCondition(ast.endLabel)])
        block.addCodeAfter([GoTo(ast.startLabel), Label(ast.endLabel)])

    def visitBreak(self, ast):
        ast.addCode([GoTo(ast.getFirstParentByName(CYCLES).endLabel)])

    def visitContinue(self, ast):
        ast.addCode([GoTo(ast.getFirstParentByName(CYCLES).startLabel)])

    def enterForStatement(self, ast):
        ast.startLabel = LABEL_GENERATOR.nextLabel()
        ast.endLabel = LABEL_GENERATOR.nextLabel()

    def exitForStatement(self, ast):
        ast.addCodeAfter([Label(ast.endLabel)])

    def exitForCondition(self, ast):
        ast.addCodeBefore([Label(ast.parent.startLabel)])
        ast.addCodeAfter([TestCondition(ast.parent.endLabel)])

    def exitForUpdate(self, ast):
        ast.addCodeAfter([GoTo(ast.parent.startLabel)])

    def exitFunctionDeclaration(self, ast):
        name = ast.getFirstChild().getName()
        ast.addCodeBefore(['.start {}'.format(name)])
        ast.addCodeAfter(['.end {}'.format(name)])

    def exitProgramme(self, ast):
        block = ast.getJustBlock()
        if block:
            block.addCodeBefore(['.start main'])
            block.addCodeAfter(['.end main'])

    def recordAccessCode(self, ast):
        fc = ast.getFirstChild()
        if fc.name == 'Identifier':
            ast.var = Variable(fc.value, fc.parent.type, status='loc')
            return ast.var
        ast.var = self.ng.nextVariable(ast.type)
        sc = ast.getLastChild()
        leftVar = self.recordAccessCode(fc)
        ast.addCode([AccessRecordField(ast.var, leftVar, sc.value, ast.type)])
        return ast.var