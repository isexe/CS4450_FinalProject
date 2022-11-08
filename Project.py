import sys
from antlr4 import *
from out.ProjectLexer import ProjectLexer
from out.ProjectParser import ProjectParser
from out.ProjectListener import ProjectListener

class HelloPrintListener(ProjectListener):
    def enterHi(self, ctx):
        print("Hello: %s" % ctx.ID())

def main():
    lexer = ProjectLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = ProjectParser(stream)
    
    tree = parser.hi()
    
    printer = HelloPrintListener()
    walker = ParseTreeWalker()

    walker.walk(printer, tree)

if __name__ == '__main__':
    main()