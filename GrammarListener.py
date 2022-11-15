from antlr4 import *
from Grammar.ProjectLexer import ProjectLexer
from Grammar.ProjectParser import ProjectParser
from Grammar.ProjectListener import ProjectListener

class GrammarListener(ProjectListener):
    pass
    # def enterExpression(self, ctx: ProjectParser.ExpressionContext):
    #     print("Enter Expression: " + ctx.getText())
    #     return

    # def exitExpression(self, ctx: ProjectParser.ExpressionContext):
    #     print("Exit Expression: " + ctx.getText())
    #     return
        
    # def visitTerminal(self, node: TerminalNode):
    #     print("Visit Terminal: " + str(node))
    #     return