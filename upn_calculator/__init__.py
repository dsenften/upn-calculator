"""UPN Calculator - Reverse Polish Notation Stack-based Calculator."""

from .calculator import UPNCalculator
from .errors import (
    UPNCalculatorError,
    InvalidTokenError,
    InsufficientOperandsError,
    InvalidExpressionError,
    ZeroDivisionError,
    EmptyStackError,
)
from .parser import is_number, is_operator, tokenize
from .operators import apply_operator, OPERATORS

__version__ = "0.1.0"
__all__ = [
    "UPNCalculator",
    "UPNCalculatorError",
    "InvalidTokenError",
    "InsufficientOperandsError",
    "InvalidExpressionError",
    "ZeroDivisionError",
    "EmptyStackError",
    "is_number",
    "is_operator",
    "tokenize",
    "apply_operator",
    "OPERATORS",
]
