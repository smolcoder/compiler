class JasminBaseGenerator:
    def __init__(self, ast, filename='Main'):
        """
        Compiles given AST to JVM mnemonic bytecode.
        See Jasmin tool and its syntax for more information.

        :type ast: NonTerminalASTNode
        """
        self.ast = ast
        self.filename = filename

    def generate(self):
        """
        Return mnemonic JVM bytecode of given AST
        :return: list of str
        """
        pass

    def getType(self, actualType):
        if actualType == 'Int':
            return 'I'
        if actualType == 'Bool':
            return 'Z'
        if actualType == 'Str':
            return self.strType
        if actualType == 'None':
            return 'V'
        return self.recType(actualType)

    def getStaticField(self, name, _type):
        return 'getstatic Main/{} {}'.format(name, self.getType(_type))

    def putStaticField(self, name, _type):
        return 'putstatic Main/{} {}'.format(name, self.getType(_type))

    def limits(self, stack=64, local=64):
        return ['.limit stack {}'.format(stack),
                '.limit locals {}'.format(local)]

    def label(self, l):
        return ['{}:'.format(l)]

    def emptyLine(self):
        return ['']

    def _arg_opt_command(self, cmd, const):
        if const not in ['0', '1', '2', '3']:
            return '{} {}'.format(cmd, const)
        return '{}_{}'.format(cmd, const)

    def iload(self, const):
        return self._arg_opt_command('iload', const)

    def aload(self, const):
        return self._arg_opt_command('aload', const)

    def astore(self, const):
        return self._arg_opt_command('astore', const)

    def istore(self, const):
        return self._arg_opt_command('istore', const)

    def invokestatic(self, name, argTypes, actualType):
        return ['invokestatic Main/{}'.format(self.methodSignature(name, argTypes, actualType))]

    def methodSignature(self, name, argTypes, retType):
        return '{name}({args}){ret}'.format(
            name=name,
            ret=self.getType(retType),
            args=''.join([self.getType(t) for t in argTypes])
        )

    def push_const(self, const, _type):
        if _type == 'Str':
            return ['ldc "{}"'.format(const)]
        if _type in ['Int', 'Bool'] and const in ['0', '1', '2', '3', '4', '5']:
            return ['iconst_{}'.format(const)]
        if const in ['true', 'false']:
            return ['iconst_0' if const == 'false' else 'iconst_1']
        try:
            i = int(const)
            if -128 <= i < 128:
                return ['bipush {}'.format(const)]
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


GET_MNEMONIC_ARITH = {
    '+': 'iadd',
    '-': 'isub',
    '*': 'imul',
    '/': 'idiv',
    '%': 'irem',
    }

GET_MNEMONIC_CMP = {
    '<': 'if_icmplt',
    '<=': 'if_icmple',
    '>': 'if_icmpgt',
    '>=': 'if_icmpge',
    '!=': 'if_icmpne',
    '==': 'if_icmpeq',
    }