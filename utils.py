import os


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


def isRecord(t):
    if isinstance(t, list):
        return False
    return not isPrimitive(t)


def jasmin(jasFile, pathToJar=None, out=None):
    from os import system
    return system('java -jar {} -d {} {}'.format(pathToJar or here('lib', 'jasmin.jar'),
                                          out or here('out'), jasFile))


def java(name, classpath=None):
    cmd = "java -classpath {} {}".format(classpath or here('out'), name)
    # print 'Run {}: {}'.format(name, cmd)
    print '_________________________________________'
    return os.system(cmd)


def run(filename):
    jasmin(filename)
    return java(filename)


ROOT_PATH = os.path.dirname(os.path.realpath(__file__))


def here(*args):
    return os.path.join(ROOT_PATH, *args)


def isInteger(s):
    try:
        int(s)
    except:
        return False
    return True


def toBool(s):
    if s == 'false':
        return False
    elif s == 'true':
        return True
    return None


def fromBool(f):
    return 'true' if f else 'false'
