from localvartable import LocalVariableTable
from tad import *


class JasminBase:
    def getType(self, actualType):
        if actualType == 'Int':
            return 'I'
        if actualType == 'Bool':
            return 'Z'
        if actualType == 'Str':
            return self.strType
        return self.recType(actualType)

    def globalHead(self):
        return ['.class public Greeter', '.super java/lang/Object']

    def limits(self, stack, local):
        return ['.limit stack {}'.format(stack),
                '.limit locals {}'.format(local)]

    # def defaultConstructor(self):
    #     return ['.method public <init>()V',
    #             'aload_0',
    #             'invokespecial java/lang/Object/<init>()V',
    #             'return',
    #             '.end method']

    # def wrapInMain(self, code):
    #     code = ['.method public static main([Ljava/lang/String;)V'] + code
    #     code += '.end method'
    #     return code

    def _arg_opt_command(self, cmd, const):
        if const not in [0, 1, 2, 3]:
            return ['{}} {}'.format(cmd, const)]
        return '{}_{}'.format(cmd, const)

    def iload(self, const):
        return self._arg_opt_command('iload', const)

    def aload(self, const):
        return self._arg_opt_command('aload', const)

    def astore(self, const):
        return self._arg_opt_command('astore', const)

    def pushBool(self, value):
        if value in ['0', 0, 'false']:
            return ['iconst_0']
        return ['iconst_1']

    def invokestatic(self, ast):
        return ''

    def push_const(self, const):
        if const in [0, 1, 2, 3, 4, 5]:
            return 'iconst_{}'.format(const)
        return 'ldc {}'.format(const)

    @property
    def strType(self):
        return 'Ljava/lang/String;'

    def recType(self, rec):
        return 'LMain${};'.format(rec)


class ExpressionJasmin(JasminBase):
    def __init__(self, tad, lvt):
        """
        :type lvt: LocalVariableTable
        """
        self.tad = tad
        self.lvt = lvt
        self.bytecode = []
        self.parseLines()

    def parseThreeAD(self, tad):
        pass

    def parseTwoAD(self, tad):
        pass

    def parseTwoADOp(self, tad):
        pass

    def parseLines(self):
        for l in self.tad:
            if isinstance(l, ThreeAD):
                self.parseThreeAD(l)
            if isinstance(l, TwoAD):
                self.parseTwoAD(l)
            if isinstance(l, TwoADOp):
                self.parseTwoADOp(l)