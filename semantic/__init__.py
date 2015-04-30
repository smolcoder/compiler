def checkOnlyOneOuterJustBlock(ast):
    blocks = filter(lambda x: x.name == 'justBlock', ast.getChildren())
    return len(blocks) <= 1