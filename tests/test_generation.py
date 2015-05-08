import os
import shutil
from runner import runProgramme
from tests import BaseTestCase
from utils import here


class ClinitGeneratorTestCase(BaseTestCase):
    pathToOut = here('test_out')
    classpath = pathToOut
    pathToJar = here('lib')

    def test_clinit(self):
        os.mkdir(self.pathToOut)
        try:
            res = self.compileFile(here('tests', 'source', 'classInit.llang'))
            self.assertFalse(res.errors)
            self.assertEqual(runProgramme(res.ast, 'Main', 'Main',
                                          jasFilePath=self.pathToOut,
                                          out=self.pathToOut), 0)

        finally:
            shutil.rmtree(self.pathToOut)

    def test_big(self):
        os.mkdir(self.pathToOut)
        try:
            res = self.compileFile(here('tests', 'source', 'big.llang'))
            self.assertFalse(res.errors)
            self.assertEqual(runProgramme(res.ast, 'Main', 'Main',
                                          jasFilePath=self.pathToOut,
                                          out=self.pathToOut), 0)

        finally:
            shutil.rmtree(self.pathToOut)