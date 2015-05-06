from ast import BaseASTListener, walkAST, CYCLES, NonTerminalASTNode
from middlecode import *


class MiddleCodeLinker:
    def __init__(self):
        self.code = []

    def getCodeBefore(self, ast):
        if hasattr(ast, 'code_before'):
            self.code += ast.code_before

    def getCodeAfter(self, ast):
        if hasattr(ast, 'code_after'):
            self.code += ast.code_after

    def getCode(self, ast):
        if hasattr(ast, 'code'):
            self.code += ast.code

    def linkChildren(self, ast):
        if isinstance(ast, NonTerminalASTNode):
            for c in ast.getChildren():
                self.link(c)

    def linkForStatement(self, ast):
        forInit = ast.getFirstChildByName('forInit')
        forCondition = ast.getFirstChildByName('forCondition')
        forUpdate = ast.getFirstChildByName('forUpdate')
        forBlock = ast.getLastChild()
        self.link(forInit)
        self.link(forCondition)
        self.link(forBlock)
        self.link(forUpdate)

    def link(self, ast):
        self.getCodeBefore(ast)
        if ast.name == 'forStatement':
            self.linkForStatement(ast)
        else:
            self.linkChildren(ast)
            self.getCode(ast)
        self.getCodeAfter(ast)


def linkCode(ast):
    linker = MiddleCodeLinker()
    linker.link(ast)
    return linker.code


class NameGenerator:
    counter = 0

    def nextName(self, _type):
        var = '__t{}'.format(self.counter)
        self.counter += 1
        return Variable(var, _type)


class LabelGenerator:
    counter = 0

    def nextLabel(self):
        var = 'Label_{}'.format(self.counter)
        self.counter += 1
        return var


ng = NameGenerator()
lg = LabelGenerator()


class ExpressionTADListener(BaseASTListener):
    def __init__(self, globalEnv):
        self.globalEnv = globalEnv

    def exitExpression(self, ast):
        # todo refactoring is needed
        fc = ast.getFirstChild()
        op = ast.getOperator().value if ast.getOperator() else None

        if fc.name == 'literal':
            ast.var = ng.nextName(ast.type)
            resType = fc.getFirstChild().type
            ast.code = [TwoAC(ast.var, Const(ast.getDeepest().value, resType), resType)]

        elif fc.name == 'leftHandSide':
            ast.var = fc.var
        elif fc.name == 'functionInvocation':
            ast.var = fc.var
        elif op:
            ast.var = ng.nextName(ast.type)
            if ast.isUnaryOperation():
                ast.code = [TwoACOp(ast.var, op, ast.getLastChild().var, ast.type)]
            else:
                left = fc.var
                right = ast.getLastChild().var
                ast.code = [ThreeAC(ast.var, left, op, right, ast.type)]
        elif fc.name == 'recordInitializer':
            ast.var = fc.var

    def exitFunctionInvocation(self, ast):
        ast.var = ng.nextName(ast.type)
        ast.code = [CallFunction(ast.var, ast.getFirstChild().value)]

    def enterRecordInitializer(self, ast):
        ast.var = ng.nextName(ast.type)
        ast.code_before = [NewRecord(ast.getFirstChild().value)]

    def exitRecordInitializer(self, ast):
        types = [f.getLastChild().type for f in ast.getLastChild().getChildren()]
        ast.code = [CreateRecord(ast.var, ast.getFirstChild().value, types)]

    def exitLeftHandSide(self, ast):
        fc = ast.getFirstChild()
        if fc.name == 'Identifier':
            ast.var = Variable(fc.value, ast.type, status='loc')
        elif fc.name == 'recordFieldAccess':
            ast.var = Variable(recordAccessCode(fc), ast.type, status='loc')

    def exitAssignment(self, ast):
        left = ast.getFirstChild().var
        op = ast.getChild(1).value
        right = ast.getLastChild().var
        if op in ['+=', '-=', '/=', '%=']:
            ast.code = [ThreeAC(left, left, op[0], right, ast.getFirstChild().type)]
        else:
            ast.code = [TwoAC(left, right, ast.getFirstChild().type)]

    def exitVariableDeclaration(self, ast):
        expr = ast.getLastChild()
        if expr.name == 'expression':
            ast.code = [TwoAC(Variable(ast.getChild(1).value, expr.type, status='loc'), expr.var, expr.type)]

    def enterIf(self, ast):
        ast.endLabel = lg.nextLabel()

    def exitIf(self, ast):
        block = ast.getBlockIfTrue()

        if not ast.getElifs() and not ast.getElse():
            block.code_before = [TestCondition(ast.endLabel)]
            block.code_after = [Label(ast.endLabel)]
        else:
            l = lg.nextLabel()
            block.code_before = [TestCondition(l)]
            block.code_after = [GoTo(ast.endLabel), Label(l)]

    def exitElse(self, ast):
        ast.code_after = [Label(ast.parent.endLabel)]

    def exitElif(self, ast):
        block = ast.getBlock()
        l = lg.nextLabel()
        block.code_before = [TestCondition(l)]
        block.code_after = [GoTo(ast.parent.endLabel), TestCondition(l)]

    def enterWhileStatement(self, ast):
        ast.startLabel = lg.nextLabel()
        ast.endLabel = lg.nextLabel()

    def exitWhileStatement(self, ast):
        expr = ast.getFirstChild()
        block = ast.getLastChild()
        expr.code_before = [Label(ast.startLabel)]
        expr.code_after = [TestCondition(ast.endLabel)]
        block.code_after = [GoTo(ast.startLabel), Label(ast.endLabel)]

    def visitBreak(self, ast):
        ast.code = [GoTo(ast.getFirstParentByName(CYCLES).endLabel)]

    def visitContinue(self, ast):
        ast.code = [GoTo(ast.getFirstParentByName(CYCLES).startLabel)]

    def enterForStatement(self, ast):
        ast.startLabel = lg.nextLabel()
        ast.endLabel = lg.nextLabel()

    def exitForStatement(self, ast):
        ast.code_after = [Label(ast.endLabel)]

    def exitForCondition(self, ast):
        ast.code_before = [Label(ast.parent.startLabel)]
        ast.code_after = [TestCondition(ast.parent.endLabel)]

    def exitForUpdate(self, ast):
        ast.code_after = [GoTo(ast.parent.startLabel)]

    def exitFunctionDeclaration(self, ast):
        name = ast.getFirstChild().getName()
        ast.code_before = ['.start {}'.format(name)]
        ast.code_after = ['.end {}'.format(name)]

    def exitProgramme(self, ast):
        block = ast.getJustBlock()
        if block:
            block.code_before = ['.start main']
            block.code_after = ['.end main']


def recordAccessCode(ast):
    fc = ast.getFirstChild()
    if fc.name == 'Identifier':
        ast.var = fc.value
        return ast.var
    ast.var = ng.nextName(ast.type)
    sc = ast.getLastChild()
    leftVar = recordAccessCode(fc)
    ast.code = [ThreeAC(ast.var, leftVar, '->', sc.value, ast.type)]
    return ast.var


def makeTAD(ast):
    l = ExpressionTADListener(ast.getGlobalEnv())
    walkAST(l, ast)
    return linkCode(ast)