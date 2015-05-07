from generator.classfilegenerator import ClassFileGenerator
from generator.record import RecordGenerator
from utils import java
from utils import jasmin
from utils import here


def runProgramme(ast, filename, classname, jasFilePath=None, out=None):
    cg = ClassFileGenerator(classname, ast, filename)
    jasFilePath = jasFilePath or here('sources', 'jas')
    out = out or here('out/')
    cg.generateToFile(jasFilePath)
    jasmin(here(jasFilePath, '{}.j'.format(classname)), out=out)

    for r in ast.env.records:
        rcg = RecordGenerator(r, ast.env.resolveRecord(r)['ast'], filename)
        rcg.generateToFile(jasFilePath)
        jasmin(here('sources', 'jas', '{}.j'.format(r)), out=out)

    return java(classname, classpath=out)