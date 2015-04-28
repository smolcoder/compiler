class CompilerError:
    def __init__(self, msg, line=None, column=None):
        self.msg = msg
        self.line = line
        self.column = column

    def __str__(self):
        if self.line is not None and self.column is not None:
            return '{}:{}: {}'.format(self.line, self.column, self.msg)
        else:
            return self.msg

    def __repr__(self):
        return str(self)