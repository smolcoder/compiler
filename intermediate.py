from ast import CYCLES, BaseASTListener, TerminalASTNode, walkAST
from localvartable import LocalVariableTable


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
        return 'store {} at {}'.format(self.var, self.index, self.isLast)


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
        self.link = None

    def isMiddle(self):
        return self.status == 'mid'

    def isLocal(self):
        return self.status == 'loc'

    def __str__(self):
        if self.link:
            return str(self.link)
        return '{}.{}'.format(self.status, self.name)


class RecordFieldAccessVariable(Variable):
    pass


class NameGenerator:
    counter = 0

    def nextVariable(self, _type, status='mid', Cls=Variable):
        var = '__t{}'.format(self.counter)
        self.counter += 1
        return Cls(var, _type, status=status)


GLOBAL_NG = NameGenerator()


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
        self.ng = GLOBAL_NG

    def pushIfLocal(self, ast):
        var = ast.var
        # if isinstance(var, Variable) and var.status == 'loc':
        #     ast.var = self.ng.nextVariable(var.type)
        #     ast.addCode([TwoAC(ast.var, var, var.type)])
        #     return ast.var
        return var

    def exitReturn(self, ast):
        if not ast.getChildren():
            ast.addCode([Return('None')])
        else:
            var = ast.getFirstChild().var
            ast.addCode([Return(var.type, var)])

    def exitExpression(self, ast):
        fc = ast.getFirstChild()
        op = ast.getOperator().value if ast.getOperator() else None

        if fc.name == 'literal':
            resType = fc.getFirstChild().type
            if ast.parent.name in ['recordFieldInitializer', 'argumentList']:
                ast.var = self.ng.nextVariable(ast.type)
                ast.addCode([TwoAC(ast.var, Const(ast.getDeepest().value, resType), resType)])
            else:
                ast.var = Const(ast.getDeepest().value, resType)

        elif fc.name == 'leftHandSide':
            ast.var = fc.var
            if ast.parent.name in ['recordFieldInitializer', 'argumentList'] and fc.var.status == 'loc':
                ast.addCode([Push(ast.var)])
        elif op:
            ast.var = self.ng.nextVariable(ast.type)
            if ast.isUnaryOperation():
                ast.addCode([TwoACOp(ast.var, op, ast.getLastChild().var, ast.type)])
            else:
                lAst = fc
                rAst = ast.getLastChild()
                left = self.pushIfLocal(lAst)
                right = self.pushIfLocal(rAst)

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
        elif fc.name == 'functionInvocation':
            ast.var = fc.var
        elif fc.name in ['readIntCall', 'readStrCall', 'readBoolCall']:
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
            ast.var = RecordFieldAccessVariable(fc.value, fc.parent.type, status='loc')
            return ast.var
        ast.var = self.ng.nextVariable(ast.type, Cls=RecordFieldAccessVariable)
        sc = ast.getLastChild()
        leftVar = self.recordAccessCode(fc)
        ast.addCode([AccessRecordField(ast.var, leftVar, sc.value, ast.type)])
        return ast.var

    def recordAccessPenultFieldCode(self, ast, prev=None):
        fc = ast.getFirstChild()
        if fc.name == 'Identifier':
            ast.var = RecordFieldAccessVariable(fc.value, fc.parent.type, status='loc')
            return fc.parent.type, ast.var
        ast.var = self.ng.nextVariable(ast.type, Cls=RecordFieldAccessVariable)
        sc = ast.getLastChild()
        _, leftVar = self.recordAccessPenultFieldCode(fc, ast)
        if prev:
            ast.addCode([AccessRecordField(ast.var, leftVar, sc.value, ast.type)])
        else:
            ast.addCode([TwoAC(self.ng.nextVariable(ast.type), leftVar, ast.type)])
        return ast.getFirstChild().type, ast.var


def extractBaseBlocks(ast):
    l = ExtractBaseBlockListener()
    walkAST(l, ast)
    return l.bbs


class ExtractBaseBlockListener(BaseASTListener):
    def __init__(self):
        self.bbs = []

    def exitBlock(self, ast):
        bb = []
        for c in ast.getChildren():
            fc = c.getFirstChild()
            if fc.name in ['variableDeclaration', 'assignment']:
                bb.append(fc)
            else:
                if bb:
                    self.bbs.append(bb)
                bb = []
        if bb:
            self.bbs.append(bb)


