//// LEXER
//
// This program converts the source code into Tokens which will then be parsed into code.


//C Includes
#include <stdio.h>
#include <string.h>


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




//Test main
int main(void) {
    struct Lexer lexer;

    lexer.source = "Test string value.";
    lexer.length = strlen(lexer.source);
    lexer.pos = 0;
    lexer.current_char = lexer.source[lexer.pos];
    lexer.line = 0;
    lexer.column = 0;

    while (lexer.current_char != '\0') {
        printf("%c", lexer.current_char);
        LexAdvance(&lexer);
    }

    return 0;
}
