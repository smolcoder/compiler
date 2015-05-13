from ast import BaseASTListener
from utils import isRecord


class ByteCodeGenerateListener(BaseASTListener):
    def __init__(self, lvt, gvt):
        self.code = []
        self.lvt = lvt
        self.gvt = gvt

    @property
    def strType(self):
        return 'Ljava/lang/String;'

    def recType(self, rec):
        return 'LMain${};'.format(rec)

    def methodSignature(self, name, argTypes, retType):
        return '{name}({args}){ret}'.format(
            name=name,
            ret=self.getType(retType),
            args=''.join([self.getType(t) for t in argTypes])
        )

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

    def getLocalArg(self, name):
        info = self.lvt.get(name)
        if isRecord(info['type']) or info['type'] == 'Str':
            return self.aload(str(info['number']))
        return self.iload(str(info['number']))

    def putLocalArg(self, name):
        info = self.lvt.get(name)
        if isRecord(info['type']) or info['type'] == 'Str':
            return self.astore(str(info['number']))
        return self.istore(str(info['number']))

    def pushIfLocalOrConst(self, var):
        """
        Put onto stack
        """
        if isinstance(var, Const):
            return self.pushConst(var.value, var.type)
        if var.status == 'loc':
            info = self.gvt.get(var.name)
            if info:
                return [self.getStaticField(info['name'], info['type'])]
            return [self.getLocalArg(var.name)]
        return []

    def pushConst(self, const, _type):
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

    def storeIfVar(self, var):
        if var.status == 'loc':
            info = self.gvt.get(var.name)
            if info:
                return [self.putStaticField(info['name'], info['type'])]
            return [self.putLocalArg(var.name)]
        return []

    ################################################################

    def exitReturn(self, ast):
        if not ast.getChildren():
            self.code += ['return']
            return
        var = ast.getFirstChild().var
        if var.type == 'None':
            self.code += ['return']
        else:
            if var.type == 'Str' or isRecord(var.type):
                self.code += ['areturn']
            self.code += ['ireturn']

