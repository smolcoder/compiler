from errors import DivisionByZeroError
from utils import isInteger, fromBool, toBool


class ASTNode:
    def __init__(self, name, source):
        self.name = name
        self.source = source

        self.left = None
        self.right = None
        self.parent = None
        self.root = None
        self.env = None
        self.globalEnv = None

    def __str__(self):
        return self.name + str(self.source) + ('[{}]'.format(getattr(self, 'type')) if hasattr(self, 'type') else '')

    def __repr__(self):
        return str(self)

    def getGlobalEnv(self):
        if not self.parent:
            if not self.globalEnv:
                self.globalEnv = self.env
            return self.globalEnv
        if not self.globalEnv:
            self.globalEnv = self.parent.getGlobalEnv()
        return self.globalEnv

    def getEnv(self):
        if self.env is not None:
            return self.env
        return self.getHigherEnv()

    def getHigherEnv(self):
        return self.parent.getEnv() if self.parent else None

    def getRoot(self):
        if not self.root:
            self.root = self.parent.getRoot()
        return self.root

    def filterByName(self, name):
        from ast import NameFilterListener  # it's not OK
        from ast import walkAST

        listener = NameFilterListener()
        array = []
        walkAST(listener, self, name, array)
        return array


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

    def removeChildren(self):
        self._children = []

    def removeChild(self, index):
        if index < 0 or index >= len(self._children):
            return None
        c = self._children[index]
        self._children = self._children[:index] + self._children[index+1:]
        c.parent = None
        return c

    def getFirstChild(self):
        return self.getChild(0)

    def getLastChild(self):
        return self.getChild(-1)

    def getChild(self, index):
        return self._children[index]

    def firstManyChildrenDesc(self):
        if len(self._children) != 1:
            return self
        c = self.getFirstChild()
        if isinstance(c, TerminalASTNode):
            return c
        return c.firstManyChildrenDesc()

    def getFirstChildByName(self, name):
        for c in self.getChildren():
            if c.name == name:
                return c
        return None

    def getChildrenByName(self, name):
        return filter(lambda c: c.name == name, self.getChildren())

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
            params.append((c.getChild(0).value, c.getChild(1).typeName))
        return params

    def getReturnType(self):
        return self.getLastChild().getFirstChild().typeName


class VariableDeclarationASTNode(NonTerminalASTNode):
    def getType(self):
        return self.getFirstChild().typeName

    def getName(self):
        return self.getChild(1).value

        # todo getInitializer()?


class LiteralASTNode(TerminalASTNode):
    def __init__(self, source, value):
        TerminalASTNode.__init__(self, self.__class__.__name__[:-7], source, value)


class StrLiteralASTNode(LiteralASTNode):
    def __init__(self, source, value):
        LiteralASTNode.__init__(self, source, value)
        self.type = 'Str'


class IntLiteralASTNode(LiteralASTNode):
    def __init__(self, source, value):
        LiteralASTNode.__init__(self, source, value)
        self.type = 'Int'


class BoolLiteralASTNode(LiteralASTNode):
    def __init__(self, source, value):
        LiteralASTNode.__init__(self, source, value)
        self.type = 'Bool'


class IdASTNode(TerminalASTNode):
    def __init__(self, source, identifier):
        TerminalASTNode.__init__(self, 'Identifier', source, identifier)


class RecordIdASTNode(TerminalASTNode):
    def __init__(self, source, identifier):
        TerminalASTNode.__init__(self, 'RecordID', source, identifier)
        self.typeName = identifier


class PrimitiveTypeASTNode(TerminalASTNode):
    def __init__(self, source, value):
        TerminalASTNode.__init__(self, 'PrimitiveType', source, value)
        self.typeName = value


class OperatorASTNode(TerminalASTNode):
    """
    There is not enough checks!!! Use it carefully
    """
    def perform(self, *args, **kwargs):
        op = self.value
        errors = kwargs.get('errors', [])
        if not args:
            raise Exception('No args found')
        a1 = args[0]
        a2 = args[1] if len(args) > 1 else None

        if op == '!':
            return fromBool(not toBool(a1))
        if op == '-':
            return str(-int(a1))

        if op == '+':
            return str(int(a1) + int(a2))
        if op == '-':
            return str(int(a1) - int(a2))
        if op == '*':
            return str(int(a1) * int(a2))
        if op == '/':
            if int(a2) == 0:
                errors.append(DivisionByZeroError(self.source))
                return "0"
            return str(int(a1) / int(a2))
        if op == '%':
            return str(int(a1) % int(a2))

        if op == '<=':
            return fromBool(int(a1) <= int(a2))
        if op == '==':
            return fromBool(a1 == a2)
        if op == '!=':
            return fromBool(a1 != a2)
        if op == '>=':
            return fromBool(int(a1) >= int(a2))
        if op == '<':
            return fromBool(int(a1) < int(a2))
        if op == '>':
            return fromBool(int(a1) > int(a2))

        if op == '||':
            return fromBool(toBool(a1) or toBool(a2))
        if op == '&&':
            return fromBool(toBool(a1) and toBool(a2))



class ProgrammeASTNode(NonTerminalASTNode):
    def __init__(self, source):
        NonTerminalASTNode.__init__(self, 'Programme', source)
        self.root = self

    def getJustBlock(self):
        for c in self.getChildren():
            if c.name == 'justBlock':
                return c
        return None


class ExpressionASTNode(NonTerminalASTNode):
    def __init__(self, source):
        NonTerminalASTNode.__init__(self, 'expression', source)
        self.type = None

    def getType(self):
        return getattr(self, 'type')

    def getOperator(self):
        op = filter(lambda c: isinstance(c, OperatorASTNode), self._children)
        if op:
            return op[0]
        return None

    def isUnaryOperation(self):
        o = self.getOperator()
        if o and o.name == 'UnaryOperator':
            return o.value
        return None

    def isBinaryOperation(self):
        o = self.getOperator()
        return o.value if o and o.name != 'UnaryOperator' else None

    def isLiteral(self):
        return len(self._children) == 1 and self.getFirstChild().name == 'literal'

    def __str__(self):
        o = self.getOperator()
        if o:
            return '[{}]expression'.format(o.value)
        return NonTerminalASTNode.__str__(self)


class IfStatementASTNode(NonTerminalASTNode):
    def __init__(self, source):
        NonTerminalASTNode.__init__(self, 'if', source)

    def getBlockIfTrue(self):
        return self.getFirstChildByName('justBlock').getFirstChild()

    def getElifs(self):
        return filter(lambda c: c.name == 'elif', self.getChildren())

    def getElse(self):
        return self.getFirstChildByName('else')

    def getCondition(self):
        return self.getFirstChildByName('expression')


class ElseBlockASTNode(NonTerminalASTNode):
    def __init__(self, source):
        NonTerminalASTNode.__init__(self, 'else', source)

    def getBlock(self):
        return self.getFirstChildByName('justBlock').getFirstChild()


class ElifBlockASTNode(NonTerminalASTNode):
    def __init__(self, source):
        NonTerminalASTNode.__init__(self, 'elif', source)

    def getCondition(self):
        return self.getFirstChildByName('expression')

    def getBlock(self):
        return self.getFirstChildByName('justBlock').getFirstChild()