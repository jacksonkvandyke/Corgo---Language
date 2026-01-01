//// LEXER
//
// This program converts the source code into Tokens which will then be parsed into code.


//C Includes
#include <stdio.h>
#include <string.h>
#include <ctype.h>


//MY Includes
#include "lexer.h"


////Lexer Functions

//Lex-Advance - Advance the lexer pointer.
int LexAdvance(struct Lexer *lexer) {
    //Check for new line
    if (lexer->current_char == '\n'){
        lexer->line += 1;
        lexer->column = 0;
    }

    //Advance
    lexer->pos += 1;
    lexer->column += 1;

    //Check if we are beyond the source
    if (lexer->pos >= lexer->length){
        lexer->current_char = '\0';
    } else {
        lexer->current_char = lexer->source[lexer->pos];
    }

    return 0;
}

//Lex-Peek - Look at the next character without incrementing the lexer.
char LexPeek (struct Lexer *lexer){
    int next_pos = lexer->pos + 1;
    if (next_pos >= lexer->length){
        return '\0';
    } else {
        return lexer->current_char;
    }
}

//Lex-SkipWhitespace - Skip all whitespace.
int LexSkipWhitespace (struct Lexer *lexer) {
    while ((isspace(lexer->current_char)) && (lexer->current_char != '\0')) {
        LexAdvance(lexer);
    }

    return 0;
}

//Lex-IdentifierORKeyword - Get an identifier or keyword.


//Lex-GetNextToken - Get the next token from source.
Token LexGetNextToken(struct Lexer *lexer) {
    while (lexer->current_char != '\0'){
        //Check for new-line
        if (lexer->current_char == '\n') {
            //Create the token
            Token token;
            token.type = NEWLINE;
            token.start = lexer->source + lexer->pos;
            token.length = 1;
            token.line = lexer->line;
            token.column = lexer->column;

            //Advance the lexer
            LexAdvance(lexer);

            //Return the token
            return token;
        }

        //Check for whitespace
        if (isspace(lexer->current_char)) {
            LexSkipWhitespace(lexer);
            continue;
        }

        //Check for arrow notation
        if ((lexer->current_char == '-') && (LexPeek(lexer) == '>')) {
            //Create the token
            Token token;
            token.type = OPERATOR_ARROW;
            token.start = lexer->source + lexer->pos;
            token.length = 2;
            token.line = lexer->line;
            token.column = lexer->column;

            //Advance the lexer 2 since we absorbed 2 characters
            LexAdvance(lexer);
            LexAdvance(lexer);

            //Return the token
            return token;
        }

        //Check for alpha characters
        if (isalpha(lexer->current_char)) {

        }

        ////TEST ADVANCE
        LexAdvance(lexer);
    }
}


//Test main
int main(void) {
    struct Lexer lexer;

    lexer.source = "Test string value.\n";
    lexer.length = strlen(lexer.source);
    lexer.pos = 0;
    lexer.current_char = lexer.source[lexer.pos];
    lexer.line = 0;
    lexer.column = 0;

    while (lexer.current_char != '\0') {
        Token token = LexGetNextToken(&lexer);
        printf("%d", token.type);
    }

    return 0;
}
