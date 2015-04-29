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