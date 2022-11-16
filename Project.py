import sys
from antlr4 import *
from Grammar.ProjectLexer import ProjectLexer
from Grammar.ProjectParser import ProjectParser

# information on antlr visitor found at resource #2
from GrammarVisitor import GrammarVisitor

def main():
    # command-line formatting
    print("pȳthon 0.0.1")
    print("Type Ctrl+D to run, Ctrl+Z to exit")
    usr_input = StdinStream()
    
    # parse input
    # ordering is lexer -> token stream -> parser
    lexer = ProjectLexer(usr_input)
    stream = CommonTokenStream(lexer)
    parser = ProjectParser(stream)
    # pretty sure is redundant but better save than sorry
    parser.buildParseTrees = True

    # parse and get tree
    tree = parser.code()
    
    # use visitor to traverse parse tree
    result = GrammarVisitor(debugging=True).visitCode(tree)
    
    print("\n--- String Parse Tree ---")
    print(tree.toStringTree())

if __name__ == '__main__':
    main()