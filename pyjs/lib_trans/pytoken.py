#! /usr/bin/env python

"""Token constants (from "token.h")."""

# https://fossies.org/linux/Python/Include/token.h
#  Taken from Python (r53757) and modified to include some tokens
#   originally monkeypatched in by pgen2.tokenize

#--start constants--
ENDMARKER = 0
NAME = 1
NUMBER = 2
STRING = 3
NEWLINE = 4
INDENT = 5
DEDENT = 6
LPAR = 7
RPAR = 8
LSQB = 9
RSQB = 10
COLON = 11
COMMA = 12
SEMI = 13
PLUS = 14
MINUS = 15
STAR = 16
SLASH = 17
VBAR = 18
AMPER = 19
LESS = 20
GREATER = 21
EQUAL = 22
DOT =  23
PERCENT = 24
LBRACE =  25
RBRACE =  26
EQEQUAL = 27
NOTEQUAL = 28
LESSEQUAL = 29
GREATEREQUAL = 30
TILDE = 31
CIRCUMFLEX = 32
LEFTSHIFT = 33
RIGHTSHIFT = 34
DOUBLESTAR = 35
PLUSEQUAL = 36
MINEQUAL = 37
STAREQUAL = 38
SLASHEQUAL = 39
PERCENTEQUAL = 40
AMPEREQUAL = 41
VBAREQUAL = 42
CIRCUMFLEXEQUAL 43
LEFTSHIFTEQUAL  44
RIGHTSHIFTEQUAL 45
DOUBLESTAREQUAL 46
DOUBLESLASH = 47
DOUBLESLASHEQUAL = 48
AT = 49
ATEQUAL = 50
RARROW = 51
ELLIPSIS = 52
COLONEQUAL = 53
OP = 54
AWAIT = 55
ASYNC = 56
TYPE_IGNORE = 57
TYPE_COMMENT = 58
ERRORTOKEN = 59
N_TOKENS = 63
NT_OFFSET = 256
#--end constants--

tok_name = {}
for _name, _value in list(globals().items()):
    if type(_value) is type(0):
 = tok_name[_value] = _name


def ISTERMINAL(x):
    return x < NT_OFFSET

def ISNONTERMINAL(x):
    return x >= NT_OFFSET

def ISEOF(x):
    return x == ENDMARKER
