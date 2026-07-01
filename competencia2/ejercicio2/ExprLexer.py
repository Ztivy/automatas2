# Generated from ./Expr.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,34,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,4,3,22,8,3,11,3,12,3,23,1,4,1,4,1,
        5,4,5,29,8,5,11,5,12,5,30,1,5,1,5,0,0,6,1,1,3,2,5,3,7,4,9,5,11,6,
        1,0,3,2,0,65,90,97,122,1,0,48,57,3,0,9,10,13,13,32,32,35,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,
        1,13,1,0,0,0,3,16,1,0,0,0,5,18,1,0,0,0,7,21,1,0,0,0,9,25,1,0,0,0,
        11,28,1,0,0,0,13,14,5,105,0,0,14,15,5,102,0,0,15,2,1,0,0,0,16,17,
        7,0,0,0,17,4,1,0,0,0,18,19,5,62,0,0,19,6,1,0,0,0,20,22,7,1,0,0,21,
        20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,8,1,0,0,
        0,25,26,5,43,0,0,26,10,1,0,0,0,27,29,7,2,0,0,28,27,1,0,0,0,29,30,
        1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,32,1,0,0,0,32,33,6,5,0,0,
        33,12,1,0,0,0,3,0,23,30,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ID = 2
    MAYOR_QUE = 3
    NUM = 4
    MAS = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'>'", "'+'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ID", "MAYOR_QUE", "NUM", "MAS", "WS" ]

    ruleNames = [ "IF", "ID", "MAYOR_QUE", "NUM", "MAS", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


