import sys
from antlr4 import *
from Grammar.ProjectLexer import ProjectLexer
from Grammar.ProjectParser import ProjectParser
from Grammar.ProjectListener import ProjectListener
from Grammar.ProjectVisitor import ProjectVisitor

# *Resource for understanding Listener VS Visitor
# https://tomassetti.me/listeners-and-visitors/
#* Resouce for general help
# https://tomassetti.me/antlr-mega-tutorial/#chapter11

class GrammarListener(ProjectListener):
    def enterExpression(self, ctx: ProjectParser.ExpressionContext):
        print("Enter Expression: " + ctx.getText())

    def exitExpression(self, ctx: ProjectParser.ExpressionContext):
        print("Exit Expression: " + ctx.getText())
        
    def visitTerminal(self, node: TerminalNode):
        print("Visit Terminal: " + str(node))

class GrammarVisitor(ProjectVisitor):
    def visitExpression(self, ctx: ProjectParser.ExpressionContext):
        pass

def main():
    # command-line formatting
    print("pȳthon 0.0.1")
    print("Type Ctrl+D to run, Ctrl+Z to exit")
    usr_input = StdinStream()
    
    # parse input
    # ordering is lexer -> stream -> parser
    lexer = ProjectLexer(usr_input)
    stream = CommonTokenStream(lexer)
    parser = ProjectParser(stream)
    # pretty sure is redundant but better save than sorry
    parser.buildParseTrees = True
    
    # Get tree from parser
    tree = parser.expression()

    # Use listener to traverse parse tree
    listener = GrammarListener()
    walker = ParseTreeWalker()
    print("\n--- Traversing Tree ---")
    walker.walk(listener, tree)

    print("\n--- OUTPUT ---")
    print(tree.toStringTree())
    print(tree.getText())

if __name__ == '__main__':
    main()