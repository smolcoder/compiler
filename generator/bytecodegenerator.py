from ast import NonTerminalASTNode
from generator.jasmin import JasminBaseGenerator, GET_MNEMONIC_CMP, GET_MNEMONIC_ARITH
from generator.linker import linkCode
from middlecode import *
from localvartable import LocalVariableTable
from utils import isRecord


class ByteCodeGenerator(JasminBaseGenerator):
    def __init__(self, ast, gvt):
        """
        Links middle code of given AST and compiles it to JVM mnemonic bytecode.
        See Jasmin tool and its syntax for more information.

        :type ast: NonTerminalASTNode
        :type gvt: LocalVariableTable
        """
        JasminBaseGenerator.__init__(self, ast)
        self.lvt = ast.getLVT()  # global variable table
        self.gvt = gvt
        self.gEnv = ast.getGlobalEnv()

    def generate(self):
        lc = linkCode(self.ast)
        bc = []
        for l in lc:
            bc += self.processLine(l)
        return bc

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
            return self.push_const(var.value, var.type)
        if var.status == 'loc':
            info = self.gvt.get(var.name)
            if info:
                return [self.getStaticField(info['name'], info['type'])]
            return [self.getLocalArg(var.name)]
        return []

    def storeIfVar(self, var):
        if var.status == 'loc':
            info = self.gvt.get(var.name)
            if info:
                return [self.putStaticField(info['name'], info['type'])]
            return [self.putLocalArg(var.name)]
        return []

    def processLine(self, line):
        bytecode = []
        if isinstance(line, CreateRecord):
            bytecode += ['invokespecial Main${}/<init>({})V'.format(
                line.name,
                ''.join([self.getType(t) for t in line.types])
            )]

        elif isinstance(line, NewRecord):
            bytecode += ['new Main${}'.format(line.name), 'dup']

        elif isinstance(line, CallFunction):
            info = self.gEnv.resolveFunction(line.name)
            retType = info['type']
            argTypes = [t for _, t in info['args']]
            bytecode += self.invokestatic(line.name, argTypes, retType)

        elif isinstance(line, PutField):
            bytecode += ['putfield Main${}/{} {}'.format(line.recordType, line.name, self.getType(line.fieldType))]

        elif isinstance(line, AccessRecordField):
            bytecode += self.pushIfLocalOrConst(line.t2)
            bytecode += ['getfield Main${}/{} {}'.format(line.t2.type, line.t3, self.getType(line.type))]

        elif isinstance(line, Push):
            bytecode += self.pushIfLocalOrConst(line.var)

        elif isinstance(line, IfEq):
            bytecode += self.pushIfLocalOrConst(line.var)
            bytecode += ['ifeq {}'.format(line.label)]
        elif isinstance(line, IfNe):
            bytecode += self.pushIfLocalOrConst(line.var)
            bytecode += ['ifne {}'.format(line.label)]

        elif isinstance(line, Label):
            bytecode += self.label(line.label)

        elif isinstance(line, PushBoolConst):
            bytecode += self.push_const('1' if line.f else '0', 'Bool')

        elif isinstance(line, GoTo):
            bytecode += ['goto {}'.format(line.label)]

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
            bytecode += self.push_const(str(line.size), 'Int')
            bytecode += ['anewarray java/lang/Object', 'dup']

        elif isinstance(line, Return):
            if line.type == 'None':
                bytecode += ['return']
            else:
                bytecode += self.pushIfLocalOrConst(line.var)
                if line.type == 'Str' or isRecord(line.type):
                    bytecode += ['areturn']
                bytecode += ['ireturn']

        elif isinstance(line, TestCondition):
            bytecode += self.pushIfLocalOrConst(line.var)
            bytecode += ['ifeq {}'.format(line.label)]

        elif isinstance(line, WriteLnCall):
            bytecode += ['invokestatic Main/writeln([Ljava/lang/Object;)V']

        elif isinstance(line, (TwoAC, TwoACOp, ThreeAC)):
            if isinstance(line, TwoAC):
                bytecode += self.pushIfLocalOrConst(line.t2)
            elif isinstance(line, TwoACOp):
                op = line.op
                bytecode += self.pushIfLocalOrConst(line.t2)
                if op == '-':
                    bytecode += ['ineg']
                elif op == '!':
                    bytecode += self.notOperation()
            elif isinstance(line, ThreeAC):
                bytecode += self.pushIfLocalOrConst(line.t2)
                bytecode += self.pushIfLocalOrConst(line.t3)
                op = line.op
                if op in GET_MNEMONIC_ARITH:
                    bytecode += [GET_MNEMONIC_ARITH[op]]
                elif op in GET_MNEMONIC_CMP:
                    if op in ['==', '!='] and line.t2.type == 'Str' and line.t3.type == 'Str':
                        bytecode += ['invokevirtual java/lang/String/equals(Ljava/lang/Object;)Z']
                        if op == '!=':
                            bytecode += self.notOperation()
                    else:
                        elseLabel = LABEL_GENERATOR.nextLabel()
                        endLabel = LABEL_GENERATOR.nextLabel()
                        bytecode += ['{} {}'.format(GET_MNEMONIC_CMP[op], elseLabel)]
                        bytecode += ['iconst_0', 'goto {}'.format(endLabel)]
                        bytecode += self.label(elseLabel)
                        bytecode += ['iconst_1']
                        bytecode += self.label(endLabel)

            # save result or not
            bytecode += self.storeIfVar(line.t1)
        return bytecode

    def notOperation(self):
        bytecode = []
        notLabel1 = LABEL_GENERATOR.nextLabel()
        notLabel2 = LABEL_GENERATOR.nextLabel()
        bytecode += ['ifne {}'.format(notLabel1)]
        bytecode += ['iconst_1']
        bytecode += ['goto {}'.format(notLabel2)]
        bytecode += self.label(notLabel1)
        bytecode += ['iconst_0']
        bytecode += self.label(notLabel2)
        return bytecode