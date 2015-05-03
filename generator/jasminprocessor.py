class JasminProcessor:
    def head(self):
        return ['.class public Greeter', '.super java/lang/Object']

    def defaultConstructor(self):
        return ['.method public <init>()V',
                'aload_0',
                'invokespecial java/lang/Object/<init>()V',
                'return',
                '.end method']

    def wrapInMain(self, code):
        code = ['.method public static main([Ljava/lang/String;)V'] + code
        code += '.end method'
        return code

    def _arg_opt_command(self, cmd, const):
        if const not in [0, 1, 2, 3]:
            return ['{}} {}'.format(cmd, const)]
        return ['{}_{}'.format(cmd, const)]

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

    def getStringType(self):
        return 'Ljava/lang/String;'


JPROC = JasminProcessor()


def evaluateExpression(ast):
    pass