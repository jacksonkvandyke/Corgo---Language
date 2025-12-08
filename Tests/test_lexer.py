import sys
import os

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_root)

from Lexer.lexer import Lexer
from Lexer.tokens import TokenType
from LanguagePacks.english import LANGUAGE_PACK

# Sample source code to test
source = '''
set x -> 10
print -> "Hello"
set y -> 4200000a
'''

# Create the lexer
lexer = Lexer(source, LANGUAGE_PACK)

# Fetch tokens until EOF
while True:
    token = lexer.get_next_token()
    print(token)

    if token.type == TokenType.EOF:
        break
