from ast import BaseASTListener, walkAST, NonTerminalASTNode, ReturnASTNode
from errors import TypeMismatchError, CompilerError


class NormalizeRecordInitializerListener(BaseASTListener):
    def __init__(self, globalEnv):
        self.globalEnv = globalEnv

    def exitRecordFieldInitializerList(self, ast):
        varInits = {}
        recordName = ast.parent.getFirstChild().value
        env = self.globalEnv.resolveRecord(recordName)['env']
        for fieldInit in ast.getChildren():
            varInits[fieldInit.getFirstChild().value] = fieldInit
        ast.removeChildren()
        for name in env.varOrder:
            ast.addChild(varInits[name])


def normalizeRecordInitializer(ast):
    l = NormalizeRecordInitializerListener(ast.getGlobalEnv())
    walkAST(l, ast)


def checkReturns(ast):
    functions = ast.filterByName('functionDeclaration')
    errors = []

    for f in functions:
        _type = f.getFirstChild().getReturnType()
        returns = f.filterByName('return')
        if _type != 'None' and not returns:
            errors.append(CompilerError('Return statement is missed.', source=f.source))
        for r in returns:
            if r.getType() != _type:
                errors.append(TypeMismatchError(r.source, msg='bad return type: {} != {}'.format(r.getType(), _type)))
        body = f.getLastChild()
        if _type == 'None':
            addLastReturn(body)

    if ast.getJustBlock():
        mainBlock = ast.getJustBlock().getFirstChild()
        returns = mainBlock.filterByName('return')
        for r in returns:
            if r.getType() != 'None':
                errors.append(TypeMismatchError(r.source, msg='return from main block is not None'))
    else:
        justBlock = NonTerminalASTNode('justBlock', None)
        mainBlock = NonTerminalASTNode('block', None)
        justBlock.addChild(mainBlock)
    addLastReturn(mainBlock)
    return errors


def addLastReturn(body):
    if not body.getChildren() or body.getLastChild().getFirstChild().name != 'return':
        stmt = NonTerminalASTNode('statement', None)
        stmt.addChild(ReturnASTNode(None))
        body.addChild(stmt)