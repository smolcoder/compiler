class JasminBaseGenerator:
    def __init__(self, ast, filename='Main'):
        self.ast = ast
        self.filename = filename

    def generate(self):
        pass

    def getType(self, actualType):
        if actualType == 'Int':
            return 'I'
        if actualType == 'Bool':
            return 'Z'
        if actualType == 'Str':
            return self.strType
        return self.recType(actualType)

    def limits(self, stack=64, local=64):
        return ['.limit stack {}'.format(stack),
                '.limit locals {}'.format(local)]

    def label(self, l):
        return ['{}:'.format(l)]

    def emptyLine(self):
        return ['']

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

    def comment(self, s):
        return [';    {}'.format(s)]

    @property
    def strType(self):
        return 'Ljava/lang/String;'

    def recType(self, rec):
        return 'LMain${};'.format(rec)