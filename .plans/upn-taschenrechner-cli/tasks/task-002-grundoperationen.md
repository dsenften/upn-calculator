# Task-002: Grundoperationen (+, -, *, /)

## Metadata
- **ID**: task-002
- **Status**: in_progress
- **Priority**: must
- **Estimate**: 3 Story Points
- **Labels**: [core, math, critical]
- **Assignee**: `python-expert`
- **Created**: 28. November 2025
- **Updated**: 28. November 2025

## Description

Implementiere die **vier Grundrechenarten** (Addition, Subtraktion, Multiplikation, Division) als UPN-Operationen, die auf dem UPN-Parser aus task-001 aufbauen.

**Anforderung**: Diese Operationen sind Must-Have und Foundation für alle Berechnungen. Sie müssen robust, schnell und mathematisch korrekt sein.

**User Story**: 
Als *Precise Peter* möchte ich `10 3 -` eingeben und `7.0` erhalten, damit ich schnelle mathematische Berechnungen im Terminal durchführe.

**Rationale**:
- Grundfunktionalität des Rechners
- Wird direkt vom Nutzer verwendet
- Muss mit UPN-Parser integriert sein
- Division by Zero Handling kritisch

## Acceptance Criteria

- [ ] **Addition**: `2 3 +` → `5.0`
- [ ] **Subtraktion**: `10 3 -` → `7.0` (nicht `-7.0`!)
- [ ] **Multiplikation**: `4 5 *` → `20.0`
- [ ] **Division**: `20 4 /` → `5.0`
- [ ] **Division by Zero**: `20 0 /` → Error mit Nachricht "Division by zero"
- [ ] **Negative Results**: `3 5 -` → `-2.0`
- [ ] **Float Precision**: `2.5 1.5 +` → `4.0` (exact)
- [ ] **Chained Operations**: `2 3 + 4 *` → `20.0`
- [ ] **Operator Integration**: Operatoren sind registriert im Parser
- [ ] **Test Coverage**: Mindestens 15 Unit-Tests
- [ ] **Performance**: Berechnung < 1ms für Standard-Operationen

## Dependencies

- **Requires**: task-001 (UPN Parser muss fertig sein)
- **Blocks**: task-004 (CLI REPL nutzt diese Operationen)

## Agent Recommendation

**Recommended Agent**: `python-expert`

**Rationale**: 
- Mathematische Operationen in Python
- Error-Handling für Division by Zero
- Integration mit bestehendem Parser

## Implementation Notes

### Operator-Registrierung

```python
# operators.py

def add(a: float, b: float) -> float:
    """Addition: a + b"""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtraction: a - b"""
    # WICHTIG: Reihenfolge! UPN: [a, b, -] means a - b
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiplication: a * b"""
    return a * b

def divide(a: float, b: float) -> float:
    """Division: a / b with zero check"""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# Operator-Mapping
OPERATORS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}
```

### Integration mit Parser

```python
# calculator.py (erweiterung zu task-001)

from operators import OPERATORS, add, subtract, multiply, divide

class UPNCalculator:
    def __init__(self):
        self.stack = []
        self.operators = OPERATORS
    
    def evaluate(self, expression: str) -> float:
        tokens = expression.split()
        
        for token in tokens:
            if self.is_number(token):
                self.stack.append(float(token))
            elif token in self.operators:
                if len(self.stack) < 2:
                    raise InsufficientOperandsError(f"Operator '{token}' needs 2 operands")
                
                b = self.stack.pop()
                a = self.stack.pop()
                
                try:
                    result = self.operators[token](a, b)
                    self.stack.append(result)
                except ZeroDivisionError as e:
                    raise ZeroDivisionError(f"Division by zero in operation: {a} / {b}") from e
            else:
                raise InvalidTokenError(f"Unknown token: '{token}'")
        
        if len(self.stack) != 1:
            raise InvalidExpressionError(f"Invalid expression: stack has {len(self.stack)} elements, expected 1")
        
        return self.stack[0]
    
    @staticmethod
    def is_number(token: str) -> bool:
        try:
            float(token)
            return True
        except ValueError:
            return False
```

### Datei-Struktur Update

```
upn_calculator/
├── __init__.py
├── calculator.py          # UPNCalculator class
├── parser.py             # Tokenize & Parsing functions
├── operators.py          # ← NEW: Operator definitions ← task-002
├── errors.py             # Custom Exception classes
└── tests/
    ├── __init__.py
    └── test_operators.py  # ← NEW: Tests für task-002
```

## Testing Strategy

### Unit Tests (mindestens 15)

