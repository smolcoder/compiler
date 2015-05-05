from ast import BaseASTListener, walkAST


class CodeLinkerListener(BaseASTListener):
    def __init__(self):
        self.code = []

    def commonAction(self, ast):
        if hasattr(ast, 'code'):
            self.code.append(ast.code)

    def exitEvery(self, ast):
        self.commonAction(ast)


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


ng = NameGenerator()


def threeAC(var, left, op, right):
    return '{} := {} {} {}'.format(var, left, op, right)


def twoAC(var, op, arg):
    return '{} := {} {}'.format(var, op, arg)


class ExpressionTADListener(BaseASTListener):
    def exitExpression(self, ast):
        fc = ast.getFirstChild()
        op = ast.getOperator().value if ast.getOperator() else None

        if fc.name == 'literal':
            ast.var = ast.getDeepest().value
        elif fc.name == 'leftHandSide':
            ast.var = fc.var
        elif fc.name == 'functionInvocation':
            ast.var = fc.var
        elif op:
            ast.var = ng.nextName()
            if ast.isUnaryOperation():
                ast.code = twoAC(ast.name, op, ast.getLastChild().var)
            else:
                left = fc.var
                right = ast.getLastChild().var
                ast.code = threeAC(ast.var, left, op, right)
        # else:
        #     print fc.name
        # else:
        #     ast.code

    def exitFunctionInvocation(self, ast):
        ast.var = ng.nextName()
        ast.code = twoAC(ast.var, 'invoke', ast.getFirstChild().value)

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
            ast.code = threeAC(left, left, op[1], right)
        else:
            ast.code = twoAC(left, op, right)


def recordAccessCode(ast):
    fc = ast.getFirstChild()
    if fc.name == 'Identifier':
        ast.var = fc.value
        return ast.var
    ast.var = ng.nextName()
    sc = ast.getLastChild()
    leftVar = recordAccessCode(fc)
    ast.code = threeAC(ast.var, leftVar, 'access', sc.value)
    # return field + '.' + sc.value
    return ast.var


def makeTAD(ast):
    l = ExpressionTADListener()
    walkAST(l, ast)
    return linkCode(ast)