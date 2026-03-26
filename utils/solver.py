from sympy import symbols, Eq, solve, sympify
import re

x = symbols('x')

def clean_equation(eq):

    # remove spaces
    eq = eq.replace(" ", "")

    # add * between number and bracket 2( -> 2*(
    eq = re.sub(r'(\d)\(', r'\1*(', eq)

    # add * between number and variable 3x -> 3*x
    eq = re.sub(r'(\d)x', r'\1*x', eq)

    return eq


def solve_equation(equation):

    steps = []

    equation = clean_equation(equation)

    steps.append(f"Original Equation: {equation}")

    left, right = equation.split("=")

    left_expr = sympify(left)
    right_expr = sympify(right)

    eq = Eq(left_expr, right_expr)

    # Step 1 Expand
    expanded = left_expr.expand()

    if expanded != left_expr:
        steps.append("Step 1: Expand the bracket")
        steps.append(f"{expanded} = {right}")
        left_expr = expanded
        eq = Eq(left_expr, right_expr)

    # Step 2 Move constants
    steps.append("Step 2: Move constants to one side")

    simplified = left_expr - right_expr

    steps.append(f"{simplified} = 0")

    # Step 3 Solve
    solution = solve(eq, x)

    steps.append("Step 3: Solve for x")
    steps.append(f"x = {solution}")

    return steps, solution