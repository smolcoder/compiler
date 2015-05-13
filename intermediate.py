from ast import CYCLES, BaseASTListener, TerminalASTNode


class IntermediateCode:
    def __repr__(self):
        return str(self)


class ThreeAC(IntermediateCode):
    def __init__(self, t1, t2, op, t3, resType, ast=None):
        self.t1 = t1
        self.t2 = t2
        self.op = op
        self.t3 = t3
        self.ast = ast
        self.type = resType

    def __str__(self):
        return '{} := {} {} {}'.format(self.t1, self.t2, self.op, self.t3)


class TwoAC(IntermediateCode):
    def __init__(self, t1, t2, resType, ast=None):
        self.t1 = t1
        self.t2 = t2
        self.ast = ast
        self.type = resType

    def __str__(self):
        return '{} := {}'.format(self.t1, self.t2)


class TwoACOp(IntermediateCode):
    def __init__(self, t1, op, t2, resType, ast=None):
        self.t1 = t1
        self.op = op
        self.t2 = t2
        self.ast = ast
        self.type = resType

    def __str__(self):
        return '{} := {} {}'.format(self.t1, self.op, self.t2)


class Label(IntermediateCode):
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return '.label {}'.format(self.label)


class Push(IntermediateCode):
    def __init__(self, variable):
        self.var = variable

    def __str__(self):
        return '.push {}'.format(self.var)


class PushBoolConst(IntermediateCode):
    def __init__(self, f):
        self.f = f

    def __str__(self):
        return '.push {}'.format(self.f)


class TestCondition(IntermediateCode):
    def __init__(self, var, label):
        """
        :type var: Variable
        """
        self.label = label
        self.var = var

    def __str__(self):
        return '.if {} is FALSE then goto {}'.format(self.var, self.label)


class Return(IntermediateCode):
    def __init__(self, _type, var=None):
        """
        :type var: Variable
        """
        self.var = var
        self.type = _type

    def __str__(self):
        if self.var:
            return 'return {} {}'.format(self.var, self.var.type)
        return 'return'


class GoTo(IntermediateCode):
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return '.goto {}'.format(self.label)


class CreateRecord(IntermediateCode):
    def __init__(self, var, name, types):
        self.t1 = var
        self.name = name
        self.types = types

    def __str__(self):
        return '{} := .create {}'.format(self.t1, self.name)


class NewRecord(IntermediateCode):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '.new {}'.format(self.name)


class CallFunction(IntermediateCode):
    def __init__(self, var, name, rType, argTypes):
        self.var = var
        self.name = name
        self.rType = rType
        self.argTypes = argTypes

    def __str__(self):
        return '{} := .call {}'.format(self.var, self.name)


class WriteLnCall(IntermediateCode):
    def __str__(self):
        return 'call writeln'


class ReadCall(IntermediateCode):
    def __init__(self, to, _type=None):
        self.to = to
        self.type = _type or to.type

    def __str__(self):
        return 'call read {}'.format(self.type)


class AccessRecordField(IntermediateCode):
    def __init__(self, t1, t2, t3, _type):
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.type = _type

    def __str__(self):
        return '{} := {} -> {}'.format(self.t1, self.t2, self.t3)


class IfEq(IntermediateCode):
    def __init__(self, var, label):
        self.label = label
        self.var = var

    def __str__(self):
        return '.ifeq {} == 0 goto {}'.format(self.var, self.label)


class IfNe(IntermediateCode):
    def __init__(self, var, label):
        self.label = label
        self.var = var

    def __str__(self):
        return '.ifne {} != 0 goto {}'.format(self.var, self.label)


class NewArray(IntermediateCode):
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return 'new array of size {}'.format(self.size)


class AAstore(IntermediateCode):
    def __init__(self, var, index, isLast=False):
        """
        :type var: Variable
        """
        self.index = index
        self.var = var
        self.isLast = isLast

    def __str__(self):
        return 'store {} at {}'.format(self.var, self.index)


class CortegeAccess(IntermediateCode):
    def __init__(self, varFrom, varTo, index, _type):
        """
        :type varFrom: Variable
        :type varTo: Variable
        """
        self.varFrom = varFrom
        self.varTo = varTo
        self.index = index
        self.type = _type

    def __str__(self):
        return 'load {}[{}] to {}'.format(self.varFrom, self.index, self.varTo)


class PutField:
    def __init__(self, name, fieldType, recordType):
        self.name = name
        self.fieldType = fieldType
        self.recordType = recordType

    def __str__(self):
        return 'putfield {}.{} [{}]'.format(self.recordType, self.name, self.fieldType)


class TACEntity:
    pass


