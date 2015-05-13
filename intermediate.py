from pprint import pprint
from ast import CYCLES, BaseASTListener, TerminalASTNode, walkAST, pprintAST


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


class RecordFieldAccessVariable(TACEntity):
    def __init__(self, ast):
        self.ast = ast
        self.type = ast.type

    def __str__(self):
        return self.ast.getText()


class NameGenerator:
    counter = 0

    def nextVariable(self, _type, status='mid'):
        var = '__t{}'.format(self.counter)
        self.counter += 1
        return Variable(var, _type, status=status)


class LabelGenerator:
    counter = 0

    def nextLabel(self):
        var = 'Label{}'.format(self.counter)
        self.counter += 1
        return var


LABEL_GENERATOR = LabelGenerator()


class BuildMiddleCodeListener(BaseASTListener):
    # todo remove code addition
    def __init__(self, globalEnv):
        self.globalEnv = globalEnv
        self.ng = NameGenerator()

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
            ast.var = Const(ast.getDeepest().value, fc.getFirstChild().type)
        elif op:
            ast.var = self.ng.nextVariable(ast.type)
        elif fc.name == 'functionInvocation':
            ast.var = fc.var
        elif fc.name == 'readIntCall':
            ast.var = fc.var
        elif fc.name == 'readStrCall':
            ast.var = fc.var
        elif fc.name == 'readBoolCall':
            ast.var = fc.var
        elif fc.name == 'leftHandSide':
            ast.var = fc.var
        elif fc.name == 'recordInitializer':
            ast.var = fc.var

    def exitFunctionInvocation(self, ast):
        ast.var = self.ng.nextVariable(ast.type)

    def enterRecordInitializer(self, ast):
        ast.var = self.ng.nextVariable(ast.type)

    def exitLeftHandSide(self, ast):
        fc = ast.getFirstChild()
        if fc.name == 'Identifier':
            ast.var = Variable(fc.value, ast.type, status='loc')
        elif fc.name == 'recordFieldAccess':
            ast.var = RecordFieldAccessVariable(fc)

    def exitReadIntCall(self, ast):
        ast.var = self.ng.nextVariable(ast.type)

    def exitReadBoolCall(self, ast):
        ast.var = self.ng.nextVariable(ast.type)

    def exitReadStrCall(self, ast):
        ast.var = self.ng.nextVariable(ast.type)


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
    opt = OptimizerListener()
    for bb in bbs:
        cache = {}
        rCache = {}
        for statement in bb:
            walkAST(opt, statement, cache, rCache)
            pprint(cache)


class OptimizerListener(BaseASTListener):
    def exitExpression(self, ast, cache, rCache):
        fc = ast.getFirstChild()
        op = ast.getOperator().value if ast.getOperator() else None

        if not op:
            return
        if ast.isUnaryOperation():
            child__var = str(ast.getLastChild().var)
            text = '{} {}'.format(op, child__var)
            if child__var not in rCache:
                rCache[child__var] = []
            rCache[child__var].append(text)
        else:
            lAst = fc
            rAst = ast.getLastChild()
            left = lAst.var
            right = rAst.var
            text = '{} {} {}'.format(left, op, right)
        if text not in cache:
            cache[text] = ast.var
        else:
            var = cache[text]
            var.status = 'loc'
            ast.var.link = var