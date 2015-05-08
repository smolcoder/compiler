from generator.bytecodegenerator import ByteCodeGenerator
from generator.jasmin import GET_MNEMONIC_CMP, GET_MNEMONIC_ARITH
from generator.linker import linkCode
from middlecode import *
from utils import isRecord
from ast.nodes import ProgrammeASTNode


class ClinitGenerator(ByteCodeGenerator):
    def __init__(self, ast):
        """
        :type ast: ProgrammeASTNode
        """
        ByteCodeGenerator.__init__(self, ast, ast.getLVT())

    def generate(self):
        bytecode = ['.method static <clinit>()V'] + self.limits()
        for v in self.gEnv.varOrder:
            if self.gvt.get(v)['ast'].getLastChild().name != 'expression':
                continue
            bytecode += self.processVarDec(self.gvt.get(v))
        bytecode += ['new java/util/Scanner',
                     'dup',
                     'getstatic java/lang/System/in Ljava/io/InputStream;',
                     'invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V',
                     'putstatic Main/__inner__in Ljava/util/Scanner;']
        bytecode += ['return', '.end method']
        return bytecode

    def processVarDec(self, varDec):
        lc = linkCode(varDec['ast'])
        bc = ['; line {}'.format(varDec['ast'].source.line)]
        for l in lc:
            bc += self.processLine(l)
        return bc