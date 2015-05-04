from generator.jasmin import JasminBase
from utils import isRecord, here


class RecordGenerator(JasminBase):
    def __init__(self, recordName, ast, sourceFileName='Main'):
        self.ast = ast
        self.recordName = recordName
        self.sourceFileName = sourceFileName

    def generate(self):
        env = self.ast.getEnv()
        fields = [(name, env.resolveVariable(name)['type']) for name in env.variables]
        inners = [self.recordName] + [t for _, t in fields if isRecord(t)]

        genFields = [self.field(n, t) for n, t in fields]
        genInners = [self.inner(t) for t in inners]
        genConstructors = []
        for n, t in fields:
            genConstructors += self.constructor(n, t)
        return self.head() + genInners + genFields + genConstructors

    def generateToFile(self, path):
        f = open(here(path, self.recordName + '.j'), 'w')
        f.write('\n'.join(self.generate()))
        f.close()

    def field(self, name, actualType):
        return '.field {} {}'.format(name, self.getType(actualType))

    def inner(self, recordName):
        return '.inner class static {recordName} inner {sourceFileName}${recordName} outer {sourceFileName}'.format(
            recordName=recordName,
            sourceFileName=self.sourceFileName
        )

    def head(self):
        template = """.source {sourceFileName}.java
                      .class {sourceFileName}${recordName}
                      .super java/lang/Object"""
        s = template.format(recordName=self.recordName,
                            sourceFileName=self.sourceFileName)
        return map(lambda x: x.strip(), s.split('\n'))

    def constructor(self, fieldName, fieldActualType):
        template = """.method <init>({fieldType})V
    .limit stack 2
    .limit locals 2
    aload_0
    invokespecial java/lang/Object/<init>()V
    aload_0
    {loadCmd}
    putfield {sourceFileName}${recordName}/{fieldName} {fieldType}
    return
.end method"""
        s = template.format(recordName=self.recordName,
                            fieldType=self.getType(fieldActualType),
                            fieldName=fieldName,
                            sourceFileName=self.sourceFileName,
                            loadCmd='aload_1' if isRecord(fieldActualType) or fieldActualType == 'Str' else 'iload_1')
        return s.split('\n')