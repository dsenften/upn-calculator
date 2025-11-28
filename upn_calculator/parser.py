"""Token parsing and validation functions for UPN expressions."""

from typing import List


def is_number(token: str) -> bool:
    """
    Check if a token is a valid number (integer or float).

    Args:
        token: The token to check.

    Returns:
        True if the token can be parsed as a float, False otherwise.

    Examples:
        >>> is_number("5")
        True
        >>> is_number("3.14")
        True
        >>> is_number("-5")
        True
        >>> is_number("1e-10")
        True
        >>> is_number("+")
        False
        >>> is_number("xyz")
        False
    """
    try:
        float(token)
        return True
    except ValueError:
        return False


def is_operator(token: str) -> bool:
    """
    Check if a token is a valid operator.

    Args:
        token: The token to check.

    Returns:
        True if the token is an operator in {+, -, *, /}, False otherwise.

    Examples:
        >>> is_operator("+")
        True
        >>> is_operator("-")
        True
        >>> is_operator("*")
        True
        >>> is_operator("/")
        True
        >>> is_operator("5")
        False
        >>> is_operator("sin")
        False
    """
    return token in {"+", "-", "*", "/"}


def tokenize(expression: str) -> List[str]:
    """
    Split an expression string into tokens by whitespace.

    Args:
        expression: The UPN expression string.

    Returns:
        A list of tokens.

    Examples:
        >>> tokenize("2 3 +")
        ['2', '3', '+']
        >>> tokenize("10 3 - 4 *")
        ['10', '3', '-', '4', '*']
        >>> tokenize("2.5   1.5   +")
        ['2.5', '1.5', '+']
    """
    return expression.split()
