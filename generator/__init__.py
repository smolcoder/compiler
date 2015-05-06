from ast import BaseASTListener, walkAST, CYCLES, NonTerminalASTNode
from tad import *


class TADLinker:
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
    linker = TADLinker()
    linker.link(ast)
    return linker.code


class NameGenerator:
    counter = 0

    def nextName(self):
        var = 't{}'.format(self.counter)
        self.counter += 1
        return var


class LabelGenerator:
    counter = 0

    def nextLabel(self):
        var = '__Label_{}'.format(self.counter)
        self.counter += 1
        return var


ng = NameGenerator()
lg = LabelGenerator()


def locvar(var):
    return 'loc.{}'.format(var)


def const(var):
    return 'const.{}'.format(var)


class ExpressionTADListener(BaseASTListener):
    def __init__(self, globalEnv):
        self.globalEnv = globalEnv

    def exitExpression(self, ast):
        # todo refactoring is needed
        fc = ast.getFirstChild()
        op = ast.getOperator().value if ast.getOperator() else None

        if fc.name == 'literal':
            if fc.getFirstChild().name == 'StrLiteral':
                ast.var = ng.nextName()
                ast.code = [TwoAD(ast.var, const('"{}"'.format(fc.getFirstChild().value)))]
            else:
                ast.var = const(ast.getDeepest().value)
        elif fc.name == 'leftHandSide':
            ast.var = fc.var
        elif fc.name == 'functionInvocation':
            ast.var = fc.var
        elif op:
            ast.var = ng.nextName()
            if ast.isUnaryOperation():
                ast.code = [TwoADOp(ast.name, op, ast.getLastChild().var)]
            else:
                left = fc.var
                right = ast.getLastChild().var
                ast.code = [ThreeAD(ast.var, left, op, right)]
        elif fc.name == 'recordInitializer':
            ast.var = fc.var

    def exitFunctionInvocation(self, ast):
        ast.var = ng.nextName()
        args = []
        for c in ast.getLastChild().getChildren():
            args.append(c.var)
        ast.code = [CallFunction(ast.var, ast.getFirstChild().value, args)]

    def enterRecordInitializer(self, ast):
        ast.var = ng.nextName()

    def exitRecordInitializer(self, ast):
        recordName = ast.getFirstChild().value
        vars = [f.getLastChild().var for f in ast.getLastChild().getChildren()]
        ast.code = [CreateRecord(ast.var, recordName, vars)]

    def exitLeftHandSide(self, ast):
        fc = ast.getFirstChild()
        if fc.name == 'Identifier':
            ast.var = locvar(fc.value)
        elif fc.name == 'recordFieldAccess':
            ast.var = recordAccessCode(fc)

    def exitAssignment(self, ast):
        left = ast.getFirstChild().var
        op = ast.getChild(1).value
        right = ast.getLastChild().var
        if op in ['+=', '-=', '/=', '%=']:
            ast.code = [ThreeAD(left, left, op[0], right)]
        else:
            ast.code = [TwoAD(left, right)]

    def exitVariableDeclaration(self, ast):
        expr = ast.getLastChild()
        if expr.name == 'expression':
            ast.code = [TwoAD(locvar(ast.getChild(1).value), expr.var)]

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

    def exitFunctionSignature(self, ast):
        ast.code_before = ['.start {} ({}):{}'.format(
            ast.getName(),
            ','.join([t for n, t in ast.getArguments()]),
            ast.getReturnType()
        )]
        ast.code_after = ['.end {}'.format(ast.getName())]

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
    ast.var = ng.nextName()
    sc = ast.getLastChild()
    leftVar = recordAccessCode(fc)
    ast.code = [ThreeAD(ast.var, leftVar, '->', sc.value)]
    return ast.var


def makeTAD(ast):
    l = ExpressionTADListener(ast.getGlobalEnv())
    walkAST(l, ast)
    return linkCode(ast)