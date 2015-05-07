from generator.jasmin import JasminBaseGenerator


class StatementGenerator(JasminBaseGenerator):
    def __init__(self, ast):
        """
        :param ast: Root ast
        """
        JasminBaseGenerator.__init__(self, ast)
        self.gvt = ast.lvt  # global variable table
        self.env = ast.env