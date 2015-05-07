from generator.jasmin import JasminBaseGenerator, GET_MNEMONIC_CMP, GET_MNEMONIC_ARITH
from generator.linker import linkCode
from middlecode import *


class ClinitGenerator(JasminBaseGenerator):
    def __init__(self, ast):
        """
        :param ast: Root ast
        """
        JasminBaseGenerator.__init__(self, ast)
        self.gvt = ast.lvt  # global variable table
        self.env = ast.env

    def generate(self):
        bytecode = ['.method static <clinit>()V'] + self.limits()
        for v in self.env.varOrder:
            if self.gvt.get(v)['ast'].getLastChild().name != 'expression':
                continue
            bytecode += self.processVarDec(self.gvt.get(v))
        bytecode += ['return', '.end method']
        return bytecode

    def processVarDec(self, varDec):
        lc = linkCode(varDec['ast'])
        bc = ['; line {}'.format(varDec['ast'].source.line)]
        for l in lc:
            bc += self.processLine(l)
        return bc

    def getStaticField(self, name, _type):
        return 'getstatic Main/{} {}'.format(name, self.getType(_type))

    def putStaticField(self, name, _type):
        return 'putstatic Main/{} {}'.format(name, self.getType(_type))

    def pushIfLocalOrConst(self, var):
        if isinstance(var, Const):
            return self.push_const(var.value)
        if var.status == 'loc':
            return [self.getStaticField(var.name, var.type)]
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
            fEnv = self.env.resolveFunction(line.name)
            _type = ''.join([self.getType(t) for n, t in fEnv['args']])
            rType = self.getType(fEnv['type'])
            bytecode += ['invokestatic Main/{}({}){}'.format(line.name, _type, rType)]
        elif isinstance(line, AccessRecordField):
            if line.t2.status == 'loc':
                bytecode += [self.getStaticField(line.t2.name, line.t2.type)]
            bytecode += ['getfield Main${}/{} {}'.format(line.t2.type, line.t3, self.getType(line.type))]
        elif isinstance(line, Push):
            bytecode += self.pushIfLocalOrConst(line.var)
        elif isinstance(line, IfNeEq):
            bytecode += self.pushIfLocalOrConst(line.var)
            bytecode += ['if{} {}'.format('ne' if line.op == '!=' else 'eq', line.label)]
        elif isinstance(line, Label):
            bytecode += self.label(line.label)
        elif isinstance(line, PushBoolConst):
            bytecode += self.push_const('1' if line.f else '0')
        elif isinstance(line, GoTo):
            bytecode += ['goto {}'.format(line.label)]
        elif isinstance(line, (TwoAC, TwoACOp, ThreeAC)):
            if isinstance(line, TwoAC):
                if isinstance(line.t2, Const):
                    bytecode += self.push_const(line.t2.value)
                elif isinstance(line.t2, Variable):
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
            if line.t1.status == 'loc':
                bytecode += [self.putStaticField(line.t1.name, line.type)]
        return bytecode