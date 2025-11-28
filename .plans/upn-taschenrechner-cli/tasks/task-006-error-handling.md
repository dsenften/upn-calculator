# Task-006: Error Handling & User Feedback

## Metadata
- **ID**: task-006
- **Status**: pending
- **Priority**: must
- **Estimate**: 1 Story Point
- **Labels**: [core, error-handling, quality]
- **Assignee**: `python-expert`
- **Created**: 28. November 2025
- **Updated**: 28. November 2025

## Description

Implementiere **robustes Error Handling** für alle kritischen Pfade und zeige nutzer-freundliche Fehlermeldungen an, statt technischer Error-Traces.

**User Story**: 
Als *Efficient Elena* möchte ich bei einem Fehler eine klare Nachricht sehen (z.B. "Error: Division by zero"), damit ich mein Commando korrigieren kann, nicht verwirrt bin von Python Tracebacks.

**Rationale**:
- Professioneller, nutzerfreundlicher Calculator
- Verhindert Verwirrung durch technische Details
- Hilft Nutzern ihre Fehler zu verstehen und zu beheben
- Stabiles System (keine Crashes, graceful Error Recovery)

## Acceptance Criteria

- [ ] **Try/Except Abdeckung**: Alle kritischen Pfade haben Try/Except
- [ ] **User-friendly Messages**: Technische Errors werden benutzerverständlich übersetzt
- [ ] **No Tracebacks**: Kein Python Traceback an Nutzer sichtbar (nur in Dev-Mode)
- [ ] **Error Recovery**: Nach Error bleibt REPL aktiv, Loop setzt sich fort
- [ ] **Specific Error Types**: Verschiedene Fehlertypen haben spezifische Messages
  - Division by Zero
  - Insufficient Operands
  - Invalid Token
  - Invalid Expression
- [ ] **Keyboard Interrupt**: Ctrl+C wird gracefully gehandhabt
- [ ] **Error Messages**: Kurz, prägnant, actionable (< 100 chars)
- [ ] **Test Coverage**: Mindestens 8 Error-Handling Tests

## Dependencies

- **Requires**: task-001 through task-005 (alle vorherigen Tasks)
- **Blocks**: task-007 (Help-System bezieht sich auf Error-Messages)

## Agent Recommendation

**Recommended Agent**: `python-expert`

**Rationale**: 
- Python Exception Handling
- Try/Except Pattern
- User Experience Design für Fehlermeldungen

## Implementation Notes

### Exception Hierarchy

```python
# errors.py

class UPNCalculatorError(Exception):
    """Base exception for all calculator errors"""
    
    def __init__(self, message: str, suggestion: str = None):
        self.message = message
        self.suggestion = suggestion
        super().__init__(self.message)
    
    def get_user_message(self) -> str:
        """Get user-friendly error message"""
        msg = f"Error: {self.message}"
        if self.suggestion:
            msg += f"\nSuggestion: {self.suggestion}"
        return msg

class InvalidTokenError(UPNCalculatorError):
    """Raised when unknown token encountered"""
    pass

class InsufficientOperandsError(UPNCalculatorError):
    """Raised when operator has too few operands"""
    pass

class InvalidExpressionError(UPNCalculatorError):
    """Raised when expression structure is invalid"""
    pass

class ZeroDivisionError(UPNCalculatorError):
    """Raised on division by zero"""
    pass
```

### Error Handler im Calculator

