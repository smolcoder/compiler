class ASTNode:
    def __init__(self, name, source):
        self.name = name
        self.source = source

        self.left = None
        self.right = None
        self.parent = None
        self.root = None
        self.env = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def getEnv(self):
        if self.env is not None:
            return self.env
        return self.parent.getEnv() if self.parent else None

    def getRoot(self):
        if not self.root:
            self.root = self.parent.getRoot()
        return self.root


class TerminalASTNode(ASTNode):
    def __init__(self, name, source, value):
        ASTNode.__init__(self, name, source)
        self.value = value

    def getDeepest(self):
        return self

    def __str__(self):
        return '{}[{}]'.format(self.name, self.value) if self.value is not None else self.name


class NonTerminalASTNode(ASTNode):
    def __init__(self, name, source):
        ASTNode.__init__(self, name, source)
        self._children = []

    def getChildren(self):
        return self._children

    def addChild(self, ast):
        ast.parent = self
        if self._children:
            ast.left = self._children[-1]
            self._children[-1].right = ast
        self._children.append(ast)

    def getFirstChild(self):
        return self._children[0]

    def getLastChild(self):
        return self._children[-1]

    def getChild(self, index):
        return self._children[index]

    def getFirstChildByName(self, name):
        for c in self.getChildren():
            if c.name == name:
                return c
        return None

    def getDeepest(self):
        if len(self._children) != 1:
            raise Exception('Node {} has zero, two or more children.'.format(self))
        first = self.getFirstChild()
        return first if isinstance(first, TerminalASTNode) else first.getDeepest()


class FunctionSignatureASTNode(NonTerminalASTNode):
    def getName(self):
        return self.getFirstChild().value

    def getArguments(self):
        paramsNode = self.getFirstChildByName('functionParameterList')
        if not paramsNode:
            return []
        params = []
        for c in paramsNode.getChildren():
            params.append((c.getChild(0).value, c.getChild(1).type))
        return params

    def getReturnType(self):
        return self.getLastChild().getFirstChild().type


class VariableDeclarationASTNode(NonTerminalASTNode):
    def getType(self):
        return self.getFirstChild().type

    def getName(self):
        return self.getChild(1).value

        # todo getInitializer()?


class LiteralASTNode(TerminalASTNode):
    def __init__(self, source, value):
        TerminalASTNode.__init__(self, self.__class__.__name__[:-7], source, value)


class StrLiteralASTNode(LiteralASTNode):
    pass


class IntLiteralASTNode(LiteralASTNode):
    pass


class BoolLiteralASTNode(LiteralASTNode):
    pass


class IdASTNode(TerminalASTNode):
    def __init__(self, source, identifier):
        TerminalASTNode.__init__(self, 'Identifier', source, identifier)


class RecordIdASTNode(TerminalASTNode):
    def __init__(self, source, identifier):
        TerminalASTNode.__init__(self, 'RecordID', source, identifier)
        self.type = identifier


class PrimitiveTypeASTNode(TerminalASTNode):
    def __init__(self, source, value):
        TerminalASTNode.__init__(self, 'PrimitiveType', source, value)
        self.type = value


class CortegeTypeASTNode(NonTerminalASTNode):
    def __init__(self, name, source):
        NonTerminalASTNode.__init__(self, name, source)


class OperatorASTNode(TerminalASTNode):
    pass


class ProgrammeASTNode(NonTerminalASTNode):
    def __init__(self, source):
        NonTerminalASTNode.__init__(self, 'Programme', source)
        self.root = self