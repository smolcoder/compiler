# Generated from java-escape by ANTLR 4.5
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by LLangParser.

class LLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LLangParser#programme.
    def visitProgramme(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#recordDeclaration.
    def visitRecordDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#recordBody.
    def visitRecordBody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#functionSignature.
    def visitFunctionSignature(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#functionReturnType.
    def visitFunctionReturnType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#functionBody.
    def visitFunctionBody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#functionParameterList.
    def visitFunctionParameterList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#functionParameter.
    def visitFunctionParameter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#variableDeclarationStatement.
    def visitVariableDeclarationStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#recordInitializer.
    def visitRecordInitializer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#recordFieldInitializerList.
    def visitRecordFieldInitializerList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#recordFieldInitializer.
    def visitRecordFieldInitializer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#cortegeInitializer.
    def visitCortegeInitializer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#expressionList.
    def visitExpressionList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#passStatement.
    def visitPassStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#exprType.
    def visitExprType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#primitiveType.
    def visitPrimitiveType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#recordId.
    def visitRecordId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#intType.
    def visitIntType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#strType.
    def visitStrType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#boolType.
    def visitBoolType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#voidType.
    def visitVoidType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#cortegeType.
    def visitCortegeType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#cortegeTypeUnit.
    def visitCortegeTypeUnit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#cortegeTypeNonEmptyList.
    def visitCortegeTypeNonEmptyList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#block.
    def visitBlock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#justBlock.
    def visitJustBlock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#statement.
    def visitStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#breakStatement.
    def visitBreakStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#breaks.
    def visitBreaks(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#continueStatement.
    def visitContinueStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#continues.
    def visitContinues(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#returnStatement.
    def visitReturnStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#returnExpr.
    def visitReturnExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#whileStatement.
    def visitWhileStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#forStatement.
    def visitForStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#forInit.
    def visitForInit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#forCondition.
    def visitForCondition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#forUpdate.
    def visitForUpdate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#ifStatement.
    def visitIfStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#elifBlock.
    def visitElifBlock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#elseBlock.
    def visitElseBlock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#writelnStatement.
    def visitWritelnStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#writelnCall.
    def visitWritelnCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#readlnStatement.
    def visitReadlnStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#readIntCall.
    def visitReadIntCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#readStrCall.
    def visitReadStrCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#readBoolCall.
    def visitReadBoolCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#functionInvocationStatement.
    def visitFunctionInvocationStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#functionInvocation.
    def visitFunctionInvocation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#argumentList.
    def visitArgumentList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#expression.
    def visitExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#assignment.
    def visitAssignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#leftHandSide.
    def visitLeftHandSide(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#cortegeAccess.
    def visitCortegeAccess(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#recordFieldAccess.
    def visitRecordFieldAccess(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#literal.
    def visitLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#intLiteral.
    def visitIntLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#strLiteral.
    def visitStrLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#boolLiteral.
    def visitBoolLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#unaryOperator.
    def visitUnaryOperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#mulDivModOperator.
    def visitMulDivModOperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#addSubOperator.
    def visitAddSubOperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#compareOperator.
    def visitCompareOperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#equalOrNotOperator.
    def visitEqualOrNotOperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#boolOperator.
    def visitBoolOperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LLangParser#identifier.
    def visitIdentifier(self, ctx):
        return self.visitChildren(ctx)


