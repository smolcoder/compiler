class MiddleCode:
    def __repr__(self):
        return str(self)


class ThreeAC(MiddleCode):
    def __init__(self, t1, t2, op, t3, resType, ast=None):
        self.t1 = t1
        self.t2 = t2
        self.op = op
        self.t3 = t3
        self.ast = ast
        self.type = resType

    def __str__(self):
        return '{} := {} {} {}'.format(self.t1, self.t2, self.op, self.t3)


class TwoAC(MiddleCode):
    def __init__(self, t1, t2, resType, ast=None):
        self.t1 = t1
        self.t2 = t2
        self.ast = ast
        self.type = resType

    def __str__(self):
        return '{} := {}'.format(self.t1, self.t2)


class TwoACOp(MiddleCode):
    def __init__(self, t1, op, t2, resType, ast=None):
        self.t1 = t1
        self.op = op
        self.t2 = t2
        self.ast = ast
        self.type = resType

    def __str__(self):
        return '{} := {} {}'.format(self.t1, self.op, self.t2)


class Label(MiddleCode):
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return '.label {}'.format(self.label)


class TestCondition(MiddleCode):
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return '.test {}'.format(self.label)


class GoTo(MiddleCode):
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return '.goto {}'.format(self.label)


class CreateRecord(MiddleCode):
    def __init__(self, var, name, types):
        self.t1 = var
        self.name = name
        self.types = types

    def __str__(self):
        return '{} := .create {}'.format(self.t1, self.name)


class NewRecord(MiddleCode):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '.new {}'.format(self.name)


class CallFunction(MiddleCode):
    def __init__(self, var, name):
        self.var = var
        self.name = name

    def __str__(self):
        return '{} := .call {}'.format(self.var, self.name)


class TACEntity:
    pass


class Const(TACEntity):
    def __init__(self, value, _type):
        self.value = value
        self.type = _type

    def getByteCode(self):
        if self.type == 'Bool':
            if self.value == 'true':
                return ['iconst_1']
            return ['iconst_0']
        if self.value in [0, 1, 2, 3, 4, 5]:
            return ['iconst_{}'.format(self.value)]
        return ['ldc {}'.format(self.value)]

    def __str__(self):
        if self.type == 'Str':
            return 'const."{}"'.format(self.value)
        return 'const.{}'.format(self.value)


class Variable(TACEntity):
    def __init__(self, name, _type, status='mid', ast=None):
        self.name = name
        self.status = status
        self.ast = ast
        self.type = _type

    def isMiddle(self):
        return self.status == 'mid'

    def isLocal(self):
        return self.status == 'loc'

    def __str__(self):
        return '{}.{}'.format(self.status, self.name)