from ast import BaseASTListener, walkAST


class CodeLinkerListener(BaseASTListener):
    def __init__(self):
        self.code = []

    def visitTerminal(self, ast):
        if hasattr(ast, 'code_before'):
            self.code += ast.code_before
        if hasattr(ast, 'code'):
            self.code += ast.code
        if hasattr(ast, 'code_after'):
            self.code += ast.code_after

    def enterEvery(self, ast):
        if hasattr(ast, 'code_before'):
            self.code += ast.code_before

    def exitEvery(self, ast):
        if hasattr(ast, 'code'):
            self.code += ast.code
        if hasattr(ast, 'code_after'):
            self.code += ast.code_after


def linkCode(ast):
    l = CodeLinkerListener()
    walkAST(l, ast)
    return l.code


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
        # else:
        #     print fc.name
        # else:
        #     ast.code

    def exitFunctionInvocation(self, ast):
        ast.var = ng.nextName()
        args = []
        for c in ast.getLastChild().getChildren():
            args.append(c.var)
        ast.code = [twoAC(ast.var, 'invoke', '{}({})'.format(ast.getFirstChild().value, ','.join(args)))]

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
        if op in ['+=, -=, /=', '%=']:
            ast.code = [threeAC(left, left, op[1], right)]
        else:
            ast.code = [twoAC(left, op, right)]

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
        ast.whileLabel = lg.nextLabel()
        ast.endLabel = lg.nextLabel()

    def exitWhileStatement(self, ast):
        expr = ast.getFirstChild()
        block = ast.getLastChild()
        expr.code_before = [label(ast.whileLabel)]
        expr.code_after = [testLabel(ast.endLabel)]
        block.code_after = [goto(ast.whileLabel), label(ast.endLabel)]

    def visitBreak(self, ast):
        ast.code = [goto(ast.getFirstParentByName('whileStatement').endLabel)]

    def visitContinue(self, ast):
        ast.code = [goto(ast.getFirstParentByName('whileStatement').whileLabel)]


def recordAccessCode(ast):
    fc = ast.getFirstChild()
    if fc.name == 'Identifier':
        ast.var = fc.value
        return ast.var
    ast.var = ng.nextName()
    sc = ast.getLastChild()
    leftVar = recordAccessCode(fc)
    ast.code = [threeAC(ast.var, leftVar, 'access', sc.value)]
    return ast.var


def makeTAD(ast):
    l = ExpressionTADListener()
    walkAST(l, ast)
    return linkCode(ast)