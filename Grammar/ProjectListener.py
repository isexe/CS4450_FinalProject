# Generated from Project.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ProjectParser import ProjectParser
else:
    from ProjectParser import ProjectParser

# This class defines a complete listener for a parse tree produced by ProjectParser.
class ProjectListener(ParseTreeListener):

    # Enter a parse tree produced by ProjectParser#expression.
    def enterExpression(self, ctx:ProjectParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ProjectParser#expression.
    def exitExpression(self, ctx:ProjectParser.ExpressionContext):
        pass



del ProjectParser