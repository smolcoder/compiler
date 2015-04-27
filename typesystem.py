INT = 'Int'
STR = 'Str'
BOOL = 'Bool'
NONE = 'None'


class BaseType:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{}:{}'.format(self.__class__.__name__[:-4], self.value)


class PrimitiveType(BaseType):
    pass


class RecordType(BaseType):
    pass


class CortegeType(BaseType):
    pass


class TypeTree:
    def __init__(self):
        self.children = []