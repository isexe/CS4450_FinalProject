# Generated from Project.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ProjectParser import ProjectParser
else:
    from ProjectParser import ProjectParser

# This class defines a complete generic visitor for a parse tree produced by ProjectParser.

class ProjectVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ProjectParser#expression.
    def visitExpression(self, ctx:ProjectParser.ExpressionContext):
        return self.visitChildren(ctx)



del ProjectParser