```python
# test_operators.py

import pytest
from upn_calculator import UPNCalculator
from upn_calculator.errors import ZeroDivisionError

class TestAddition:
    def test_simple_addition(self):
        calc = UPNCalculator()
        assert calc.evaluate("2 3 +") == 5.0
    
    def test_addition_negative(self):
        calc = UPNCalculator()
        assert calc.evaluate("-5 3 +") == -2.0
    
    def test_addition_float(self):
        calc = UPNCalculator()
        assert calc.evaluate("2.5 1.5 +") == 4.0

class TestSubtraction:
    def test_simple_subtraction(self):
        calc = UPNCalculator()
        assert calc.evaluate("10 3 -") == 7.0
    
    def test_subtraction_negative_result(self):
        calc = UPNCalculator()
        assert calc.evaluate("3 5 -") == -2.0
    
    def test_subtraction_order_matters(self):
        """UPN: [a, b, -] means a - b, not b - a"""
        calc = UPNCalculator()
        assert calc.evaluate("5 3 -") == 2.0
        assert calc.evaluate("3 5 -") == -2.0

class TestMultiplication:
    def test_simple_multiplication(self):
        calc = UPNCalculator()
        assert calc.evaluate("4 5 *") == 20.0
    
    def test_multiplication_by_zero(self):
        calc = UPNCalculator()
        assert calc.evaluate("100 0 *") == 0.0
    
    def test_multiplication_float(self):
        calc = UPNCalculator()
        assert calc.evaluate("2.5 4 *") == 10.0

class TestDivision:
    def test_simple_division(self):
        calc = UPNCalculator()
        assert calc.evaluate("20 4 /") == 5.0
    
    def test_division_float_result(self):
        calc = UPNCalculator()
        assert calc.evaluate("1 2 /") == 0.5
    
    def test_division_by_zero(self):
        calc = UPNCalculator()
        with pytest.raises(ZeroDivisionError):
            calc.evaluate("20 0 /")

class TestChainedOperations:
    def test_three_operands(self):
        calc = UPNCalculator()
        assert calc.evaluate("2 3 + 4 *") == 20.0
    
    def test_complex_chain(self):
        calc = UPNCalculator()
        # (10 - 3) * 2 = 14
        assert calc.evaluate("10 3 - 2 *") == 14.0

class TestErrorHandling:
    def test_division_by_zero_error_message(self):
        calc = UPNCalculator()
        with pytest.raises(ZeroDivisionError) as exc_info:
            calc.evaluate("20 0 /")
        assert "Division by zero" in str(exc_info.value)
```

### Performance Tests

```python
import timeit

def test_performance():
    calc = UPNCalculator()
    
    # Durchschnittliche Ausführungszeit sollte < 1ms sein
    time = timeit.timeit(
        lambda: calc.evaluate("2 3 +"),
        number=1000
    )
    
    assert time < 1.0  # 1000 iterations < 1 second = < 1ms per iteration
```

## Edge Cases

1. **Sehr große Zahlen**:
   - `1e100 1e100 +` → `2e100`
   - Risk: Overflow
   - Mitigation: IEEE 754 erlaubt diese

2. **Sehr kleine Zahlen**:
   - `1e-100 1e-100 +` → `2e-100`
   - Risk: Underflow
   - Mitigation: Python handhab dies

3. **Negative Zahlen als Operand**:
   - `-10 -3 +` → `-13`
   - `-10 -3 -` → `-7` (wichtig: -10 - (-3) = -7)

4. **Division-Spezialfälle**:
   - `0 5 /` → `0.0` (OK)
   - `5 0 /` → Error (ZeroDivisionError)
   - `0 0 /` → Error (ZeroDivisionError)

## Notes

**Referenced PRD Sections**:
- [FR-2: Vier Grundoperationen](../../PRD.md#fr-2-vier-grundoperationen)
- [US-1.1: Grundarithmetik](../../PRD.md#us-11-grundarithmetik-mit-upn-must-have)

**Implementation Order**:
1. Implementiere `operators.py` mit 4 Funktionen
2. Registriere Operatoren im Parser
3. Schreibe Tests
4. Code Review

**Quality Checks**:
- [ ] Alle Tests bestanden
- [ ] Keine Pylint Warnungen
- [ ] Docstrings vollständig
- [ ] Error Messages aussagekräftig

---

**Status**: 🟡 Ready for Development (nach task-001)
**Next Task**: task-003 (Trigonometric Functions) → parallel möglich
**Estimated Completion**: 8. Dezember 2025 (3 SP nach task-001 fertig)
