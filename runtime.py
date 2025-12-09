import sys
import os

# Ensure project root is on the path
project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, project_root)

from Lexer.lexer import Lexer
from Parser.parser import Parser
from Interpreter.interpreter import Interpreter
from LanguagePacks.english import LANGUAGE_PACK


def run_source(source: str):
    lexer = Lexer(source, LANGUAGE_PACK)
    parser = Parser(lexer)
    ast = parser.parse()

    print(ast.pretty())

    interpreter = Interpreter()
    interpreter.visit(ast)


if __name__ == "__main__":
    source = """
    print -> 1 + 2
    print -> 10 - 3
    print -> 4 * 5
    print -> 20 / 4

    print -> 1 + 2 * 3
    print -> (1 + 2) * 3
    print -> 10 - 2 * 3
    print -> (10 - 2) * 3

    set a -> 5
    set b -> 10
    print -> a + b
    print -> a * b + 2
    print -> a + b * 2
    print -> (a + b) * 2

    set a -> 3
    print -> a * (b - 5)
    """

    run_source(source)

