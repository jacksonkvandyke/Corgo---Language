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
    set x -> 10
    set y -> 15
    set x -> 1
    print -> "Hello"
    print -> y
    print -> x
    """
    run_source(source)
