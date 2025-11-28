# Task-004: CLI REPL Interface

## Metadata
- **ID**: task-004
- **Status**: pending
- **Priority**: must
- **Estimate**: 2 Story Points
- **Labels**: [core, cli, interface]
- **Assignee**: `python-expert`
- **Created**: 28. November 2025
- **Updated**: 28. November 2025

## Description

Implementiere die **Interaktive Command-Line REPL** (Read-Eval-Print-Loop), die Nutzer-Eingaben entgegennimmt, durch den UPN-Calculator verarbeitet und Resultate anzeigt.

**User Story**: 
Als *Learning Luis* möchte ich den Rechner starten, `2 3 +` eingeben und `5.0` sehen, damit ich intuitiv mathematische Berechnungen durchführe.

**Rationale**:
- Primärer Zugang für Nutzer zum Tool
- Muss stabil, responsive und fehlerbehandelt sein
- Integriert alle bisherigen Tasks (Parser, Math Ops, Trig Functions)

## Acceptance Criteria

- [ ] **Startup-Message**: Zeigt Title und Version
- [ ] **Prompt**: `> ` wird angezeigt für Nutzer-Eingabe
- [ ] **Input Processing**: Eingabe wird gelesen und an Calculator übergeben
- [ ] **Output Display**: Resultat wird angezeigt (z.B. `5.0`)
- [ ] **Loop**: Nach jedem Kommando bleibt Loop aktiv
- [ ] **Exit Command**: `q` oder `exit` beendet das Programm gracefully
- [ ] **Ctrl+C Handling**: Ctrl+C beendet Program ohne Error-Trace
- [ ] **Help Command**: `help` zeigt Dokumentation (optional für task-004, main in task-007)
- [ ] **Error Recovery**: Nach Error bleibt Loop aktiv, kein Crash
- [ ] **Stack Persistence**: Stack bleibt über mehrere Eingaben hinweg
- [ ] **Test Coverage**: Mindestens 10 Integration Tests

## Dependencies

- **Requires**: task-001, task-002, task-003 (alle Math-Features)
- **Blocks**: task-005, task-006 (CLI wird als Basis benötigt)

## Agent Recommendation

**Recommended Agent**: `python-expert`

**Rationale**: 
- Python CLI-Entwicklung mit Input/Output Handling
- Error Handling und Exception Management
- Integration mit bestehendem Calculator

## Implementation Notes

### REPL Loop Struktur

```python
# cli.py

import sys
from upn_calculator import UPNCalculator

def main():
    """Main REPL entry point"""
    print("=" * 40)
    print("UPN Calculator v1.0")
    print("Type 'help' for commands")
    print("=" * 40)
    
    calc = UPNCalculator()
    
    while True:
        try:
            # Read
            user_input = input("> ").strip()
            
            # Empty input
            if not user_input:
                continue
            
            # Commands
            if user_input.lower() in ('q', 'exit', 'quit'):
                print("Goodbye!")
                sys.exit(0)
            
            if user_input.lower() == 'help':
                print_help()
                continue
            
            if user_input.lower() in ('stack', 's'):
                stack = calc.get_stack()
                print(f"Stack: {stack}")
                continue
            
            if user_input.lower() in ('clear', 'c'):
                calc.clear_stack()
                print("Stack cleared")
                continue
            
            # Eval - evaluate mathematical expression
            result = calc.evaluate(user_input)
            
            # Print
            print(f"{result}")
        
        except KeyboardInterrupt:
            print("\n(Interrupted)")
            sys.exit(0)
        
        except ValueError as e:
            print(f"Error: {e}")
        
        except Exception as e:
            print(f"Error: {str(e)}")
            # Don't exit, loop continues

def print_help():
    """Print help message"""
    help_text = """
UPN Calculator Help
===================

Basic Operations:
  +    Addition: 2 3 + → 5
  -    Subtraction: 10 3 - → 7
  *    Multiplication: 4 5 * → 20
  /    Division: 20 4 / → 5

Trigonometric (in radians):
  sin  Sine: 1.5707963267948966 sin → 1
  cos  Cosine: 0 cos → 1
  tan  Tangent: 0.7853981633974483 tan → 1

Commands:
  stack    Display current stack
  clear    Clear the stack
  help     Show this help
  q/exit   Exit calculator

Examples:
  > 2 3 +
  5.0
  > 4 *
  20.0
  > stack
  [20.0]
  > clear
  Stack cleared
  > q
  Goodbye!
"""
    print(help_text)

if __name__ == "__main__":
    main()
```

### Einstiegspunkt (main.py oder __main__.py)

```python
# upn_calculator/__main__.py

from upn_calculator.cli import main

if __name__ == "__main__":
    main()
```

Ermöglicht sowohl:
```bash
python -m upn_calculator
python cli.py
```

### Error Handling Strategy

