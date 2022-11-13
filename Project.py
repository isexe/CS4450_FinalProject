import sys
from antlr4 import *
from Grammar.ProjectLexer import ProjectLexer
from Grammar.ProjectParser import ProjectParser
from GrammarListener import GrammarListener
from GrammarVisitor import GrammarVisitor

# *Resource for tree visualization - not image so not useful
# https://treelib.readthedocs.io/en/latest/
# from treelib import Node, Tree

# *Resource for understanding Listener VS Visitor
# https://tomassetti.me/listeners-and-visitors/
#* Resouce for general help
# https://tomassetti.me/antlr-mega-tutorial/#chapter11

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
    result = GrammarVisitor().visitCode(tree)
    
    print("\n--- String Parse Tree ---")
    print(tree.toStringTree())

    # currently using Visitor as I found that was easier to work with
    # # Use listener to traverse parse tree
    # # mainly used for debugging currently
    # print("\n--- Listener ---")
    # listener = GrammarListener()
    # walker = ParseTreeWalker()
    # walker.walk(listener, tree)

if __name__ == '__main__':
    main()