//// LEXER
//
// This program converts the source code into Tokens which will then be parsed into code.


//C Includes
#include <stdio.h>
#include <string.h>
#include <ctype.h>


//MY Includes
#include "lexer.h"
#include "languages.h"


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
Token LexIdentifierORKeyword (struct Lexer *lexer) {
    //Get the start of this token
    const char *tokenstart = lexer->source + lexer->pos;
    int tokenlength = 0;
    int line = lexer->line;
    int column = lexer->column;

    //Continue to advance the lexer until we find a valid token, or not.
    while ((lexer->current_char != '\0') && isalpha(lexer->current_char)){
        tokenlength += 1;
        LexAdvance(lexer);
    }

    //Store the string using memcpy
    char tokenbuffer[tokenlength + 1];
    memcpy(tokenbuffer, tokenstart, tokenlength);
    tokenbuffer[tokenlength] = '\0';

    //Check if the string is a valid keyword

    //Build identifier token and return
    Token token;
    token.type = IDENTIFIER;
    token.start = tokenstart;
    token.length = tokenlength;
    token.line = line;
    token.column = column;
    return token;
}


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

        //Check for an identifier or keyword
        if (isalpha(lexer->current_char)) {
            return LexIdentifierORKeyword(lexer);
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
    lexer.language_pack = EnglishPack;
    lexer.pos = 0;
    lexer.current_char = lexer.source[lexer.pos];
    lexer.line = 0;
    lexer.column = 0;

    printf(lexer.language_pack->name);

    return 0;
}
