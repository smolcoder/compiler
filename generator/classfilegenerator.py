from generator.bytecodegenerator import ByteCodeGenerator
from generator.clinit import ClinitGenerator
from generator.jasmin import JasminBaseGenerator
from generator.readType import generateReads
from generator.writeln import generateWriteLn
from utils import here


class ClassFileGenerator(JasminBaseGenerator):
    def __init__(self, className, rootAst, filename):
        JasminBaseGenerator.__init__(self, rootAst, filename)
        self.gEnv = rootAst.getGlobalEnv()
        self.gvt = rootAst.lvt
        self.className = className
        self.mainBlock = self.ast.getJustBlock()

    def makeHead(self):
        return ['.class public {}', '.super java/lang/Object'.format(self.filename)]

    def generate(self):
        bytecode = self.head()
        for r in self.gEnv.records:
            bytecode += self.inner(r)
        bytecode += self.comment('')
        for f in self.gEnv.varOrder:
            bytecode += self.staticField(f, self.gEnv.resolveVariable(f)['type'])

        bytecode += ['.field static __inner__in Ljava/util/Scanner;']

        bytecode += self.comment('')
        bytecode += self.mainInit()
        bytecode += self.comment('')
        bytecode += generateWriteLn()
        bytecode += self.comment('')

        bytecode += generateReads()
        bytecode += self.comment('')

        for f in self.gEnv.functions.values():
            bytecode += self.method(f['ast'], self.gvt)
            bytecode += self.comment('')

        bytecode += self.main()
        bytecode += self.comment('')
        bytecode += ClinitGenerator(self.ast).generate()
        return bytecode

    def bodyGenerator(self, statements, gvt):
        bc = []
        for s in statements:
            bc += ByteCodeGenerator(s, gvt).generate()
        return bc

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
        bc = ['.method public static main([Ljava/lang/String;)V',
              '.limit stack 64',
              '.limit locals 100']
        main = self.bodyGenerator(self.mainBlock.getFirstChild().getChildrenByName('statement'), self.gvt) \
            if self.mainBlock else []
        bc += main
        bc += ['.end method']
        return bc

    def method(self, ast, gvt):
        name = ast.getFirstChild().getName()
        info = self.gEnv.resolveFunction(name)
        retType = info['type']
        argTypes = [t for _, t in info['args']]
        bc = ['.method static {}'.format(self.methodSignature(name, argTypes, retType))]
        bc += self.limits()
        bc += self.bodyGenerator(ast.getLastChild().getChildrenByName('statement'), gvt)
        bc += ['.end method']
        return bc

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