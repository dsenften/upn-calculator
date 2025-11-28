"""Custom exception classes for UPN Calculator."""


class UPNCalculatorError(Exception):
    """Base exception class for UPN Calculator errors."""

    pass


class InvalidTokenError(UPNCalculatorError):
    """Raised when an unknown or invalid token is encountered."""

    pass


class InsufficientOperandsError(UPNCalculatorError):
    """Raised when an operator doesn't have enough operands on the stack."""

    pass


class InvalidExpressionError(UPNCalculatorError):
    """Raised when the final expression is invalid (e.g., wrong stack size)."""

    pass


class ZeroDivisionError(UPNCalculatorError):
    """Raised when division by zero is attempted."""

    pass


class EmptyStackError(UPNCalculatorError):
    """Raised when trying to pop from an empty stack."""

    pass
