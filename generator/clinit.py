from generator.jasmin import JasminBase


class ClinitGenerator(JasminBase):
    def __init__(self, varDeclarations):
        self.varDeclarations = varDeclarations

    # def generate(self, ):