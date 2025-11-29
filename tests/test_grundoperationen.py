"""Integration and acceptance tests for task-002: Grundoperationen."""

import pytest

from upn_calculator import (
    UPNCalculator,
    ZeroDivisionError,
)


class TestAddition:
    """Tests for addition operator (AC 1)."""

    def test_addition_simple(self):
        """Test: 2 3 + → 5.0"""
        calc = UPNCalculator()
        result = calc.evaluate("2 3 +")
        assert result == 5.0

    def test_addition_floats(self):
        """Test addition with floats."""
        calc = UPNCalculator()
        result = calc.evaluate("2.5 3.7 +")
        assert pytest.approx(result, abs=1e-10) == 6.2

    def test_addition_multiple(self):
        """Test multiple additions: 1 2 + 3 + = 6"""
        calc = UPNCalculator()
        result = calc.evaluate("1 2 + 3 +")
        assert result == 6.0


class TestSubtraction:
    """Tests for subtraction operator (AC 2)."""

    def test_subtraction_simple(self):
        """Test: 10 3 - → 7.0 (NOT -7.0!)"""
        calc = UPNCalculator()
        result = calc.evaluate("10 3 -")
        assert result == 7.0

    def test_subtraction_order_matters(self):
        """Test that subtraction order is correct."""
        calc = UPNCalculator()
        result = calc.evaluate("3 10 -")
        assert result == -7.0

    def test_subtraction_floats(self):
        """Test subtraction with floats."""
        calc = UPNCalculator()
        result = calc.evaluate("5.5 2.3 -")
        assert pytest.approx(result, abs=1e-10) == 3.2


class TestMultiplication:
    """Tests for multiplication operator (AC 3)."""

    def test_multiplication_simple(self):
        """Test: 4 5 * → 20.0"""
        calc = UPNCalculator()
        result = calc.evaluate("4 5 *")
        assert result == 20.0

    def test_multiplication_by_zero(self):
        """Test multiplication by zero."""
        calc = UPNCalculator()
        result = calc.evaluate("100 0 *")
        assert result == 0.0

    def test_multiplication_floats(self):
        """Test multiplication with floats."""
        calc = UPNCalculator()
        result = calc.evaluate("2.5 4.0 *")
        assert result == 10.0


class TestDivision:
    """Tests for division operator (AC 4, 5)."""

    def test_division_simple(self):
        """Test: 20 4 / → 5.0"""
        calc = UPNCalculator()
        result = calc.evaluate("20 4 /")
        assert result == 5.0

    def test_division_floats(self):
        """Test division with floats."""
        calc = UPNCalculator()
        result = calc.evaluate("10.0 2.5 /")
        assert result == 4.0

    def test_division_by_zero_error(self):
        """Test: 20 0 / → Error (AC 5)"""
        calc = UPNCalculator()
        with pytest.raises(ZeroDivisionError):
            calc.evaluate("20 0 /")

    def test_division_order_matters(self):
        """Test that division order is correct (20 / 4 = 5, not 0.2)."""
        calc = UPNCalculator()
        result = calc.evaluate("20 4 /")
        assert result == 5.0

        calc2 = UPNCalculator()
        result2 = calc2.evaluate("4 20 /")
        assert pytest.approx(result2, abs=1e-10) == 0.2


class TestNegativeResults:
    """Tests for negative results (AC 6)."""

    def test_subtraction_negative_result(self):
        """Test: 3 5 - → -2.0"""
        calc = UPNCalculator()
        result = calc.evaluate("3 5 -")
        assert result == -2.0

    def test_multiplication_negative(self):
        """Test: -5 3 * → -15.0"""
        calc = UPNCalculator()
        result = calc.evaluate("-5 3 *")
        assert result == -15.0

    def test_division_negative(self):
        """Test: -20 4 / → -5.0"""
        calc = UPNCalculator()
        result = calc.evaluate("-20 4 /")
        assert result == -5.0


