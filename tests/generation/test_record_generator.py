from generator.record import RecordGenerator
import shutil
from tests import BaseTestCase
from utils import jasmin, java, here
from os.path import realpath
import os


class RecordGeneratorTestCase(BaseTestCase):
    pathToOut = here('test_out')
    classpath = ':'.join([realpath(x) for x in [here('test_out'),
                                                here('tests', 'source', 'java')]])
    pathToJar = here('lib')

    def generate(self, name, globalEnv):
        ast = globalEnv.resolveRecord(name)['ast']
        rg = RecordGenerator(name, ast)
        rg.generateToFile(self.pathToOut)

    def test_t(self):
        res = self.compile("""record R1 {
                               Int i;
                               Str s;
                               Bool b;
                           }

                           record R2 {
                               Int i;
                               R1 r1;
                           }""")
        os.mkdir(self.pathToOut)
        try:
            self.generate('R1', res.globalEnv)
            self.generate('R2', res.globalEnv)
            jasmin(here(self.pathToOut, 'R1.j'), self.pathToJar, self.pathToOut)
            jasmin(here(self.pathToOut, 'R2.j'), self.pathToJar, self.pathToOut)
            res = java('Main', self.classpath)
            self.assertFalse(res)
        finally:
            shutil.rmtree(self.pathToOut)
