def capitalizeFirst(s):
    return s[0].capitalize() + s[1:]


def getRuleName(ctx):
    return ctx.parser.ruleNames[ctx.getRuleIndex()]


class Stack:
    def __init__(self):
        self.stack = []
        self.pop = self.stack.pop

    def __len__(self):
        return len(self.stack)

    def push(self, elt):
        self.stack.append(elt)

    def top(self):
        return self.stack[-1]


class SourceInfo:
    def __init__(self, firstPos, lastPos, line, column):
        self.first_pos = firstPos
        self.last_pos = lastPos
        self.line = line
        self.column = column

    def __str__(self):
        return '[{}:{}]'.format(self.line, self.column)

    def __repr__(self):
        return str(self)


def isPrimitive(t):
    return t in ['Int', 'Str', 'Bool', 'None']


def jasmin(filename):
    from os import system
    system('java -jar lib/jasmin.jar -d out/ sources/jas/{}.j'.format(filename))


def java(classname):
    from os import system
    system("java -cp 'out' {}".format(classname))


def run(filename):
    jasmin(filename)
    java(filename)