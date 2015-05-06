from generator import makeTAD, linkCode
from generator.jasmin import JasminBase
from localvartable import LocalVariableTable
from middlecode import *


class ClinitGenerator(JasminBase):
    def __init__(self, ast):
        """
        :param ast: Root ast
        """
        self.gvt = ast.lvt  # global variable table
        self.ast = ast
        self.env = ast.env
        self.bytecode = []
        self.compiler = MiddleCodeCompiler(self.env)

    def generate(self):
        for v in self.env.varOrder:
            if self.gvt.get(v)['ast'].getLastChild().name != 'expression':
                continue
            self.processVarDec(self.gvt.get(v))

    def processVarDec(self, varDec):
        print 40 * '.', varDec['name']
        lc = linkCode(varDec['ast'])
        # print '\n'.join(map(str, lc))
        bc = self.compiler.compile(lc)
        print '\n'.join(map(str, bc))
        self.bytecode += bc

GET_MNEMONIC = {
    '+': 'iadd',
    '-': 'isub',
    '*': 'imul',
    '/': 'idiv',
    '%': 'irem',
}


class MiddleCodeCompiler(JasminBase):
    def __init__(self, gEnv):
        self.gEnv = gEnv

    def getStaticField(self, name, _type):
        return 'getstatic Main/{} {}'.format(name, self.getType(_type))

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
            fEnv = self.gEnv.resolveFunction(line.name)
            _type = ''.join([self.getType(t) for n, t in fEnv['args']])
            rType = self.getType(fEnv['type'])
            bytecode += ['invokestatic Main/{}({}){}'.format(line.name, _type, rType)]
        elif isinstance(line, (TwoAC, TwoACOp, ThreeAC)):
            if isinstance(line, TwoAC):
                if isinstance(line.t2, Const):
                    bytecode += self.push_const(line.t2.value)
                elif isinstance(line.t2, Variable) and line.t2.status == 'loc':
                    bytecode += [self.getStaticField(line.t2.name, line.t2.type)]
            elif isinstance(line, TwoACOp):
                op = line.op
                if line.t2.status == 'loc':
                    bytecode += [self.getStaticField(line.t2.name, line.t2.type)]
                if op == '-':
                    bytecode += ['ineg']
                elif op == '!':
                    bytecode += ['ineg']
            elif isinstance(line, ThreeAC):
                if line.t2.status == 'loc':
                    bytecode += [self.getStaticField(line.t2.name, line.t2.type)]
                if line.t3.status == 'loc':
                    bytecode += [self.getStaticField(line.t3.name, line.t3.type)]
                op = line.op
                bytecode += [GET_MNEMONIC[op]]

            # save result or not
            if line.t1.status == 'loc':
                bytecode += ['putstatic Main/{} {}'.format(line.t1.name, self.getType(line.type))]
        return bytecode

    def compile(self, code):
        bc = []
        for l in code:
            bc += self.processLine(l)
        return bc
