class Interpreter:
    def __init__(self):
        # Variable environment
        self.env = {}

    # ============================
    # Visitor dispatcher
    # ============================
    def visit(self, node):
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name, None)

        if method is None:
            raise Exception(f"No visit_{type(node).__name__} method defined")

        return method(node)

    # ============================
    # Program
    # ============================
    def visit_ProgramNode(self, node):
        for stmt in node.statements:
            self.visit(stmt)

    # ============================
    # Assignment
    # ============================
    def visit_AssignNode(self, node):
        value = self.visit(node.value)
        self.env[node.name] = value
        return value

    # ============================
    # Print
    # ============================
    def visit_PrintNode(self, node):
        value = self.visit(node.value)
        print(value)
        return value

    # ============================
    # Expressions
    # ============================
    def visit_NumberNode(self, node):
        return node.value

    def visit_StringNode(self, node):
        return node.value

    def visit_IdentifierNode(self, node):
        if node.name not in self.env:
            raise Exception(f"Undefined variable '{node.name}'")
        return self.env[node.name]
