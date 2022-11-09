# Generated from Project.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("\33\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\13\n\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2\26\n\2\f\2\16\2\31\13")
        buf.write("\2\3\2\2\3\2\3\2\2\4\3\2\6\b\3\2\t\n\2\35\2\n\3\2\2\2")
        buf.write("\4\5\b\2\1\2\5\6\7\3\2\2\6\7\5\2\2\2\7\b\7\4\2\2\b\13")
        buf.write("\3\2\2\2\t\13\7\13\2\2\n\4\3\2\2\2\n\t\3\2\2\2\13\27\3")
        buf.write("\2\2\2\f\r\f\6\2\2\r\16\7\5\2\2\16\26\5\2\2\7\17\20\f")
        buf.write("\5\2\2\20\21\t\2\2\2\21\26\5\2\2\6\22\23\f\4\2\2\23\24")
        buf.write("\t\3\2\2\24\26\5\2\2\5\25\f\3\2\2\2\25\17\3\2\2\2\25\22")
        buf.write("\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30")
        buf.write("\3\3\2\2\2\31\27\3\2\2\2\5\n\25\27")
        return buf.getvalue()


class ProjectParser ( Parser ):

    grammarFileName = "Project.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'**'", "'*'", "'/'", "'%'", 
                     "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "EXPON", "MULT", 
                      "DIV", "MOD", "ADD", "SUB", "ATOM", "NUM", "CHAR", 
                      "VAR", "WS" ]

    RULE_expression = 0

    ruleNames =  [ "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    EXPON=3
    MULT=4
    DIV=5
    MOD=6
    ADD=7
    SUB=8
    ATOM=9
    NUM=10
    CHAR=11
    VAR=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ExpressionContext
            self.expr = None # ExpressionContext
            self.terminal = None # Token
            self.operator = None # Token
            self.right = None # ExpressionContext

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ProjectParser.ExpressionContext,i)


        def ATOM(self):
            return self.getToken(ProjectParser.ATOM, 0)

        def EXPON(self):
            return self.getToken(ProjectParser.EXPON, 0)

        def MULT(self):
            return self.getToken(ProjectParser.MULT, 0)

        def DIV(self):
            return self.getToken(ProjectParser.DIV, 0)

        def MOD(self):
            return self.getToken(ProjectParser.MOD, 0)

        def ADD(self):
            return self.getToken(ProjectParser.ADD, 0)

        def SUB(self):
            return self.getToken(ProjectParser.SUB, 0)

        def getRuleIndex(self):
            return ProjectParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ProjectParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ProjectParser.T__0]:
                self.state = 3
                self.match(ProjectParser.T__0)
                self.state = 4
                localctx.expr = self.expression(0)
                self.state = 5
                self.match(ProjectParser.T__1)
                pass
            elif token in [ProjectParser.ATOM]:
                self.state = 7
                localctx.terminal = self.match(ProjectParser.ATOM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 21
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 19
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ProjectParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 10
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 11
                        localctx.operator = self.match(ProjectParser.EXPON)
                        self.state = 12
                        localctx.right = self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = ProjectParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 13
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 14
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ProjectParser.MULT) | (1 << ProjectParser.DIV) | (1 << ProjectParser.MOD))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 15
                        localctx.right = self.expression(4)
                        pass

                    elif la_ == 3:
                        localctx = ProjectParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 16
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 17
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ProjectParser.ADD or _la==ProjectParser.SUB):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 18
                        localctx.right = self.expression(3)
                        pass

             
                self.state = 23
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




