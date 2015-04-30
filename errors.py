class CompilerError:
    def __init__(self, msg, source=None):
        """
        :type source: SourceInfo
        """
        self.source = source
        self.msg = msg

    def __str__(self):
        if self.source is not None and self.source.line is not None and self.source.column is not None:
            return '{}:{}: {}'.format(self.source.line, self.source.column, self.msg)
        else:
            return self.msg

    def __repr__(self):
        return str(self)


class NameNotFoundError(CompilerError):
    def __init__(self, name, source=None):
        CompilerError.__init__(self, "Name '{}' not found".format(name), source)


class NameAlreadyDefinedError(CompilerError):
    def __init__(self, name, source=None):
        CompilerError.__init__(self, "Name '{}' already defined".format(name), source)


class LLangSyntaxError(CompilerError):
    def __init__(self, msg, source=None):
        CompilerError.__init__(self, "Syntax error: {}".format(msg), source)