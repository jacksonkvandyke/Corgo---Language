from Lexer.tokens import TokenType

# ============================
# TOKEN TO ACTION
# ============================
LANGUAGE_PACK = {
    "set": TokenType.COMMAND_ASSIGN,
    "print": TokenType.COMMAND_PRINT,
}
