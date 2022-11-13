# Generated from Project.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ProjectParser import ProjectParser
else:
    from ProjectParser import ProjectParser

# This class defines a complete generic visitor for a parse tree produced by ProjectParser.

class ProjectVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ProjectParser#code.
    def visitCode(self, ctx:ProjectParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#lines.
    def visitLines(self, ctx:ProjectParser.LinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#statement.
    def visitStatement(self, ctx:ProjectParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#assignment.
    def visitAssignment(self, ctx:ProjectParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#addition_assignment.
    def visitAddition_assignment(self, ctx:ProjectParser.Addition_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#subtraction_assignment.
    def visitSubtraction_assignment(self, ctx:ProjectParser.Subtraction_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#multiplication_assignment.
    def visitMultiplication_assignment(self, ctx:ProjectParser.Multiplication_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#division_assignment.
    def visitDivision_assignment(self, ctx:ProjectParser.Division_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#id.
    def visitId(self, ctx:ProjectParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#eq.
    def visitEq(self, ctx:ProjectParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#eq_add.
    def visitEq_add(self, ctx:ProjectParser.Eq_addContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#eq_sub.
    def visitEq_sub(self, ctx:ProjectParser.Eq_subContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#eq_mult.
    def visitEq_mult(self, ctx:ProjectParser.Eq_multContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#eq_div.
    def visitEq_div(self, ctx:ProjectParser.Eq_divContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#equation.
    def visitEquation(self, ctx:ProjectParser.EquationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#factor.
    def visitFactor(self, ctx:ProjectParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#exponent.
    def visitExponent(self, ctx:ProjectParser.ExponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#val.
    def visitVal(self, ctx:ProjectParser.ValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#expon.
    def visitExpon(self, ctx:ProjectParser.ExponContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#mult.
    def visitMult(self, ctx:ProjectParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#div.
    def visitDiv(self, ctx:ProjectParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#mod.
    def visitMod(self, ctx:ProjectParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#add.
    def visitAdd(self, ctx:ProjectParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#sub.
    def visitSub(self, ctx:ProjectParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#expression.
    def visitExpression(self, ctx:ProjectParser.ExpressionContext):
        return self.visitChildren(ctx)



del ProjectParser