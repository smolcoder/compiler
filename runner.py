from generator.classfilegenerator import ClassFileGenerator
from generator.record import RecordGenerator
from utils import java
from utils import jasmin
from utils import here


def runProgramme(ast, filename, classname):
    cg = ClassFileGenerator(classname, ast, filename)
    jas = here('sources', 'jas')
    cg.generateToFile(jas)
    jasmin(here('sources', 'jas', '{}.j'.format(classname)))

    for r in ast.env.records:
        rcg = RecordGenerator(r, ast.env.resolveRecord(r)['ast'], filename)
        rcg.generateToFile(jas)
        jasmin(here('sources', 'jas', '{}.j'.format(r)))

    java(classname)