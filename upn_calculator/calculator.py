"""UPN (Reverse Polish Notation) Stack-based Calculator implementation."""

from typing import List

from .errors import (
    InsufficientOperandsError,
    InvalidExpressionError,
    InvalidTokenError,
    EmptyStackError,
)
from .parser import is_number, is_operator, tokenize
from .operators import apply_operator


class UPNCalculator:
    """
    A stack-based calculator for Reverse Polish Notation (UPN) expressions.

    UPN is a postfix notation where operands come before operators.
    Examples:
        - "2 3 +" evaluates to 5
        - "10 3 -" evaluates to 7
        - "2 3 + 4 *" evaluates to 20
    """

    def __init__(self):
        """Initialize the calculator with an empty stack."""
        self.stack: List[float] = []

    def evaluate(self, expression: str) -> float:
        """
        Evaluate a UPN expression and return the result.

        Algorithm:
        1. Split expression into tokens
        2. For each token:
           - If number: push to stack
           - If operator: pop 2 operands, apply operator, push result
           - Otherwise: raise InvalidTokenError
        3. After all tokens, stack must have exactly 1 element (the result)

        Args:
            expression: A UPN expression string (e.g., "2 3 +").

        Returns:
            The result of the evaluation as a float.

        Raises:
            InvalidTokenError: If an unknown token is encountered.
            InsufficientOperandsError: If an operator has fewer than 2 operands.
            InvalidExpressionError: If the final stack size is not 1.

        Examples:
            >>> calc = UPNCalculator()
            >>> calc.evaluate("2 3 +")
            5.0
            >>> calc.evaluate("10 3 -")
            7.0
            >>> calc.evaluate("2 3 + 4 *")
            20.0
            >>> calc.evaluate("-5 3 +")
            -2.0
        """
        tokens = tokenize(expression)
        self.stack = []  # Clear stack for new evaluation

        for token in tokens:
            if is_number(token):
                self.stack.append(float(token))
            elif is_operator(token):
                if len(self.stack) < 2:
                    msg = (
                        f"Operator '{token}' requires 2 operands "
                        f"but stack has {len(self.stack)}"
                    )
                    raise InsufficientOperandsError(msg)
                b = self.stack.pop()
                a = self.stack.pop()
                result = apply_operator(a, b, token)
                self.stack.append(result)
            else:
                raise InvalidTokenError(f"Unknown token: '{token}'")

        if len(self.stack) != 1:
            msg = (
                f"Invalid expression: stack must have exactly 1 element, "
                f"but has {len(self.stack)}"
            )
            raise InvalidExpressionError(msg)

        return self.stack[0]

    def push(self, value: float) -> None:
        """
        Manually push a value onto the stack.

        Args:
            value: The value to push.
        """
        self.stack.append(value)

    def pop(self) -> float:
        """
        Manually pop a value from the stack.

        Returns:
            The popped value.

        Raises:
            EmptyStackError: If the stack is empty.
        """
        if not self.stack:
            raise EmptyStackError("Cannot pop from an empty stack")
        return self.stack.pop()

    def get_stack(self) -> List[float]:
        """
        Get a copy of the current stack.

        Returns:
            A list representing the current stack (top at end).

        Examples:
            >>> calc = UPNCalculator()
            >>> calc.evaluate("2 3 +")
            5.0
            >>> calc.get_stack()
            [5.0]
        """
        return self.stack.copy()

    def clear_stack(self) -> None:
        """Clear the stack."""
        self.stack = []

    def peek(self) -> float:
        """
        Get the top value of the stack without removing it.

        Returns:
            The top value.

        Raises:
            EmptyStackError: If the stack is empty.
        """
        if not self.stack:
            raise EmptyStackError("Cannot peek an empty stack")
        return self.stack[-1]
