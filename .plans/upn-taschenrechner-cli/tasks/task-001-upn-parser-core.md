# Task-001: UPN-Parser Core Implementation

## Metadata
- **ID**: task-001
- **Status**: pending
- **Priority**: must
- **Estimate**: 3 Story Points
- **Labels**: [core, parser, critical]
- **Assignee**: `python-expert`
- **Created**: 28. November 2025
- **Updated**: 28. November 2025

## Description

Implementiere den **Stack-basierten UPN-Parser und Evaluator**, die Kernkomponente des Taschenrechners. Dieser Parser liest Eingaben in Umgekehrter Polnischer Notation (UPN) und evaluiert sie mit einem Stack-Algorithmus.

**UPN-Basis**: 
- Operanden vor Operatoren: `2 3 +` statt `2 + 3`
- Keine Klammern nötig
- Stack-Algorithmus: Operanden auf Stack pushen, bei Operator: Operanden poppen, berechnen, Resultat pushen

**User Story**: 
Als *Efficient Elena* möchte ich dass einfache UPN-Ausdrücke wie `2 3 +` zu `5.0` evaluiert werden, damit ich Berechnungen präzise eingeben kann.

**Rationale**:
- Foundation für alle anderen Features
- Wird von Grundoperationen, Trig-Funktionen und CLI benötigt
- Muss robust und fehlerbehandelt sein von Anfang an

## Acceptance Criteria

- [ ] **Basic Parsing**: String-Input wird in Token zerlegt (whitespace-separator)
- [ ] **Numeric Token Recognition**: Zahlen (Integer & Float) korrekt erkannt
  - Beispiele: `2`, `3.14`, `-5`, `1e-10`
- [ ] **Operator Token Recognition**: Operatoren (+, -, *, /) identifiziert
- [ ] **Stack Implementation**: Stack-Datenstruktur funktioniert (Push, Pop, Peek)
- [ ] **Stack Evaluation Algorithm**: 
  - Zahl-Token → Push to Stack
  - Operator-Token → Pop 2 Operanden, berechne, Push Resultat
- [ ] **Valid Expression**: Nach Evaluation genau 1 Element im Stack (das Resultat)
- [ ] **Error: Invalid Token**: Unbekannte Token werfen aussagekräftigen Error
- [ ] **Error: Insufficient Operands**: Zu wenige Operanden für Operator werfen Error
- [ ] **Float Precision**: Resultat als Float mit IEEE 754 Precision (64-bit)
- [ ] **Test Coverage**: Mindestens 20 Unit-Tests für diverse Szenarien
- [ ] **Code Quality**: Keine Pylint-Warnungen, Docstrings für Funktionen

## Dependencies

- **Requires**: None (Foundation Task)
- **Blocks**: task-002, task-003, task-004, task-005

**Critical Path**: YES - Dieses Task blockiert alle anderen Features

## Agent Recommendation

**Recommended Agent**: `python-expert`

**Rationale**: 
- Python-Stack-Datenstruktur und Parsing erforderlich
- Fehlerbehandlung und Validierung zentral
- Unit-Testing in pytest

## Implementation Notes

### Architektur-Ansatz

```python
# Pseudo-Code

class UPNCalculator:
    def __init__(self):
        self.stack = []
    
    def evaluate(self, expression: str) -> float:
        tokens = expression.split()
        for token in tokens:
            if is_number(token):
                self.stack.append(float(token))
            elif is_operator(token):
                if len(self.stack) < 2:
                    raise InsufficientOperandsError(token)
                b = self.stack.pop()
                a = self.stack.pop()
                result = apply_operator(a, b, token)
                self.stack.append(result)
            else:
                raise InvalidTokenError(token)
        
        if len(self.stack) != 1:
            raise InvalidExpressionError("Stack muss genau 1 Element enthalten")
        
        return self.stack[0]
    
    def clear_stack(self):
        self.stack = []
    
    def get_stack(self) -> list:
        return self.stack.copy()
```

### Key Funktionen

**1. Token-Parsing**:
```python
def tokenize(expression: str) -> List[str]:
    """Split expression by whitespace, handle edge cases"""
    return expression.split()

def is_number(token: str) -> bool:
    """Check if token is valid number (int or float)"""
    try:
        float(token)
        return True
    except ValueError:
        return False
```

**2. Operator-Handling**:
```python
OPERATORS = {'+', '-', '*', '/'}

def apply_operator(a: float, b: float, op: str) -> float:
    """Apply operator to two operands"""
    if op == '+':
        return a + b
    elif op == '-':
        return a - b  # Wichtig: Reihenfolge! a - b, nicht b - a
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Division durch Null")
        return a / b
```

