# Generated from Project.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("P\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\6\16?\n\16\r\16")
        buf.write("\16\16@\3\17\3\17\7\17E\n\17\f\17\16\17H\13\17\3\20\6")
        buf.write("\20K\n\20\r\20\16\20L\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21\3\2\6\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\5\2\13")
        buf.write("\f\17\17\"\"\2R\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2\2")
        buf.write("\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2\2\2\13)\3\2\2\2\r+\3")
        buf.write("\2\2\2\17-\3\2\2\2\21/\3\2\2\2\23\61\3\2\2\2\25\64\3\2")
        buf.write("\2\2\27\67\3\2\2\2\31:\3\2\2\2\33>\3\2\2\2\35B\3\2\2\2")
        buf.write("\37J\3\2\2\2!\"\7*\2\2\"\4\3\2\2\2#$\7+\2\2$\6\3\2\2\2")
        buf.write("%&\7,\2\2&\b\3\2\2\2\'(\7\61\2\2(\n\3\2\2\2)*\7\'\2\2")
        buf.write("*\f\3\2\2\2+,\7-\2\2,\16\3\2\2\2-.\7/\2\2.\20\3\2\2\2")
        buf.write("/\60\7?\2\2\60\22\3\2\2\2\61\62\7-\2\2\62\63\7?\2\2\63")
        buf.write("\24\3\2\2\2\64\65\7/\2\2\65\66\7?\2\2\66\26\3\2\2\2\67")
        buf.write("8\7,\2\289\7?\2\29\30\3\2\2\2:;\7\61\2\2;<\7?\2\2<\32")
        buf.write("\3\2\2\2=?\t\2\2\2>=\3\2\2\2?@\3\2\2\2@>\3\2\2\2@A\3\2")
        buf.write("\2\2A\34\3\2\2\2BF\t\3\2\2CE\t\4\2\2DC\3\2\2\2EH\3\2\2")
        buf.write("\2FD\3\2\2\2FG\3\2\2\2G\36\3\2\2\2HF\3\2\2\2IK\t\5\2\2")
        buf.write("JI\3\2\2\2KL\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MN\3\2\2\2NO\b")
        buf.write("\20\2\2O \3\2\2\2\6\2@FL\3\b\2\2")
        return buf.getvalue()


class ProjectLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    NUM = 13
    VAR = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'*'", "'/'", "'%'", "'+'", "'-'", "'='", "'+='", 
            "'-='", "'*='", "'/='" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "VAR", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "NUM", "VAR", 
                  "WS" ]

    grammarFileName = "Project.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