def optimize(ast):
    bbs = extractBaseBlocks(ast)
    for bb in bbs:
        print bb
        cache = {}
        rCache = {}
        opt = OptimizerListener(bb[0].getLVT())
        for statement in bb:
            walkAST(opt, statement, cache, rCache)


class OptimizerListener(BaseASTListener):
    def __init__(self, lvt):
        """
        :type lvt: LocalVariableTable
        """
        self.lvt = lvt

    def getId(self, var):
        return var.name if isinstance(var, Variable) else str(var)

    def goLink(self, var):
        if isinstance(var, Variable) and var.link:
            return var.link
        return var

    def addToRCache(self, var, rCache, text):
        s = self.getId(var)
        if s not in rCache:
            rCache[s] = set()
        rCache[s].add(text)

    def exitExpression(self, ast, cache, rCache):
        fc = ast.getFirstChild()
        op = ast.getOperator().value if ast.getOperator() else None

        if not op:
            return
        if ast.isUnaryOperation():
            var = ast.getLastChild().var
            if isinstance(var, RecordFieldAccessVariable):
                return
            text = '{} {}'.format(op, self.getId(var))
            self.addToRCache(var, rCache, text)
        else:
            lAst = fc
            rAst = ast.getLastChild()
            left = self.goLink(lAst.var)
            right = self.goLink(rAst.var)

            if isinstance(left, RecordFieldAccessVariable):
                return
            if isinstance(right, RecordFieldAccessVariable):
                return
            text = '{} {} {}'.format(self.getId(left), op, self.getId(right))
            self.addToRCache(left, rCache, text)
            self.addToRCache(right, rCache, text)
        if text not in cache:
            cache[text] = ast.var
        else:
            var = cache[text]
            var.status = 'loc'
            self.lvt.put(var.name, var.type, ast)
            ast.var.link = var

    def removeFromCaches(self, var, cache, rCache):
        dirties = []
        for text in rCache.get(var, []):
            if text in cache:
                dirties.append(self.getId(cache[text]))
                del cache[text]
        for d in dirties:
            self.removeFromCaches(d, cache, rCache)

    def exitAssignment(self, ast, cache, rCache):
        dirty = self.getId(ast.getFirstChild().var)
        self.removeFromCaches(dirty, cache, rCache)


class RemoveAllIntermediateListener(BaseASTListener):
    def enterEvery(self, ast):
        ast.code = []
        ast.codeAfter = []
        ast.codeBefore = []


class AdjustIntermediateListener(BaseASTListener):
    def pushIfLocal(self, ast):
        var = ast.var
        if isinstance(var, Variable) and var.status == 'loc':
            ast.var = GLOBAL_NG.nextVariable(var.type)
            ast.addCode([TwoAC(ast.var, var, var.type)])
            return ast.var
        return var

    def enterExpression(self, ast):
        var = ast.var
        if isinstance(var, Variable) and var.link:
            l = RemoveAllIntermediateListener()
            walkAST(l, ast)
            ast.var = var

    def exitExpression(self, ast):
        # var = ast.var
        # if isinstance(var, Variable) and var.link:
        #     self.pushIfLocal(ast)
        op = ast.getOperator().value if ast.getOperator() else None

        lAst = ast.getFirstChild()
        rAst = ast.getLastChild()

        if ast.isUnaryOperation() and rAst.var.link:
            ast.code, ast.codeAfter, ast.codeBefore = [], [], []
            rAst.var = rAst.var.link
            ast.addCode([TwoACOp(ast.var, op, rAst.var, ast.type)])
            return
        if ast.isBinaryOperation():
            if not hasattr(lAst, 'var') or not hasattr(rAst, 'var'):
                return
            if not hasattr(lAst, 'var') or not hasattr(rAst, 'var'):
                return
            if not isinstance(lAst, Variable) or not isinstance(rAst, Variable):
                return
            ast.code = []
            if lAst.var.link:
                lAst.var = lAst.var.link
            if rAst.var.link:
                rAst.var = rAst.var.link

            left = self.pushIfLocal(lAst)
            right = self.pushIfLocal(rAst)

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


def adjustIntermediateCode(ast):
    l = AdjustIntermediateListener()
    walkAST(l, ast)