**3. Stack-Management**:
```python
def push(self, value: float):
    """Add value to stack"""
    self.stack.append(value)

def pop(self) -> float:
    """Remove and return top of stack"""
    if not self.stack:
        raise EmptyStackError("Stack ist leer")
    return self.stack.pop()

def get_stack(self) -> List[float]:
    """Get copy of current stack"""
    return self.stack.copy()
```

### Datei-Struktur

```
upn_calculator/
├── __init__.py
├── calculator.py          # UPNCalculator class
├── parser.py             # Tokenize & Parsing functions
├── operators.py          # Operator definitions & application
└── errors.py             # Custom Exception classes
```

### Fehlerklassen

```python
# errors.py

class UPNCalculatorError(Exception):
    """Base error class"""
    pass

class InvalidTokenError(UPNCalculatorError):
    """Raised when unknown token encountered"""
    pass

class InsufficientOperandsError(UPNCalculatorError):
    """Raised when operator has too few operands"""
    pass

class InvalidExpressionError(UPNCalculatorError):
    """Raised when expression is invalid overall"""
    pass

class ZeroDivisionError(UPNCalculatorError):
    """Raised on division by zero"""
    pass
```

### Reihenfolge-Wichtigkeit (Operator-Assoziativität)

**Kritisch**: Stack ist LIFO, d.h. bei `a b -` wird zuerst b gepopped, dann a:

```
Stack: [a, b] ← top
pop b
pop a
result = a - b  ✅ RICHTIG (nicht b - a)
```

Beispiel: `10 3 -` sollte `7.0` sein, nicht `-7.0`

## Testing Strategy

### Unit Tests (mindestens 20)

```python
# test_calculator.py

import pytest
from upn_calculator import UPNCalculator

class TestBasicOperations:
    
    def test_addition(self):
        calc = UPNCalculator()
        result = calc.evaluate("2 3 +")
        assert result == 5.0
    
    def test_subtraction(self):
        calc = UPNCalculator()
        result = calc.evaluate("10 3 -")
        assert result == 7.0
    
    def test_negative_numbers(self):
        calc = UPNCalculator()
        result = calc.evaluate("-5 3 +")
        assert result == -2.0
    
    def test_float_numbers(self):
        calc = UPNCalculator()
        result = calc.evaluate("2.5 1.5 +")
        assert result == 4.0
    
    def test_chained_operations(self):
        calc = UPNCalculator()
        result = calc.evaluate("2 3 + 4 *")
        assert result == 20.0

class TestErrorHandling:
    
    def test_invalid_token(self):
        calc = UPNCalculator()
        with pytest.raises(InvalidTokenError):
            calc.evaluate("2 3 xyz +")
    
    def test_insufficient_operands(self):
        calc = UPNCalculator()
        with pytest.raises(InsufficientOperandsError):
            calc.evaluate("2 +")
    
    def test_too_many_operands(self):
        calc = UPNCalculator()
        with pytest.raises(InvalidExpressionError):
            calc.evaluate("2 3 4 +")

class TestStackManagement:
    
    def test_get_stack(self):
        calc = UPNCalculator()
        calc.evaluate("2 3 +")
        assert calc.get_stack() == [5.0]
    
    def test_clear_stack(self):
        calc = UPNCalculator()
        calc.evaluate("2 3 +")
        calc.clear_stack()
        assert calc.get_stack() == []
```

### Edge Cases

- Sehr große Zahlen: `1e100 2e100 +`
- Sehr kleine Zahlen: `1e-100 2e-100 +`
- Negative Zahlen: `-10 -5 +`
- Dezimalzahlen mit vielen Stellen: `3.14159265358979 2.71828182845905 +`

## Notes

**Referenced PRD Sections**:
- [Funktionale Anforderungen - FR-1: UPN-Parsing](../../PRD.md#fr-1-upn-parsing-und-evaluation)
- [User Stories - US-1.1](../../PRD.md#us-11-grundarithmetik-mit-upn-must-have)

**Potential Challenges**:

1. **Floating-Point Precision**: IEEE 754 hat Grenzen
   - Lösung: Tests mit Toleranz (abs(result - expected) < 1e-10)

2. **Negative Zahlen Parsing**: `-5` ist negative Zahl, nicht minus-Operator
   - Lösung: `is_number()` mit float() Try/Except

3. **Operator-Reihenfolge**: Stack ist LIFO, muss Reihenfolge richtig beachten
   - Lösung: Code-Review, umfangreiche Tests

4. **Edge-Case bei Division**: `20 0 /` muss zu aussagekräftigem Error führen
   - Lösung: Expliziter Check vor Division

**Future Enhancements** (Post-MVP):
- Support für Funktionen (sin, cos, tan) - siehe task-003
- Support für Konstanten (pi, e)
- Support für Variable & Memory

---

**Status**: 🟡 Ready for Development
**Next Task**: task-002 (Grundoperationen) → parallel nach task-001 fertig
**Estimated Completion**: 4. Dezember 2025 (3 SP @ 1 SP/Tag)
