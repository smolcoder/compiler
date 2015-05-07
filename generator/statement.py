from ast import NonTerminalASTNode
from generator.jasmin import JasminBaseGenerator, GET_MNEMONIC_CMP, GET_MNEMONIC_ARITH
from generator.linker import linkCode
from middlecode import *
from localvartable import LocalVariableTable
from utils import isRecord


class StatementGenerator(JasminBaseGenerator):
    def __init__(self, ast, gvt):
        """
        :type ast: NonTerminalASTNode
        :type gvt: LocalVariableTable
        """
        JasminBaseGenerator.__init__(self, ast)
        self.lvt = ast.getLVT()  # global variable table
        self.gvt = gvt

    def generate(self):
        lc = linkCode(self.ast)
        bc = []
        for l in lc:
            bc += self.processLine(l)
        return bc

    def getLocalArg(self, name):
        info = self.lvt.get(name)
        if isRecord(info['type']) or info['type'] == 'Str':
            return self.aload(str(info['number'] + 1))
        return self.iload(str(info['number'] + 1))

    def putLocalArg(self, name):
        info = self.lvt.get(name)
        if isRecord(info['type']) or info['type'] == 'Str':
            return self.astore(str(info['number'] + 1))
        return self.istore(str(info['number'] + 1))

    def pushIfLocalOrConst(self, var):
        """
        Put onto stack
        """
        if isinstance(var, Const):
            return self.push_const(var.value)
        if var.status == 'loc':
            return [self.getLocalArg(var.name)]
        return []

    def storeIfLocal(self, var):
        if var.status == 'loc':
            return [self.putLocalArg(var.name)]
        return []

    def processLine(self, line):
        bytecode = []
        if isinstance(line, CreateRecord):
            bytecode += ['invokespecial Main${}/<init>({})V'.format(
                line.name,
                ''.join([self.getType(t) for t in line.types])
            )]

        # elif isinstance(line, CallFunction):
        #     fEnv = self.env.resolveFunction(line.name)
        #     _type = ''.join([self.getType(t) for n, t in fEnv['args']])
        #     rType = self.getType(fEnv['type'])
        #     bytecode += ['invokestatic Main/{}({}){}'.format(line.name, _type, rType)]

        # elif isinstance(line, AccessRecordField):
        #     if line.t2.status == 'loc':
        #         bytecode += [self.getLocalArg(line.t2.name)]
        #     bytecode += ['getfield Main${}/{} {}'.format(line.t2.type, line.t3, self.getType(line.type))]

        elif isinstance(line, Push):
            if isinstance(line.var, Const):
                bytecode += self.push_const(line.var.value)
            else:
                bytecode += [self.getLocalArg(line.var.name)]
        elif isinstance(line, IfNeEq):
            bytecode += self.pushIfLocalOrConst(line.var)
            bytecode += ['if{} {}'.format('ne' if line.op == '!=' else 'eq', line.label)]
        elif isinstance(line, Label):
            bytecode += self.label(line.label)
        elif isinstance(line, TestCondition):
            bytecode += ['ifeq {}'.format(line.label)]
        elif isinstance(line, PushBoolConst):
            bytecode += self.push_const('1' if line.f else '0')
        elif isinstance(line, GoTo):
            bytecode += ['goto {}'.format(line.label)]
        elif isinstance(line, WriteLnCall):
            bytecode += ['invokestatic Main/writeln([Ljava/lang/Object;)V']
        elif isinstance(line, AAstore):
            t = line.var.type
            if t == 'Bool':
                bytecode += ['invokestatic java/lang/Boolean/valueOf(Z)Ljava/lang/Boolean;']
            elif t == 'Int':
                bytecode += ['invokestatic java/lang/Integer/valueOf(I)Ljava/lang/Integer;']
            bytecode += ['aastore']
            if not line.isLast:
                bytecode += ['dup']
        elif isinstance(line, NewArray):
            bytecode += self.push_const(str(line.size))
            bytecode += ['anewarray java/lang/Object', 'dup']

        elif isinstance(line, Return):
            bytecode += self.makeReturn(line.var.type if line.var else 'None')

        elif isinstance(line, (TwoAC, TwoACOp, ThreeAC)):
            if isinstance(line, TwoAC):
                bytecode += self.pushIfLocalOrConst(line.t2)
            elif isinstance(line, TwoACOp):
                op = line.op
                bytecode += self.pushIfLocalOrConst(line.t2)
                if op == '-':
                    bytecode += ['ineg']
                elif op == '!':
                    bytecode += ['ineg']
            elif isinstance(line, ThreeAC):
                bytecode += self.pushIfLocalOrConst(line.t2)
                bytecode += self.pushIfLocalOrConst(line.t3)
                op = line.op
                if op in GET_MNEMONIC_ARITH:
                    bytecode += [GET_MNEMONIC_ARITH[op]]
                elif op in GET_MNEMONIC_CMP:
                    elseLabel = LABEL_GENERATOR.nextLabel()
                    endLabel = LABEL_GENERATOR.nextLabel()
                    bytecode += ['{} {}'.format(GET_MNEMONIC_CMP[op], elseLabel)]
                    bytecode += ['iconst_1', 'goto {}'.format(endLabel)]
                    bytecode += self.label(elseLabel)
                    bytecode += ['iconst_0']
                    bytecode += self.label(endLabel)

            # save result or not
            bytecode += self.storeIfLocal(line.t1)
        return bytecode

    def makeReturn(self, _type):
        if _type == 'None':
            return ['return']
        if _type == 'Str' or isRecord(_type):
            return ['areturn']
        return ['ireturn']


def bodyGenerator(ast, gvt):
    statements = [s for s in ast.getFirstChild().getChildren() if s.name == 'statement']
    bc = []
    for s in statements:
        bc += StatementGenerator(s, gvt).generate()
    return bc