"""Unit tests for UPN Calculator - tests for task-001 acceptance criteria."""

import pytest
from upn_calculator import (
    UPNCalculator,
    InvalidTokenError,
    InsufficientOperandsError,
    InvalidExpressionError,
    ZeroDivisionError,
    EmptyStackError,
)


class TestBasicParsing:
    """Tests for basic parsing and tokenization."""

    def test_single_number(self):
        """Test parsing single number."""
        calc = UPNCalculator()
        result = calc.evaluate("5")
        assert result == 5.0

    def test_whitespace_separator(self):
        """Test that whitespace correctly separates tokens."""
        calc = UPNCalculator()
        result = calc.evaluate("2   3   +")
        assert result == 5.0


class TestNumericTokens:
    """Tests for numeric token recognition (AC 2)."""

    def test_integer_tokens(self):
        """Test recognition of integer tokens."""
        calc = UPNCalculator()
        result = calc.evaluate("5 10 +")
        assert result == 15.0

    def test_float_tokens(self):
        """Test recognition of float tokens."""
        calc = UPNCalculator()
        result = calc.evaluate("2.5 1.5 +")
        assert result == 4.0

    def test_negative_numbers(self):
        """Test recognition of negative numbers."""
        calc = UPNCalculator()
        result = calc.evaluate("-5 3 +")
        assert result == -2.0

    def test_scientific_notation(self):
        """Test recognition of scientific notation."""
        calc = UPNCalculator()
        result = calc.evaluate("1e-10 2e-10 +")
        assert pytest.approx(result, abs=1e-12) == 3e-10


class TestOperatorTokens:
    """Tests for operator token recognition (AC 3)."""

    def test_plus_operator(self):
        """Test + operator recognition."""
        calc = UPNCalculator()
        result = calc.evaluate("2 3 +")
        assert result == 5.0

    def test_minus_operator(self):
        """Test - operator recognition."""
        calc = UPNCalculator()
        result = calc.evaluate("10 3 -")
        assert result == 7.0

    def test_multiply_operator(self):
        """Test * operator recognition."""
        calc = UPNCalculator()
        result = calc.evaluate("4 5 *")
        assert result == 20.0

    def test_divide_operator(self):
        """Test / operator recognition."""
        calc = UPNCalculator()
        result = calc.evaluate("20 4 /")
        assert result == 5.0


class TestStackImplementation:
    """Tests for stack functionality (AC 4, 5)."""

    def test_stack_operations_basic(self):
        """Test that stack correctly handles push/pop."""
        calc = UPNCalculator()
        calc.push(5.0)
        calc.push(3.0)
        assert calc.get_stack() == [5.0, 3.0]
        assert calc.pop() == 3.0
        assert calc.get_stack() == [5.0]

    def test_evaluation_uses_stack(self):
        """Test that evaluation correctly uses stack operations."""
        calc = UPNCalculator()
        result = calc.evaluate("2 3 +")
        assert result == 5.0


class TestStackEvaluation:
    """Tests for stack evaluation algorithm (AC 5)."""

    def test_single_operation(self):
        """Test single operation evaluation."""
        calc = UPNCalculator()
        result = calc.evaluate("2 3 +")
        assert result == 5.0

    def test_chained_operations(self):
        """Test multiple operations (2 3 + 4 * = (2+3)*4 = 20)."""
        calc = UPNCalculator()
        result = calc.evaluate("2 3 + 4 *")
        assert result == 20.0

    def test_complex_chained_operations(self):
        """Test complex expression: (10 - 3) * 2 = 14."""
        calc = UPNCalculator()
        result = calc.evaluate("10 3 - 2 *")
        assert result == 14.0


class TestValidExpression:
    """Tests for valid expression requirement (AC 6)."""

    def test_valid_expression_single_result(self):
        """Test that valid expression leaves exactly one element on stack."""
        calc = UPNCalculator()
        result = calc.evaluate("2 3 +")
        assert calc.get_stack() == [result]

    def test_invalid_expression_too_many_operands(self):
        """Test error when too many operands remain on stack (AC 6)."""
        calc = UPNCalculator()
        with pytest.raises(InvalidExpressionError) as exc_info:
            calc.evaluate("2 3 4 +")
        assert "exactly 1 element" in str(exc_info.value).lower()


