# Generated from Project.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("V\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\3\n\5\n\61\n\n\3\13\5\13\64\n")
        buf.write("\13\3\13\6\13\67\n\13\r\13\16\138\3\13\3\13\7\13=\n\13")
        buf.write("\f\13\16\13@\13\13\5\13B\n\13\3\f\6\fE\n\f\r\f\16\fF\3")
        buf.write("\r\3\r\7\rK\n\r\f\r\16\rN\13\r\3\16\6\16Q\n\16\r\16\16")
        buf.write("\16R\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\3\2\b\4\2--//\3\2\62;\5")
        buf.write("\2\62;C\\c|\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"")
        buf.write("\"\2]\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\3\35\3\2\2\2\5\37\3\2\2\2\7!\3\2\2\2\t$\3\2\2")
        buf.write("\2\13&\3\2\2\2\r(\3\2\2\2\17*\3\2\2\2\21,\3\2\2\2\23\60")
        buf.write("\3\2\2\2\25\63\3\2\2\2\27D\3\2\2\2\31H\3\2\2\2\33P\3\2")
        buf.write("\2\2\35\36\7*\2\2\36\4\3\2\2\2\37 \7+\2\2 \6\3\2\2\2!")
        buf.write("\"\7,\2\2\"#\7,\2\2#\b\3\2\2\2$%\7,\2\2%\n\3\2\2\2&\'")
        buf.write("\7\61\2\2\'\f\3\2\2\2()\7\'\2\2)\16\3\2\2\2*+\7-\2\2+")
        buf.write("\20\3\2\2\2,-\7/\2\2-\22\3\2\2\2.\61\5\25\13\2/\61\5\27")
        buf.write("\f\2\60.\3\2\2\2\60/\3\2\2\2\61\24\3\2\2\2\62\64\t\2\2")
        buf.write("\2\63\62\3\2\2\2\63\64\3\2\2\2\64\66\3\2\2\2\65\67\t\3")
        buf.write("\2\2\66\65\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2\29")
        buf.write("A\3\2\2\2:>\7\60\2\2;=\t\3\2\2<;\3\2\2\2=@\3\2\2\2><\3")
        buf.write("\2\2\2>?\3\2\2\2?B\3\2\2\2@>\3\2\2\2A:\3\2\2\2AB\3\2\2")
        buf.write("\2B\26\3\2\2\2CE\t\4\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2")
        buf.write("FG\3\2\2\2G\30\3\2\2\2HL\t\5\2\2IK\t\6\2\2JI\3\2\2\2K")
        buf.write("N\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M\32\3\2\2\2NL\3\2\2\2OQ")
        buf.write("\t\7\2\2PO\3\2\2\2QR\3\2\2\2RP\3\2\2\2RS\3\2\2\2ST\3\2")
        buf.write("\2\2TU\b\16\2\2U\34\3\2\2\2\f\2\60\638>ADFLR\3\b\2\2")
        return buf.getvalue()


class ProjectLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    EXPON = 3
    MULT = 4
    DIV = 5
    MOD = 6
    ADD = 7
    SUB = 8
    ATOM = 9
    NUM = 10
    CHAR = 11
    VAR = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'**'", "'*'", "'/'", "'%'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "EXPON", "MULT", "DIV", "MOD", "ADD", "SUB", "ATOM", "NUM", 
            "CHAR", "VAR", "WS" ]

    ruleNames = [ "T__0", "T__1", "EXPON", "MULT", "DIV", "MOD", "ADD", 
                  "SUB", "ATOM", "NUM", "CHAR", "VAR", "WS" ]

    grammarFileName = "Project.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


