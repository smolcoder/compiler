from ast import BaseASTListener, walkAST, CYCLES, NonTerminalASTNode


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


def threeAC(var, left, op, right):
    return '{} := {} {} {}'.format(var, left, op, right)


def twoAC(var, op, arg):
    return '{} := {} {}'.format(var, op, arg)


def oneAC(var, arg):
    return '{} := {}'.format(var, arg)


def testLabel(label=None):
    return 'test {}'.format(label or lg.nextLabel())


def goto(label):
    return 'goto {}'.format(label)


def label(l):
    return '{}:'.format(l)


class ExpressionTADListener(BaseASTListener):
    def exitExpression(self, ast):
        fc = ast.getFirstChild()
        op = ast.getOperator().value if ast.getOperator() else None

        if fc.name == 'literal':
            if fc.getFirstChild().name == 'StrLiteral':
                ast.var = ng.nextName()
                ast.code = [oneAC(ast.var, '"{}"'.format(fc.getFirstChild().value))]
            else:
                ast.var = ast.getDeepest().value
        elif fc.name == 'leftHandSide':
            ast.var = fc.var
        elif fc.name == 'functionInvocation':
            ast.var = fc.var
        elif op:
            ast.var = ng.nextName()
            if ast.isUnaryOperation():
                ast.code = [twoAC(ast.name, op, ast.getLastChild().var)]
            else:
                left = fc.var
                right = ast.getLastChild().var
                ast.code = [threeAC(ast.var, left, op, right)]

    def exitFunctionInvocation(self, ast):
        ast.var = ng.nextName()
        args = []
        for c in ast.getLastChild().getChildren():
            args.append(c.var)
        ast.code = [twoAC(ast.var, 'call', '{} {} '.format(ast.getFirstChild().value, ' '.join(args)))]

    def exitLeftHandSide(self, ast):
        fc = ast.getFirstChild()
        if fc.name == 'Identifier':
            ast.var = fc.value
        elif fc.name == 'recordFieldAccess':
            ast.var = recordAccessCode(fc)

    def exitAssignment(self, ast):
        left = ast.getFirstChild().var
        op = ast.getChild(1).value
        right = ast.getLastChild().var
        if op in ['+=', '-=', '/=', '%=']:
            ast.code = [threeAC(left, left, op[0], right)]
        else:
            ast.code = [oneAC(left, right)]

    def exitVariableDeclaration(self, ast):
        expr = ast.getLastChild()
        if expr.name == 'expression':
            ast.code = [oneAC(ast.getChild(1).value, expr.var)]

    def enterIf(self, ast):
        ast.endLabel = lg.nextLabel()

    def exitIf(self, ast):
        block = ast.getBlockIfTrue()

        if not ast.getElifs() and not ast.getElse():
            block.code_before = [testLabel(ast.endLabel)]
            block.code_after = [label(ast.endLabel)]
        else:
            l = lg.nextLabel()
            block.code_before = [testLabel(l)]
            block.code_after = [goto(ast.endLabel), label(l)]

    def exitElse(self, ast):
        ast.code_after = [label(ast.parent.endLabel)]

    def exitElif(self, ast):
        block = ast.getBlock()
        l = lg.nextLabel()
        block.code_before = [testLabel(l)]
        block.code_after = [goto(ast.parent.endLabel), label(l)]

    def enterWhileStatement(self, ast):
        ast.startLabel = lg.nextLabel()
        ast.endLabel = lg.nextLabel()

    def exitWhileStatement(self, ast):
        expr = ast.getFirstChild()
        block = ast.getLastChild()
        expr.code_before = [label(ast.startLabel)]
        expr.code_after = [testLabel(ast.endLabel)]
        block.code_after = [goto(ast.startLabel), label(ast.endLabel)]

    def visitBreak(self, ast):
        ast.code = [goto(ast.getFirstParentByName(CYCLES).endLabel)]

    def visitContinue(self, ast):
        ast.code = [goto(ast.getFirstParentByName(CYCLES).startLabel)]

    def enterForStatement(self, ast):
        ast.startLabel = lg.nextLabel()
        ast.endLabel = lg.nextLabel()

    def exitForStatement(self, ast):
        ast.code_after = [label(ast.endLabel)]

    def exitForCondition(self, ast):
        ast.code_before = [label(ast.parent.startLabel)]
        ast.code_after = [testLabel(ast.parent.endLabel)]

    def exitForUpdate(self, ast):
        ast.code_after = [goto(ast.parent.startLabel)]

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
    ast.code = [threeAC(ast.var, leftVar, '->', sc.value)]
    return ast.var


def makeTAD(ast):
    l = ExpressionTADListener()
    walkAST(l, ast)
    return linkCode(ast)