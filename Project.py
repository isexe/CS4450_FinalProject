import sys
from antlr4 import *
from Grammer.ProjectLexer import ProjectLexer
from Grammer.ProjectParser import ProjectParser
from Grammer.ProjectListener import ProjectListener
from Grammer.ProjectVisitor import ProjectVisitor

# *Resource for understanding Listener VS Visitor
# https://tomassetti.me/listeners-and-visitors/
class GrammarListener(ProjectListener):
    def enterExpression(self, ctx: ProjectParser.ExpressionContext):
        print("Enter Expression: " + ctx.getText())

    def exitExpression(self, ctx: ProjectParser.ExpressionContext):
        print("Exit Expression: " + ctx.getText())

    def visitTerminal(self, node: TerminalNode):
        print("Visit Terminal: " + str(node))

class GrammarVisitor(ProjectVisitor):
    def visitExpression(self, ctx: ProjectParser.ExpressionContext):
        print("Visit Expression: " + ctx.getText())

def main():
    # command-line formatting
    print("pȳthon 0.0.1")
    print("Type Ctrl+D to run, Ctrl+Z to exit")
    usr_input = StdinStream('utf-8')
    
    # actual useful stuff
    lexer = ProjectLexer(usr_input)
    stream = CommonTokenStream(lexer)
    parser = ProjectParser(stream)
    parser.buildParseTrees = True
    
    tree = parser.expression()
    listener = GrammarListener()

    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    print(tree.toStringTree())
    print(tree.getText())

if __name__ == '__main__':
    main()