class TestErrorHandling:
    """Tests for error handling (AC 7, 8, 9)."""

    def test_invalid_token_error(self):
        """Test error for invalid/unknown token (AC 7)."""
        calc = UPNCalculator()
        with pytest.raises(InvalidTokenError) as exc_info:
            calc.evaluate("2 3 xyz +")
        assert "xyz" in str(exc_info.value)

    def test_insufficient_operands_single_operator(self):
        """Test error when operator has insufficient operands (AC 8)."""
        calc = UPNCalculator()
        with pytest.raises(InsufficientOperandsError) as exc_info:
            calc.evaluate("2 +")
        assert "2 operands" in str(exc_info.value).lower()

    def test_insufficient_operands_after_operations(self):
        """Test error when operator lacks operands after prior operations.
        
        Example: "2 + 3 +" → After "2 +" tries to pop, only 2 is on stack initially.
        Better example: "2 3 + +" → After 2+3=5 computed, the final + needs 2 operands
        but only 5 remains.
        """
        calc = UPNCalculator()
        with pytest.raises(InsufficientOperandsError):
            # This should fail: push 2, then immediate operator needs another operand
            calc.evaluate("2 + 3")


    def test_division_by_zero_error(self):
        """Test error for division by zero (AC 9)."""
        calc = UPNCalculator()
        with pytest.raises(ZeroDivisionError):
            calc.evaluate("10 0 /")


class TestFloatPrecision:
    """Tests for float precision (AC 10)."""

    def test_float_precision_ieee754(self):
        """Test that results maintain IEEE 754 64-bit precision."""
        calc = UPNCalculator()
        result = calc.evaluate("0.1 0.2 +")
        # IEEE 754 has precision limits, but should be within 1e-15
        assert pytest.approx(result, abs=1e-15) == 0.3

    def test_float_precision_small_numbers(self):
        """Test precision with very small numbers."""
        calc = UPNCalculator()
        result = calc.evaluate("1e-100 2e-100 +")
        assert pytest.approx(result, abs=1e-115) == 3e-100

    def test_float_precision_large_numbers(self):
        """Test precision with very large numbers."""
        calc = UPNCalculator()
        result = calc.evaluate("1e100 2e100 +")
        assert pytest.approx(result, rel=1e-14) == 3e100


class TestOrderOfOperations:
    """Tests for operator associativity and order (important for stack LIFO)."""

    def test_subtraction_order(self):
        """Test that subtraction preserves order (10 - 3 = 7, not -7)."""
        calc = UPNCalculator()
        result = calc.evaluate("10 3 -")
        assert result == 7.0  # Not -7

    def test_division_order(self):
        """Test that division preserves order (20 / 4 = 5, not 0.2)."""
        calc = UPNCalculator()
        result = calc.evaluate("20 4 /")
        assert result == 5.0  # Not 0.2


class TestStackManagement:
    """Tests for stack management methods."""

    def test_clear_stack(self):
        """Test clearing the stack."""
        calc = UPNCalculator()
        calc.evaluate("2 3 +")
        calc.clear_stack()
        assert calc.get_stack() == []

    def test_peek_stack(self):
        """Test peeking at top of stack without removing."""
        calc = UPNCalculator()
        calc.push(5.0)
        calc.push(3.0)
        assert calc.peek() == 3.0
        assert calc.get_stack() == [5.0, 3.0]  # Stack unchanged

    def test_pop_empty_stack_error(self):
        """Test error when popping empty stack."""
        calc = UPNCalculator()
        with pytest.raises(EmptyStackError):
            calc.pop()

    def test_peek_empty_stack_error(self):
        """Test error when peeking empty stack."""
        calc = UPNCalculator()
        with pytest.raises(EmptyStackError):
            calc.peek()


class TestEdgeCases:
    """Tests for edge cases."""

    def test_zero_operations(self):
        """Test operations with zero."""
        calc = UPNCalculator()
        result = calc.evaluate("0 5 +")
        assert result == 5.0

    def test_negative_operands(self):
        """Test operations with negative operands."""
        calc = UPNCalculator()
        result = calc.evaluate("-10 -5 +")
        assert result == -15.0

    def test_mixed_operations(self):
        """Test mixed positive and negative operands."""
        calc = UPNCalculator()
        result = calc.evaluate("-5 10 +")
        assert result == 5.0

    def test_long_expression(self):
        """Test longer expression: ((2+3)*4-5)/3 = (20-5)/3 ≈ 5."""
        calc = UPNCalculator()
        result = calc.evaluate("2 3 + 4 * 5 - 3 /")
        assert pytest.approx(result, abs=1e-10) == 5.0
