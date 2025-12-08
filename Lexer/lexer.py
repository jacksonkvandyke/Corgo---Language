from Lexer.tokens import *

class Lexer():
    def __init__(self, source, language_pack):
        self.source = source
        self.language_pack = language_pack
        self.pos = 0
        self.current_char = self.source[self.pos] if self.source else None
        self.line = 1
        self.column = 1

    def advance(self):
        #Check for new line
        if self.current_char == '\n':
            self.line += 1
            self.column = 0

        self.pos += 1
        self.column += 1

        if self.pos >= len(self.source):
            self.current_char = None
        else:
            self.current_char = self.source[self.pos]

    def peek(self):
        next_pos = self.pos + 1
        if next_pos >= len(self.source):
            return None
        return self.source[next_pos]
    
    def error(self, message):
        raise Exception(f"[Line {self.line}, Col {self.column}] {message}")
    
    def get_next_token(self):
        while self.current_char is not None:

            if self.current_char == '\n':
                start_line = self.line
                start_column = self.column
                self.advance()
                return Token(TokenType.NEWLINE, None, start_line, start_column)
        
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char == '-' and self.peek() == '>':
                start_line = self.line
                start_column = self.column
                self.advance()
                self.advance()
                return Token(TokenType.OPERATOR_ARROW, None, start_line, start_column)

            if self.current_char.isalpha():
                return self.identifier_or_keyword()

            if self.current_char.isdigit():
                return self.number()

            if self.current_char == '"':
                return self.string()
            
            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(TokenType.MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(TokenType.STAR, '*')

            if self.current_char == '/':
                self.advance()
                return Token(TokenType.SLASH, '/')

            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RPAREN, ')')

            # Unknown character
            self.error("Unexpected character")

        return Token(TokenType.EOF)
    
    def skip_whitespace(self):
        '''
            Skips whitespace.
        '''
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def identifier_or_keyword(self):
        """
        Extracts identifiers and keywords.
        """
        start_line = self.line
        start_column = self.column

        token = ''

        while self.current_char is not None and self.current_char.isalpha():
            token += self.current_char
            self.advance()

        if token in self.language_pack:
            return Token(self.language_pack[token], None, start_line, start_column)

        return Token(TokenType.IDENTIFIER, token, start_line, start_column)
    
    def number(self):
        '''
            Extracts numbers.
        '''
        start_line = self.line
        start_column = self.column
        
        token = ''

        while self.current_char is not None and self.current_char.isdigit():
            token += self.current_char
            self.advance()

        return Token(TokenType.NUMBER, token, start_line, start_column)
    
    def string(self):
        start_line = self.line
        start_column = self.column

        self.advance()
        token = ''

        while self.current_char is not None and self.current_char != '"':
            token += self.current_char
            self.advance()

        if self.current_char != '"':
            self.error("Unterminated string")

        self.advance()

        return Token(TokenType.STRING, token, start_line, start_column)


        





