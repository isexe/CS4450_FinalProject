import sys
from antlr4 import *
from Grammer.ProjectLexer import ProjectLexer
from Grammer.ProjectParser import ProjectParser
from Grammer.ProjectListener import ProjectListener

class HelloPrintListener(ProjectListener):
    def enterHi(self, ctx):
        print("Hello: %s" % ctx.ID())

def main():
    # command-line formatting
    print("pȳthon 0.0.1")
    print("Type Ctrl+D to run, Ctrl+Z to exit")
    usr_input = StdinStream(input('>>> '))

    # actual useful stuff
    lexer = ProjectLexer(usr_input)
    stream = CommonTokenStream(lexer)
    parser = ProjectParser(stream)
    
    tree = parser.hi()
    
    printer = HelloPrintListener()
    walker = ParseTreeWalker()

    walker.walk(printer, tree)

if __name__ == '__main__':
    main()