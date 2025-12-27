//// LEXER
//
// This is the header file for the lexer.


//Includes
#include "tokens.h"


typedef struct Lexer {
    const char *source;
    int length;
    const char *language_pack;
    int pos;
    char current_char;
    int line;
    int column;
} Lexer;