class TestFloatPrecision:
    """Tests for float precision (AC 7)."""

    def test_addition_precision(self):
        """Test: 2.5 1.5 + → 4.0 (exact)"""
        calc = UPNCalculator()
        result = calc.evaluate("2.5 1.5 +")
        assert result == 4.0

    def test_subtraction_precision(self):
        """Test subtraction precision."""
        calc = UPNCalculator()
        result = calc.evaluate("5.5 2.25 -")
        assert pytest.approx(result, abs=1e-10) == 3.25

    def test_division_precision(self):
        """Test division precision."""
        calc = UPNCalculator()
        result = calc.evaluate("1.0 3.0 /")
        assert pytest.approx(result, abs=1e-15) == 1.0 / 3.0


class TestChainedOperations:
    """Tests for chained operations (AC 8)."""

    def test_chained_mixed(self):
        """Test: 2 3 + 4 * → 20.0 (AC 8)"""
        calc = UPNCalculator()
        result = calc.evaluate("2 3 + 4 *")
        assert result == 20.0

    def test_chained_long(self):
        """Test: (10 - 3) * 2 = 14"""
        calc = UPNCalculator()
        result = calc.evaluate("10 3 - 2 *")
        assert result == 14.0

    def test_chained_division_sequence(self):
        """Test: 100 2 / 5 / = 10"""
        calc = UPNCalculator()
        result = calc.evaluate("100 2 / 5 /")
        assert result == 10.0


class TestOperatorIntegration:
    """Tests for operator integration (AC 9)."""

    def test_all_operators_in_expression(self):
        """Test: 2 3 + 4 * 5 - 2 / = ((2+3)*4-5)/2 = 7.5"""
        calc = UPNCalculator()
        result = calc.evaluate("2 3 + 4 * 5 - 2 /")
        assert pytest.approx(result, abs=1e-10) == 7.5

    def test_operators_registered(self):
        """Test that operators are properly registered."""
        calc = UPNCalculator()
        # Each operator should work
        ops_test = [
            ("2 3 +", 5.0),
            ("10 3 -", 7.0),
            ("4 5 *", 20.0),
            ("20 4 /", 5.0),
        ]
        for expr, expected in ops_test:
            calc.clear_stack()
            result = calc.evaluate(expr)
            assert result == expected


class TestPerformance:
    """Tests for performance requirements (AC 11 - implicit)."""

    def test_simple_operation_performance(self):
        """Test that simple operations are fast."""
        import time

        calc = UPNCalculator()

        start = time.time()
        for _ in range(1000):
            calc.clear_stack()
            calc.evaluate("2 3 +")
        elapsed = (time.time() - start) * 1000  # Convert to ms

        # Should complete 1000 operations in less than 1000ms (1ms each)
        assert elapsed < 1000, f"1000 operations took {elapsed}ms, expected < 1000ms"


class TestEdgeCases:
    """Tests for edge cases."""

    def test_very_large_numbers(self):
        """Test with very large numbers."""
        calc = UPNCalculator()
        result = calc.evaluate("1e100 2e100 +")
        assert pytest.approx(result, rel=1e-14) == 3e100

    def test_very_small_numbers(self):
        """Test with very small numbers."""
        calc = UPNCalculator()
        result = calc.evaluate("1e-100 2e-100 +")
        assert pytest.approx(result, abs=1e-115) == 3e-100

    def test_negative_and_positive_mix(self):
        """Test mixing negative and positive numbers."""
        calc = UPNCalculator()
        result = calc.evaluate("-10 20 +")
        assert result == 10.0

    def test_zero_operations(self):
        """Test operations with zero."""
        calc = UPNCalculator()
        assert calc.evaluate("0 5 +") == 5.0
        assert calc.evaluate("10 0 -") == 10.0
        assert calc.evaluate("0 5 *") == 0.0
        assert calc.evaluate("0 5 /") == 0.0