```python
# calculator.py

from upn_calculator.errors import (
    UPNCalculatorError,
    InvalidTokenError,
    InsufficientOperandsError,
    InvalidExpressionError,
    ZeroDivisionError
)

class UPNCalculator:
    def evaluate(self, expression: str) -> float:
        """
        Evaluate UPN expression with comprehensive error handling.
        """
        try:
            tokens = expression.split()
            
            if not tokens:
                raise InvalidExpressionError(
                    "Empty expression",
                    "Enter at least one number or operation"
                )
            
            for token in tokens:
                if self.is_number(token):
                    self.stack.append(float(token))
                
                elif token in self.operators:
                    if len(self.stack) < 2:
                        raise InsufficientOperandsError(
                            f"Operator '{token}' requires 2 operands",
                            f"Stack has {len(self.stack)} element(s)"
                        )
                    
                    b = self.stack.pop()
                    a = self.stack.pop()
                    
                    try:
                        result = self.operators[token](a, b)
                        self.stack.append(result)
                    except ZeroDivisionError:
                        # Re-raise with context
                        raise ZeroDivisionError(
                            f"Cannot divide {a} by 0",
                            "Use non-zero divisor"
                        )
                
                elif token in self.functions:
                    if len(self.stack) < 1:
                        raise InsufficientOperandsError(
                            f"Function '{token}' requires 1 operand",
                            f"Stack is empty"
                        )
                    
                    angle = self.stack.pop()
                    result = self.functions[token](angle)
                    self.stack.append(result)
                
                else:
                    raise InvalidTokenError(
                        f"Unknown token: '{token}'",
                        "Use numbers, operators (+, -, *, /), or functions (sin, cos, tan)"
                    )
            
            if len(self.stack) != 1:
                raise InvalidExpressionError(
                    f"Invalid expression: {len(self.stack)} elements remain",
                    "Each expression should result in exactly 1 value"
                )
            
            return self.stack[0]
        
        except UPNCalculatorError:
            raise  # Re-raise known errors
        
        except Exception as e:
            # Catch unexpected errors
            raise UPNCalculatorError(
                "Unexpected error",
                f"Technical details: {str(e)}"
            )
```

### CLI Error Handling

```python
# cli.py

def main():
    calc = UPNCalculator()
    
    while True:
        try:
            user_input = input("> ").strip()
            
            if not user_input:
                continue
            
            # Commands
            if user_input.lower() in ('q', 'exit', 'quit'):
                print("Goodbye!")
                sys.exit(0)
            
            if user_input.lower() in ('stack', 's'):
                print(calc.display_stack())
                continue
            
            if user_input.lower() in ('clear', 'c'):
                calc.clear_stack()
                print("Stack cleared")
                continue
            
            if user_input.lower() == 'help':
                print_help()
                continue
            
            # Evaluate expression
            result = calc.evaluate(user_input)
            print(f"{result}")
        
        except KeyboardInterrupt:
            # Ctrl+C handling - graceful exit
            print("\n(Interrupted)")
            sys.exit(0)
        
        except UPNCalculatorError as e:
            # Known calculator errors - show user message
            print(e.get_user_message())
        
        except Exception as e:
            # Unexpected errors - generic message
            print(f"Error: An unexpected error occurred")
            if "--debug" in sys.argv:
                print(f"Technical: {str(e)}")
            else:
                print(f"(Use --debug flag to see technical details)")

def print_help():
    # ... help text ...
    pass

if __name__ == "__main__":
    main()
```

### Error Message Beispiele

```
User: 2 +
Error: Operator '+' requires 2 operands
Suggestion: Stack has 1 element(s)

User: 2 xyz 3
Error: Unknown token: 'xyz'
Suggestion: Use numbers, operators (+, -, *, /), or functions (sin, cos, tan)

User: 20 0 /
Error: Cannot divide 20 by 0
Suggestion: Use non-zero divisor

User: 2 3 4 +
Error: Invalid expression: 2 elements remain
Suggestion: Each expression should result in exactly 1 value

User: (Ctrl+C)
(Interrupted)
```

## Testing Strategy

### Error Handling Tests (mindestens 8)

