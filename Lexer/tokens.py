from enum import Enum, auto

class TokenType(Enum):
    COMMAND_ASSIGN = auto()
    OPERATOR_ARROW = auto()
    COMMAND_PRINT = auto()
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    LPAREN = auto()
    RPAREN = auto()
    IDENTIFIER = auto()
    STRING = auto()
    NUMBER = auto()
    NEWLINE = auto()
    EOF = auto()

class Token:
    def __init__(self, type_, value=None, line=0, column=0):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        if self.value is not None:
            return f"Token({self.type}, {self.value}, line={self.line}, col={self.column})"
        return f"Token({self.type}, line={self.line}, col={self.column})"