class Const(TACEntity):
    def __init__(self, value, _type):
        self.value = value
        self.type = _type

    def __str__(self):
        if self.type == 'Str':
            return '"{}"'.format(self.value)
        return '{}'.format(self.value)


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

    def nextVariable(self, _type, status='mid'):
        var = '__t{}'.format(self.counter)
        self.counter += 1
        return Variable(var, _type, status=status)


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

    def exitReturn(self, ast):
        if not ast.getChildren():
            ast.addCode([Return('None')])
        else:
            var = ast.getFirstChild().var
            ast.addCode([Return(var.type, var)])

    def exitExpression(self, ast):
        # todo refactoring is needed
        fc = ast.getFirstChild()
        op = ast.getOperator().value if ast.getOperator() else None

        if fc.name == 'literal':
            resType = fc.getFirstChild().type
            if ast.parent.name in ['recordFieldInitializer', 'argumentList', 'expressionList']:
                ast.var = self.ng.nextVariable(ast.type)
                ast.addCode([TwoAC(ast.var, Const(ast.getDeepest().value, resType), resType)])
            else:
                ast.var = Const(ast.getDeepest().value, resType)

        elif fc.name == 'leftHandSide':
            if ast.parent.name in ['recordFieldInitializer', 'argumentList', 'expressionList']:
                if fc.var.status == 'loc':
                    ast.var = Variable(fc.var.name, fc.var.type, 'loc')
                    ast.addCode([Push(ast.var)])
                else:
                    ast.var = fc.var
            else:
                ast.var = fc.var
        elif fc.name == 'functionInvocation':
            ast.var = fc.var
        elif fc.name in ['readIntCall', 'readStrCall', 'readBoolCall']:
            ast.var = fc.var
        elif op:
            ast.var = self.ng.nextVariable(ast.type)
            if ast.isUnaryOperation():
                ast.addCode([TwoACOp(ast.var, op, ast.getLastChild().var, ast.type)])
            else:
                lAst = fc
                rAst = ast.getLastChild()
                left = lAst.var
                right = rAst.var

                # todo monkey code :(
                if isinstance(left, Variable) and left.status == 'loc':
                    lAst.var = self.ng.nextVariable(left.type)
                    lAst.addCode([TwoAC(lAst.var, left, left.type)])
                    left = lAst.var
                if isinstance(right, Variable) and right.status == 'loc':
                    rAst.var = self.ng.nextVariable(right.type)
                    rAst.addCode([TwoAC(rAst.var, right, right.type)])
                    right = rAst.var

                if op in ['&&', '||']:
                    condLabel = LABEL_GENERATOR.nextLabel()
                    endLabel = LABEL_GENERATOR.nextLabel()
                    if op == '&&':
                        lAst.addCodeAfter([IfEq(left, condLabel)])
                        rAst.addCodeAfter([IfEq(right, condLabel)])
                    else:
                        lAst.addCodeAfter([IfNe(left, condLabel)])
                        rAst.addCodeAfter([IfNe(right, condLabel)])
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
        elif fc.name == 'cortegeInitializer':
            ast.var = fc.var

    def enterWritelnCall(self, ast):
        ast.addCodeBefore([NewArray(len(ast.getFirstChild().getChildren()))])

    def exitWritelnCall(self, ast):
        children = ast.getFirstChild().getChildren()
        for i, e in enumerate(children):
            e.addCodeBefore([Push(Const(str(i), 'Int'))])
            e.addCodeAfter([AAstore(e.var, i, i+1 == len(children))])
        ast.addCodeAfter([WriteLnCall()])

    def exitFunctionInvocation(self, ast):
        ast.var = self.ng.nextVariable(ast.type)
        types = [e.type for e in ast.getLastChild().getChildren()]
        ast.addCode([CallFunction(ast.var, ast.getFirstChild().value, ast.type, types)])

    # todo duplicated code, see enter/exit WritelnCall
    def enterCortegeInitializer(self, ast):
        ast.addCodeBefore([NewArray(len(ast.getFirstChild().getChildren()))])

    def exitCortegeInitializer(self, ast):
        ast.var = self.ng.nextVariable(ast.type)
        children = ast.getFirstChild().getChildren()
        for i, e in enumerate(children):
            e.addCodeBefore([Push(Const(str(i), 'Int'))])
            e.addCodeAfter([AAstore(e.var, i, i+1 == len(children))])

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
            if ast.parent.name == 'assignment' and ast.parent.getFirstChild() is ast:
                prevType, ast.var = self.recordAccessPenultFieldCode(fc)
                ast.parent.addCodeAfter([PutField(fc.getLastChild().value, ast.var.type, prevType)])
            else:
                ast.var = self.recordAccessCode(fc)
        elif fc.name == 'cortegeAccess':
            ast.var = self.ng.nextVariable(ast.type)
            # if ast.parent.name == 'assignment' and ast.parent.getFirstChild() is ast:
            var = Variable(fc.getFirstChild().value, fc.type, status='loc', ast=ast)
            ast.addCodeBefore([CortegeAccess(var, ast.var, fc.getLastChild().value, fc.type)])
            # else:
            #     ast.addCode([CortegeAccess(ast.var, fc.getLastChild().value, fc.type, ast.var)])

    def exitAssignment(self, ast):
        left = ast.getFirstChild().var
        op = ast.getChild(1).value
        right = ast.getLastChild().var
        if op in ['+=', '-=', '*=', '/=', '%=']:
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
            block.addCodeBefore([TestCondition(ast.getCondition().var, ast.endLabel)])
        else:
            l = LABEL_GENERATOR.nextLabel()
            block.addCodeBefore([TestCondition(ast.getCondition().var, l)])
            block.addCodeAfter([GoTo(ast.endLabel), Label(l)])
        ast.addCodeAfter([Label(ast.endLabel)])

    def exitElse(self, ast):
        ast.addCodeAfter([Label(ast.parent.endLabel)])

    def exitElif(self, ast):
        block = ast.getBlock()
        l = LABEL_GENERATOR.nextLabel()
        block.addCodeBefore([TestCondition(ast.getCondition().var, l)])
        block.addCodeAfter([GoTo(ast.parent.endLabel), Label(l)])

    def enterWhileStatement(self, ast):
        ast.startLabel = LABEL_GENERATOR.nextLabel()
        ast.endLabel = LABEL_GENERATOR.nextLabel()

    def exitWhileStatement(self, ast):
        expr = ast.getFirstChild()
        block = ast.getLastChild()
        expr.addCodeBefore([Label(ast.startLabel)])
        expr.addCodeAfter([TestCondition(expr.var, ast.endLabel)])
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
        ast.addCodeAfter([TestCondition(ast.getFirstChild().var, ast.parent.endLabel)])

    def exitForUpdate(self, ast):
        ast.addCodeAfter([GoTo(ast.parent.startLabel)])

    def exitFunctionDeclaration(self, ast):
        name = ast.getFirstChild().getName()
        ast.addCodeBefore([50 * '.' + 'start {}'.format(name)])
        ast.addCodeAfter([50 * '.' + 'end {}'.format(name)])

    def exitProgramme(self, ast):
        block = ast.getJustBlock()
        if block:
            block.addCodeBefore(['.start main'])
            block.addCodeAfter(['.end main'])

    def exitReadIntCall(self, ast):
        ast.var = self.ng.nextVariable(ast.type)
        ast.addCode([ReadCall(ast.var)])

    def exitReadBoolCall(self, ast):
        ast.var = self.ng.nextVariable(ast.type)
        ast.addCode([ReadCall(ast.var)])

    def exitReadStrCall(self, ast):
        ast.var = self.ng.nextVariable(ast.type)
        ast.addCode([ReadCall(ast.var)])

    def recordAccessCode(self, ast):
        fc = ast.getFirstChild()
        if fc.name == 'Identifier':
            ast.var = Variable(fc.value, fc.parent.type, status='loc')
            return ast.var
        ast.var = self.ng.nextVariable(ast.type)
        sc = ast.getLastChild()
        leftVar = self.recordAccessCode(fc)
        if sc.name == 'cortegeAccess':
            cVar = self.ng.nextVariable(sc.type)
            ast.addCode([AccessRecordField(cVar, leftVar, sc.getFirstChild().value, ast.type)])
            ast.addCode([CortegeAccess(ast.var, sc.getLastChild().value, sc.type)])
        else:
            ast.addCode([AccessRecordField(ast.var, leftVar, sc.value, ast.type)])
        return ast.var

    def recordAccessPenultFieldCode(self, ast, prev=None):
        fc = ast.getFirstChild()
        if fc.name == 'Identifier':
            ast.var = Variable(fc.value, fc.parent.type, status='loc')
            return fc.parent.type, ast.var
        ast.var = self.ng.nextVariable(ast.type)
        sc = ast.getLastChild()
        _, leftVar = self.recordAccessPenultFieldCode(fc, ast)
        if prev:
            ast.addCode([AccessRecordField(ast.var, leftVar, sc.value, ast.type)])
        else:
            ast.addCode([TwoAC(self.ng.nextVariable(ast.type), leftVar, ast.type)])
        return ast.getFirstChild().type, ast.var