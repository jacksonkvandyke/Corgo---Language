//// TOKENS
//
// This include is used to store the TokenTypes and Token struct for the language.

#ifndef TOKENS_H
#define TOKENS_H

typedef enum TokenType {
    // These types are used throughout the lexer to turn source code into tokens.
    COMMAND_ASSIGN,
    OPERATOR_ARROW,
    COMMAND_PRINT,
    PLUS,
    MINUS,
    MULTIPLY,
    DIVIDE,
    LPAREN,
    RPAREN,
    IDENTIFIER,
    STRING,
    NUMBER,
    NEWLINE,
    TOKEN_EOF
} TokenType;

typedef struct Token {
    // This struct is designed to point to the original memory definition used to generate the token making garbage cleanup easier.
    TokenType type;
    const char *start;
    int length;
    int line;
    int column;
} Token;

typedef struct Keyword { 
    const char *name; 
    TokenType type; 
} Keyword; 

#endif