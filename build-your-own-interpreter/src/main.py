"""
Build Your Own Interpreter – Expression Evaluator
Author: Ihunna Amugo | Build-Your-Own-X Series

🧮 Goal:
Implement a minimal interpreter that can:
- Tokenize and parse arithmetic expressions
- Build an abstract syntax tree (AST)
- Recursively evaluate the result

🔬 Healthcare Example:
You could expand this to parse a formula like:
  perfusion = pressure * velocity

This is the foundation for domain-specific modeling languages (e.g. FEM config, EHR formula logic).
"""

import operator
import re

# ----- Lexer: Convert string to list of tokens -----
def tokenize(expr):
    # Match numbers, operators, and parentheses
    token_pattern = r"\d+|[()+\-*/]"
    return re.findall(token_pattern, expr)

# ----- Parser: Convert tokens into nested structure -----
def parse(tokens):
    def parse_expr(index=0):
        result = []
        while index < len(tokens):
            token = tokens[index]
            if token == '(':
                subtree, index = parse_expr(index + 1)
                result.append(subtree)
            elif token == ')':
                return result, index
            else:
                result.append(token)
            index += 1
        return result, index
    parsed_tree, _ = parse_expr()
    return parsed_tree

# ----- Evaluator: Recursively compute expression -----
def evaluate(expr):
    if isinstance(expr, list):
        if len(expr) == 1:
            return evaluate(expr[0])
        elif len(expr) == 3:
            a, op, b = expr
            a = evaluate(a)
            b = evaluate(b)
            ops = {
                '+': operator.add,
                '-': operator.sub,
                '*': operator.mul,
                '/': operator.truediv
            }
            return ops[op](a, b)
        else:
            raise ValueError("Invalid expression")
    else:
        return float(expr)

# ----- REPL Loop -----
def run():
    print("Welcome to Ihunna's Interpreter (Type 'exit' to quit)")
    while True:
        expr = input(">> ")
        if expr.lower() in ["exit", "quit"]:
            break
        try:
            tokens = tokenize(expr)
            parsed = parse(tokens)
            result = evaluate(parsed)
            print("= ", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    run()
