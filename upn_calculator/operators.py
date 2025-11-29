"""Operator definitions and application functions."""

from .errors import ZeroDivisionError

OPERATORS = {"+", "-", "*", "/"}


def apply_operator(a: float, b: float, op: str) -> float:
    """
    Apply a binary operator to two operands.

    Important: Stack is LIFO, so when we pop b then a, we compute a op b.

    Args:
        a: First operand (popped second from stack).
        b: Second operand (popped first from stack).
        op: Operator string (+, -, *, /).

    Returns:
        The result of the operation.

    Raises:
        ZeroDivisionError: If trying to divide by zero.
        ValueError: If operator is not recognized.

    Examples:
        >>> apply_operator(2, 3, "+")
        5.0
        >>> apply_operator(10, 3, "-")
        7.0
        >>> apply_operator(2, 3, "*")
        6.0
        >>> apply_operator(10, 2, "/")
        5.0
    """
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b
    else:
        raise ValueError(f"Unknown operator: {op}")
