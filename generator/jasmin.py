from ast import BaseASTListener
from localvartable import LocalVariableTable
from middlecode import *


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

    def invokestatic(self, ast):
        return ''

    def push_const(self, const):
        if const in ['0', '1', '2', '3', '4', '5']:
            return ['iconst_{}'.format(const)]
        if const in ['true', 'false']:
            return ['iconst_0' if const == 'false' else 'iconst_1']
        try:
            int(const)
            return ['ldc {}'.format(const)]
        except:
            return ['ldc "{}"'.format(const)]

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

    def processThreeAD(self, tad):
        pass

    def processTwoAD(self, tad):
        if isinstance(tad.t2, Const):
            self.bytecode += tad.t2.getByteCode()

    def processTwoADOp(self, tad):
        pass

    def processLines(self):
        for l in self.tad:
            methodName = 'process{}'.format(l.__class__.__name__)
            if hasattr(self, methodName):
                getattr(self, methodName)(l)


class MainGenListener(BaseASTListener):
    def __init__(self, rootAst):
        self.bytecode = []
        self.gEnv = rootAst.getGlovalEnv()
        self.gvt = rootAst.lvt

    # def