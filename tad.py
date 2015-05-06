class MiddleCode:
    def __repr__(self):
        return str(self)


class ThreeAD(MiddleCode):
    def __init__(self, t1, t2, op, t3, ast=None):
        self.t1 = t1
        self.t2 = t2
        self.op = op
        self.t3 = t3
        self.ast = ast

    def __str__(self):
        return '3: {} := {} {} {}'.format(self.t1, self.t2, self.op, self.t3)


class TwoAD(MiddleCode):
    def __init__(self, t1, t2, ast=None):
        self.t1 = t1
        self.t2 = t2
        self.ast = ast

    def __str__(self):
        return '2: {} := {}'.format(self.t1, self.t2)


class TwoADOp(MiddleCode):
    def __init__(self, t1, op, t2, ast=None):
        self.t1 = t1
        self.op = op
        self.t2 = t2
        self.ast = ast

    def __str__(self):
        return '2: {} := {} {}'.format(self.t1, self.op, self.t2)


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
    def __init__(self, var, name, args):
        self.var = var
        self.name = name
        self.args = args

    def __str__(self):
        return '{} := .create {} {}'.format(self.var, self.name, ' '.join(self.args))


class CallFunction(MiddleCode):
    def __init__(self, var, name, args):
        self.var = var
        self.name = name
        self.args = args

    def __str__(self):
        return '{} := .call {} {}'.format(self.var, self.name, ' '.join(self.args))