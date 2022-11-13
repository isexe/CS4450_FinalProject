# Generated from Project.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ProjectParser import ProjectParser
else:
    from ProjectParser import ProjectParser

# This class defines a complete listener for a parse tree produced by ProjectParser.
class ProjectListener(ParseTreeListener):

    # Enter a parse tree produced by ProjectParser#code.
    def enterCode(self, ctx:ProjectParser.CodeContext):
        pass

    # Exit a parse tree produced by ProjectParser#code.
    def exitCode(self, ctx:ProjectParser.CodeContext):
        pass


    # Enter a parse tree produced by ProjectParser#lines.
    def enterLines(self, ctx:ProjectParser.LinesContext):
        pass

    # Exit a parse tree produced by ProjectParser#lines.
    def exitLines(self, ctx:ProjectParser.LinesContext):
        pass


    # Enter a parse tree produced by ProjectParser#statement.
    def enterStatement(self, ctx:ProjectParser.StatementContext):
        pass

    # Exit a parse tree produced by ProjectParser#statement.
    def exitStatement(self, ctx:ProjectParser.StatementContext):
        pass


    # Enter a parse tree produced by ProjectParser#assignment.
    def enterAssignment(self, ctx:ProjectParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ProjectParser#assignment.
    def exitAssignment(self, ctx:ProjectParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ProjectParser#addition_assignment.
    def enterAddition_assignment(self, ctx:ProjectParser.Addition_assignmentContext):
        pass

    # Exit a parse tree produced by ProjectParser#addition_assignment.
    def exitAddition_assignment(self, ctx:ProjectParser.Addition_assignmentContext):
        pass


    # Enter a parse tree produced by ProjectParser#subtraction_assignment.
    def enterSubtraction_assignment(self, ctx:ProjectParser.Subtraction_assignmentContext):
        pass

    # Exit a parse tree produced by ProjectParser#subtraction_assignment.
    def exitSubtraction_assignment(self, ctx:ProjectParser.Subtraction_assignmentContext):
        pass


    # Enter a parse tree produced by ProjectParser#multiplication_assignment.
    def enterMultiplication_assignment(self, ctx:ProjectParser.Multiplication_assignmentContext):
        pass

    # Exit a parse tree produced by ProjectParser#multiplication_assignment.
    def exitMultiplication_assignment(self, ctx:ProjectParser.Multiplication_assignmentContext):
        pass


    # Enter a parse tree produced by ProjectParser#division_assignment.
    def enterDivision_assignment(self, ctx:ProjectParser.Division_assignmentContext):
        pass

    # Exit a parse tree produced by ProjectParser#division_assignment.
    def exitDivision_assignment(self, ctx:ProjectParser.Division_assignmentContext):
        pass


    # Enter a parse tree produced by ProjectParser#id.
    def enterId(self, ctx:ProjectParser.IdContext):
        pass

    # Exit a parse tree produced by ProjectParser#id.
    def exitId(self, ctx:ProjectParser.IdContext):
        pass


    # Enter a parse tree produced by ProjectParser#eq.
    def enterEq(self, ctx:ProjectParser.EqContext):
        pass

    # Exit a parse tree produced by ProjectParser#eq.
    def exitEq(self, ctx:ProjectParser.EqContext):
        pass


    # Enter a parse tree produced by ProjectParser#eq_add.
    def enterEq_add(self, ctx:ProjectParser.Eq_addContext):
        pass

    # Exit a parse tree produced by ProjectParser#eq_add.
    def exitEq_add(self, ctx:ProjectParser.Eq_addContext):
        pass


    # Enter a parse tree produced by ProjectParser#eq_sub.
    def enterEq_sub(self, ctx:ProjectParser.Eq_subContext):
        pass

    # Exit a parse tree produced by ProjectParser#eq_sub.
    def exitEq_sub(self, ctx:ProjectParser.Eq_subContext):
        pass


    # Enter a parse tree produced by ProjectParser#eq_mult.
    def enterEq_mult(self, ctx:ProjectParser.Eq_multContext):
        pass

    # Exit a parse tree produced by ProjectParser#eq_mult.
    def exitEq_mult(self, ctx:ProjectParser.Eq_multContext):
        pass


    # Enter a parse tree produced by ProjectParser#eq_div.
    def enterEq_div(self, ctx:ProjectParser.Eq_divContext):
        pass

    # Exit a parse tree produced by ProjectParser#eq_div.
    def exitEq_div(self, ctx:ProjectParser.Eq_divContext):
        pass


    # Enter a parse tree produced by ProjectParser#equation.
    def enterEquation(self, ctx:ProjectParser.EquationContext):
        pass

    # Exit a parse tree produced by ProjectParser#equation.
    def exitEquation(self, ctx:ProjectParser.EquationContext):
        pass


    # Enter a parse tree produced by ProjectParser#factor.
    def enterFactor(self, ctx:ProjectParser.FactorContext):
        pass

    # Exit a parse tree produced by ProjectParser#factor.
    def exitFactor(self, ctx:ProjectParser.FactorContext):
        pass


    # Enter a parse tree produced by ProjectParser#exponent.
    def enterExponent(self, ctx:ProjectParser.ExponentContext):
        pass

    # Exit a parse tree produced by ProjectParser#exponent.
    def exitExponent(self, ctx:ProjectParser.ExponentContext):
        pass


    # Enter a parse tree produced by ProjectParser#val.
    def enterVal(self, ctx:ProjectParser.ValContext):
        pass

    # Exit a parse tree produced by ProjectParser#val.
    def exitVal(self, ctx:ProjectParser.ValContext):
        pass


    # Enter a parse tree produced by ProjectParser#expon.
    def enterExpon(self, ctx:ProjectParser.ExponContext):
        pass

    # Exit a parse tree produced by ProjectParser#expon.
    def exitExpon(self, ctx:ProjectParser.ExponContext):
        pass


    # Enter a parse tree produced by ProjectParser#mult.
    def enterMult(self, ctx:ProjectParser.MultContext):
        pass

    # Exit a parse tree produced by ProjectParser#mult.
    def exitMult(self, ctx:ProjectParser.MultContext):
        pass


    # Enter a parse tree produced by ProjectParser#div.
    def enterDiv(self, ctx:ProjectParser.DivContext):
        pass

    # Exit a parse tree produced by ProjectParser#div.
    def exitDiv(self, ctx:ProjectParser.DivContext):
        pass


    # Enter a parse tree produced by ProjectParser#mod.
    def enterMod(self, ctx:ProjectParser.ModContext):
        pass

    # Exit a parse tree produced by ProjectParser#mod.
    def exitMod(self, ctx:ProjectParser.ModContext):
        pass


    # Enter a parse tree produced by ProjectParser#add.
    def enterAdd(self, ctx:ProjectParser.AddContext):
        pass

    # Exit a parse tree produced by ProjectParser#add.
    def exitAdd(self, ctx:ProjectParser.AddContext):
        pass


    # Enter a parse tree produced by ProjectParser#sub.
    def enterSub(self, ctx:ProjectParser.SubContext):
        pass

    # Exit a parse tree produced by ProjectParser#sub.
    def exitSub(self, ctx:ProjectParser.SubContext):
        pass


    # Enter a parse tree produced by ProjectParser#expression.
    def enterExpression(self, ctx:ProjectParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ProjectParser#expression.
    def exitExpression(self, ctx:ProjectParser.ExpressionContext):
        pass



del ProjectParser