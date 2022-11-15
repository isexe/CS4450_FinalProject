from antlr4 import *
from Grammar.ProjectLexer import ProjectLexer
from Grammar.ProjectParser import ProjectParser
from Grammar.ProjectVisitor import ProjectVisitor

from Visitors.EquationVisitor import EquationVisitor

class GrammarVisitor(ProjectVisitor):
    def __init__(self, debugging = False):
        self.debugging = debugging
    
    # Visit a parse tree produced by ProjectParser#code.
    # Next Node is Lines
    def visitCode(self, ctx:ProjectParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#lines.
    # Next Node is Statement
    def visitLines(self, ctx:ProjectParser.LinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjectParser#statement.
    # Will direct to visit parse rule
    # i.e. 1 + 1 will go to visitEquation next
    def visitStatement(self, ctx:ProjectParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#equation.
    def visitEquation(self, ctx:ProjectParser.EquationContext):
        result = EquationVisitor().visitEquation(ctx)

        # used to debug
        if(self.debugging):
            print("Equation:\n" + ctx.getText() + " = " + str(result))

        return result