```python
# test_error_handling.py

import pytest
from upn_calculator import UPNCalculator
from upn_calculator.errors import (
    InvalidTokenError,
    InsufficientOperandsError,
    InvalidExpressionError,
    ZeroDivisionError
)

class TestErrorMessages:
    def test_division_by_zero_error(self):
        calc = UPNCalculator()
        with pytest.raises(ZeroDivisionError) as exc:
            calc.evaluate("20 0 /")
        
        assert "divide" in str(exc.value).lower()
        assert "0" in str(exc.value)
    
    def test_insufficient_operands_for_operator(self):
        calc = UPNCalculator()
        with pytest.raises(InsufficientOperandsError) as exc:
            calc.evaluate("2 +")
        
        assert "requires 2" in str(exc.value).lower()
    
    def test_insufficient_operands_for_function(self):
        calc = UPNCalculator()
        with pytest.raises(InsufficientOperandsError) as exc:
            calc.evaluate("sin")
        
        assert "requires 1" in str(exc.value).lower()
    
    def test_invalid_token(self):
        calc = UPNCalculator()
        with pytest.raises(InvalidTokenError) as exc:
            calc.evaluate("2 xyz +")
        
        assert "xyz" in str(exc.value)
        assert "unknown" in str(exc.value).lower()
    
    def test_too_many_operands(self):
        calc = UPNCalculator()
        with pytest.raises(InvalidExpressionError) as exc:
            calc.evaluate("2 3 4 +")
        
        assert "2 elements" in str(exc.value) or "elements remain" in str(exc.value).lower()
    
    def test_empty_expression(self):
        calc = UPNCalculator()
        with pytest.raises(InvalidExpressionError) as exc:
            calc.evaluate("")
        
        assert "empty" in str(exc.value).lower()

class TestErrorRecovery:
    def test_error_does_not_corrupt_state(self):
        """Nach Error sollte Calculator noch funktionieren"""
        calc = UPNCalculator()
        
        # Erfolgreiche Operation
        result1 = calc.evaluate("2 3 +")
        assert result1 == 5.0
        
        # Fehlgeschlagene Operation (aber Stack ist jetzt leer)
        calc.clear_stack()
        
        try:
            calc.evaluate("2 +")  # Insufficient operands
        except InsufficientOperandsError:
            pass  # Expected
        
        # Calculator sollte noch funktionieren
        calc.clear_stack()
        result2 = calc.evaluate("10 5 -")
        assert result2 == 5.0

class TestErrorMessages:
    def test_error_message_not_too_long(self):
        """Error-Nachrichten sollten kurz und prägnant sein"""
        calc = UPNCalculator()
        
        try:
            calc.evaluate("xyz")
        except InvalidTokenError as e:
            msg = str(e)
            assert len(msg) < 150  # Reasonable limit
```

## Usage Examples

```
$ python -m upn_calculator
UPN Calculator v1.0

> 2 +
Error: Operator '+' requires 2 operands
Suggestion: Stack has 1 element(s)

> 2 3 +
5.0

> 20 0 /
Error: Cannot divide 20 by 0
Suggestion: Use non-zero divisor

> 2 xyz 3
Error: Unknown token: 'xyz'
Suggestion: Use numbers, operators (+, -, *, /), or functions (sin, cos, tan)

> ^C
(Interrupted)
```

## Notes

**Referenced PRD Sections**:
- [FR-6: Error Handling & User Feedback](../../PRD.md#fr-6-error-handling-mit-aussagekräftigen-meldungen)
- [NFR-3: Intuitive Bedienung](../../PRD.md#nfr-3-intuitive-bedienung-ohne-onboarding)

**Design Principles**:
1. **Nutzer-freundlich**: Keine technischen Python Tracebacks
2. **Actionable**: Fehler-Messages sind hilfreich, nicht kryptisch
3. **Kurz**: < 100 Zeichen pro Error
4. **Recoverable**: Nach Error kann Nutzer weitermachen

**Debug-Mode**:
```bash
python -m upn_calculator --debug
```
Zeigt technische Details für Entwickler

---

**Status**: 🟡 Ready for Development (nach task-005)
**Next Task**: task-007 (Help-System) - abhängig von task-006
**Estimated Completion**: 20. Dezember 2025 (1 SP nach Stack-Task)
