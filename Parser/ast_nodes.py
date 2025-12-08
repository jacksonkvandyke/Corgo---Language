# ============================
# Base AST Node
# ============================

class ASTNode:
    def pretty(self, indent=0, is_last=True):
        """
        Pretty-print the AST using ASCII tree branches.
        """
        pad = " " * indent
        branch = "└── " if is_last else "├── "
        return f"{pad}{branch}{self._pretty_label()}\n"

    def _pretty_label(self):
        """
        Override in subclasses to define the label shown in the tree.
        """
        return self.__class__.__name__


# ============================
# Program Node
# ============================

class ProgramNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"ProgramNode(statements={self.statements})"

    def pretty(self, indent=0, is_last=True):
        pad = " " * indent
        branch = "└── " if is_last else "├── "
        result = f"{pad}{branch}Program\n"

        for i, stmt in enumerate(self.statements):
            last = (i == len(self.statements) - 1)
            result += stmt.pretty(indent + 4, is_last=last)

        return result


# ============================
# Assignment Node
# ============================

class AssignNode(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"AssignNode(name={self.name}, value={self.value})"

    def _pretty_label(self):
        return f"Assign(name={self.name})"

    def pretty(self, indent=0, is_last=True):
        pad = " " * indent
        branch = "└── " if is_last else "├── "
        result = f"{pad}{branch}{self._pretty_label()}\n"

        # Value is always last child
        result += self.value.pretty(indent + 4, is_last=True)

        return result


# ============================
# Print Node
# ============================

class PrintNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"PrintNode(value={self.value})"

    def _pretty_label(self):
        return "Print"

    def pretty(self, indent=0, is_last=True):
        pad = " " * indent
        branch = "└── " if is_last else "├── "
        result = f"{pad}{branch}Print\n"

        result += self.value.pretty(indent + 4, is_last=True)

        return result


# ============================
# Number Node
# ============================

class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = int(value)

    def __repr__(self):
        return f"NumberNode({self.value})"

    def _pretty_label(self):
        return f"Number({self.value})"


# ============================
# String Node
# ============================

class StringNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"StringNode({self.value})"

    def _pretty_label(self):
        return f'String("{self.value}")'


# ============================
# Identifier Node
# ============================

class IdentifierNode(ASTNode):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"IdentifierNode({self.name})"

    def _pretty_label(self):
        return f"Identifier({self.name})"