```python
# error-handling.py

# Verschiedene Error-Typen und User-Nachrichten

class ErrorHandler:
    """Handle verschiedene Exception-Typen mit User-freundlichen Messages"""
    
    @staticmethod
    def handle(exception: Exception) -> str:
        """Convert exception to user-friendly message"""
        
        if isinstance(exception, ZeroDivisionError):
            return "Error: Division by zero"
        
        elif isinstance(exception, InvalidTokenError):
            return f"Error: Unknown token. Type 'help' for commands"
        
        elif isinstance(exception, InsufficientOperandsError):
            return f"Error: Not enough operands for operation"
        
        elif isinstance(exception, InvalidExpressionError):
            return f"Error: Invalid expression"
        
        else:
            return f"Error: {str(exception)}"
```

### Datei-Struktur Update

```
upn_calculator/
├── __init__.py
├── __main__.py           # ← NEW: Entry point für CLI
├── calculator.py
├── parser.py
├── operators.py
├── math_functions.py
├── errors.py
├── cli.py               # ← NEW: REPL implementation (task-004)
└── tests/
    ├── test_operators.py
    ├── test_math_functions.py
    └── test_cli.py       # ← NEW: CLI tests
```

## Testing Strategy

### Integration Tests (mindestens 10)

```python
# test_cli.py

import pytest
from io import StringIO
import sys
from upn_calculator.cli import main
from upn_calculator import UPNCalculator

class TestREPLBasic:
    def test_simple_calculation_in_loop(self):
        calc = UPNCalculator()
        
        # Simuliere: 2 3 +
        result = calc.evaluate("2 3 +")
        assert result == 5.0
    
    def test_stack_persistence(self):
        """Stack sollte über mehrere Eingaben hinweg bestehen"""
        calc = UPNCalculator()
        
        # Eingabe 1: 2 3 +
        result1 = calc.evaluate("2 3 +")
        assert result1 == 5.0
        assert calc.get_stack() == [5.0]
        
        # Eingabe 2: 4 *
        result2 = calc.evaluate("4 *")
        assert result2 == 20.0
        assert calc.get_stack() == [20.0]

class TestREPLCommands:
    def test_stack_command(self):
        calc = UPNCalculator()
        calc.evaluate("2 3 +")
        
        stack = calc.get_stack()
        assert stack == [5.0]
    
    def test_clear_command(self):
        calc = UPNCalculator()
        calc.evaluate("2 3 +")
        calc.clear_stack()
        
        assert calc.get_stack() == []

class TestREPLErrorHandling:
    def test_error_does_not_crash(self):
        """Nach Error sollte REPL noch funktionieren"""
        calc = UPNCalculator()
        
        # Führe Error aus
        try:
            calc.evaluate("2 +")  # Insufficient operands
        except Exception:
            pass  # Expected
        
        # REPL sollte noch funktionieren
        result = calc.evaluate("3 4 +")
        assert result == 7.0
    
    def test_division_by_zero_error(self):
        calc = UPNCalculator()
        
        with pytest.raises(ZeroDivisionError):
            calc.evaluate("5 0 /")

class TestREPLIntegration:
    def test_complex_calculation_sequence(self):
        """Simuliere typische User-Session"""
        calc = UPNCalculator()
        
        # Session:
        # > 10 5 -
        # 5.0
        # > 2 *
        # 10.0
        # > stack
        # [10.0]
        # > clear
        # > 0 sin
        # 0.0
        
        r1 = calc.evaluate("10 5 -")
        assert r1 == 5.0
        
        r2 = calc.evaluate("2 *")
        assert r2 == 10.0
        
        stack = calc.get_stack()
        assert stack == [10.0]
        
        calc.clear_stack()
        assert calc.get_stack() == []
        
        r3 = calc.evaluate("0 sin")
        assert r3 == 0.0
```

## Usage Examples

```
$ python -m upn_calculator
========================================
UPN Calculator v1.0
Type 'help' for commands
========================================

> 2 3 +
5.0

> 4 *
20.0

> stack
[20.0]

> 10 3 -
7.0

> 0 sin
0.0

> help
UPN Calculator Help
===================
...

> q
Goodbye!
```

## Notes

**Referenced PRD Sections**:
- [FR-4: Interaktive CLI-Interface](../../PRD.md#fr-4-interaktive-cli-interface)
- [User Experience & Bedienung](../../PRD.md#7-user-experience--bedienung)

**Keyboard Shortcuts** (optional, nice-to-have):
- Arrow-Up für History (task-010)
- Tab für Auto-Completion (Future)

**Graceful Exit Handling**:
- Ctrl+C sollte zu "Goodbye!" führen (nicht zu Traceback)
- `exit` / `q` Commands sollten cleanly beenden

---

**Status**: 🟡 Ready for Development (nach task-001,002,003)
**Next Task**: task-005 (Stack Management)
**Estimated Completion**: 17. Dezember 2025 (2 SP nach math tasks)
