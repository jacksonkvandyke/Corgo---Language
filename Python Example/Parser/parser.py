from Lexer.tokens import TokenType
from Parser.ast_nodes import *

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    # ============================
    # Utility
    # ============================
    def error(self, message):
        raise Exception(
            f"Parser error at line {self.current_token.line}, "
            f"column {self.current_token.column}: {message}"
        )

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"Expected {token_type}, got {self.current_token.type}")

    # ============================
    # Entry point
    # ============================
    def parse(self):
        statements = []

        while self.current_token.type != TokenType.EOF:
            # Skip NEWLINE tokens if you decide to emit them
            if self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
                continue

            stmt = self.parse_statement()
            statements.append(stmt)

        return ProgramNode(statements)

    # ============================
    # Statement dispatcher
    # ============================
    def parse_statement(self):
        token_type = self.current_token.type

        if token_type == TokenType.COMMAND_ASSIGN:
            return self.parse_assignment()

        if token_type == TokenType.COMMAND_PRINT:
            return self.parse_print()

        self.error(f"Unexpected token {token_type} at start of statement")

    # ============================
    # Assignment: set x -> expr
    # ============================
    def parse_assignment(self):
        self.eat(TokenType.COMMAND_ASSIGN)

        if self.current_token.type != TokenType.IDENTIFIER:
            self.error("Expected identifier after assignment command")

        name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)

        self.eat(TokenType.OPERATOR_ARROW)

        value = self.parse_expression()

        return AssignNode(name, value)

    # ============================
    # Print: print -> expr
    # ============================
    def parse_print(self):
        self.eat(TokenType.COMMAND_PRINT)
        self.eat(TokenType.OPERATOR_ARROW)

        value = self.parse_expression()

        return PrintNode(value)

    # ============================
    # Expressions: NUMBER | STRING | IDENTIFIER
    # ============================
    def parse_primary(self):
        token = self.current_token

        if token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return NumberNode(token.value)

        if token.type == TokenType.STRING:
            self.eat(TokenType.STRING)
            return StringNode(token.value)

        if token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
            return IdentifierNode(token.value)

        if token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            expr = self.parse_expression()
            self.eat(TokenType.RPAREN)
            return expr
        
        self.error(f"Unexpected token in expression: {token.type}")
        
    # ============================
    # Parse Expression
    # ============================
    def parse_expression(self):
        node = self.parse_term()

        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current_token
            self.eat(op.type)
            right = self.parse_term()
            node = BinaryOpNode(node, op, right)

        return node
    
    # ============================
    # Parse Term
    # ============================
    def parse_term(self):
        node = self.parse_primary()

        while self.current_token.type in (TokenType.STAR, TokenType.SLASH):
            op = self.current_token
            self.eat(op.type)
            right = self.parse_primary()
            node = BinaryOpNode(node, op, right)

        return node
