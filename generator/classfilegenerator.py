from generator.clinit import ClinitGenerator
from generator.jasmin import JasminBaseGenerator
from utils import here


class ClassFileGenerator(JasminBaseGenerator):
    def __init__(self, className, rootAst, filename):
        JasminBaseGenerator.__init__(self, rootAst, filename)
        self.gEnv = rootAst.getGlobalEnv()
        self.gvt = rootAst.lvt
        self.className = className

    def makeHead(self):
        return ['.class public {}', '.super java/lang/Object'.format(self.filename)]

    def generate(self):
        bytecode = self.head()
        for r in self.gEnv.records:
            bytecode += self.inner(r)
        bytecode += self.comment('')
        for f in self.gEnv.varOrder:
            bytecode += self.staticField(f, self.gEnv.resolveVariable(f)['type'])
        bytecode += self.comment('')
        bytecode += self.mainInit()
        bytecode += self.comment('')
        bytecode += self.main()
        bytecode += self.comment('')
        bytecode += ClinitGenerator(self.ast).generate()
        return bytecode

    def generateToFile(self, path):
        print path, self.className
        f = open(here(path, self.className + '.j'), 'w')
        f.write('\n'.join(self.generate()))
        f.close()

    def staticField(self, name, actualType):
        return ['.field static {} {}'.format(name, self.getType(actualType))]

    def inner(self, recordName):
        inner = '.inner class static {recordName} inner {sourceFileName}${recordName} outer {sourceFileName}'.format(
            recordName=recordName,
            sourceFileName=self.filename
        )
        return [inner]

    def mainInit(self):
        return self.ss(""".method public <init>()V
                           .limit stack 1
                           .limit locals 1
                           aload_0
                           invokespecial java/lang/Object/<init>()V
                           return
                           .end method""")

    def main(self):
        template = """.method public static main([Ljava/lang/String;)V
                      .limit stack 0
                      .limit locals 1
                      return
                      .end method"""
        return self.ss(template)

    def head(self):
        template = """.source {filename}.java
                      .class public {className}
                      .super java/lang/Object""".format(
            filename=self.filename,
            className=self.className
        )
        return self.ss(template)

    def ss(self, code):
        return map(lambda x: x.strip(), code.split('\n'))