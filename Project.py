import sys
from antlr4 import *
from Grammer.ProjectLexer import ProjectLexer
from Grammer.ProjectParser import ProjectParser
from Grammer.ProjectListener import ProjectListener

class HelloPrintListener(ProjectListener):
    def enterHi(self, ctx):
        print("Hello: %s" % ctx.ID())

def main():
    input = StdinStream()

    lexer = ProjectLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ProjectParser(stream)
    
    tree = parser.hi()
    
    printer = HelloPrintListener()
    walker = ParseTreeWalker()

    walker.walk(printer, tree)

if __name__ == '__main__':
    main()