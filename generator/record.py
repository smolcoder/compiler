from generator.classfilegenerator import ClassFileGenerator
from utils import isRecord


class RecordGenerator(ClassFileGenerator):
    def __init__(self, recordName, ast, filename='Main'):
        self.filename = filename
        self.className = recordName
        self.ast = ast

    def generate(self):
        env = self.ast.getEnv()
        fields = [(name, env.resolveVariable(name)['type']) for name in env.varOrder]
        inners = [self.className] + [t for _, t in fields if isRecord(t)]

        genFields = [self.field(n, t)[0] for n, t in fields]
        genInners = [self.inner(t)[0] for t in inners]
        return self.head() + self.comment('') + \
               genInners + self.comment('') + \
               genFields + self.comment('') + \
               self.constructor(fields)

    def field(self, name, actualType):
        return ['.field {} {}'.format(name, self.getType(actualType))]

    def head(self):
        template = """.source {sourceFileName}.java
                      .class {sourceFileName}${recordName}
                      .super java/lang/Object"""
        s = template.format(recordName=self.className,
                            sourceFileName=self.filename)
        return self.ss(s)

    def constructor(self, fields):
        template = """.method <init>({signature})V
                     .limit stack 2
                     .limit locals {local}
                     aload_0
                     invokespecial java/lang/Object/<init>()V
                     {inits}
                     return
                     .end method"""
        inits = []
        for i, (f, t) in enumerate(fields):
            inits += self.initField(i + 1, f, t)
        s = template.format(signature=''.join([self.getType(t) for _, t in fields]),
                            inits='\n'.join(inits),
                            local=len(fields) + 1)
        return self.ss(s)


    def initField(self, number, fieldName, fieldActualType):
        template = """aload_0
                     {loadCmd}
                     putfield {sourceFileName}${recordName}/{fieldName} {fieldType}
                     """
        s = template.format(recordName=self.className,
                            fieldType=self.getType(fieldActualType),
                            fieldName=fieldName,
                            sourceFileName=self.filename,
                            loadCmd=self.aload(number) if isRecord(fieldActualType) or fieldActualType == 'Str'
                            else self.iload(number))
        return self.ss(s)