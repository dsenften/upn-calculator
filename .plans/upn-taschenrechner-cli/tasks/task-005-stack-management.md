# Task-005: Stack Management & Display

## Metadata
- **ID**: task-005
- **Status**: pending
- **Priority**: must
- **Estimate**: 2 Story Points
- **Labels**: [core, cli, stack-management]
- **Assignee**: `python-expert`
- **Created**: 28. November 2025
- **Updated**: 28. November 2025

## Description

Implementiere **Stack-Display und Management-Kommandos** für Nutzer, um den aktuellen Stack zu inspizieren und zurückzusetzen.

**User Story**: 
Als *Learning Luis* möchte ich `stack` eingeben um zu sehen welche Zahlen noch im Stack sind, und `clear` um neu anzufangen, damit ich meinen Arbeitsfluss kontrolliere.

**Rationale**:
- Essential für Nutzer um zu verstehen was gerade passiert
- Debugging-Hilfe bei komplexen Kalkulationen
- Ermöglicht "Restart" ohne Programm neu starten

## Acceptance Criteria

- [ ] **stack Kommando**: Zeigt alle Elemente im Stack in Reihenfolge
- [ ] **Stack Format**: `[element1, element2, element3]` (Liste-Format)
- [ ] **Clear Kommando**: `clear` löscht den kompletten Stack
- [ ] **Clear Shortcut**: `c` ist Alias für `clear`
- [ ] **Stack nach Clear**: Nächstes `stack` zeigt `[]` (leerer Stack)
- [ ] **Stack Display Format**: Oben/Unten Reihenfolge konsistent mit Push/Pop
- [ ] **Integration mit CLI**: Kommandos funktionieren in task-004 REPL
- [ ] **Test Coverage**: Mindestens 8 Unit/Integration Tests

## Dependencies

- **Requires**: task-001, task-004 (Parser und CLI Loop)
- **Blocks**: task-006 (Error Handling nutzt Stack-Status)

## Agent Recommendation

**Recommended Agent**: `python-expert`

**Rationale**: 
- Stack-Datenstruktur Management
- CLI Command Integration
- Display Formatting

## Implementation Notes

### Stack Display Implementierung

```python
# calculator.py (Erweiterung)

class UPNCalculator:
    def __init__(self):
        self.stack = []
    
    def get_stack(self) -> list:
        """
        Get copy of current stack.
        
        Returns:
            List of stack elements (top on right side)
        
        Example:
            [1.0, 2.0, 3.0] means 3.0 is on top
        """
        return self.stack.copy()
    
    def clear_stack(self) -> None:
        """Clear all elements from stack"""
        self.stack = []
    
    def display_stack(self) -> str:
        """
        Format stack for display.
        
        Returns:
            String representation like "[1.0, 2.0, 3.0]"
        """
        return str(self.stack)
```

### CLI Integration

```python
# cli.py (Erweiterung)

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
            
            # Stack Commands
            if user_input.lower() in ('stack', 's'):
                stack_display = calc.display_stack()
                print(stack_display)
                continue
            
            if user_input.lower() in ('clear', 'c'):
                calc.clear_stack()
                print("Stack cleared")
                continue
            
            if user_input.lower() == 'help':
                print_help()
                continue
            
            # Math expression
            result = calc.evaluate(user_input)
            print(f"{result}")
        
        except Exception as e:
            print(f"Error: {str(e)}")
```

### Help Text Update

```python
def print_help():
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

Stack Commands:
  stack  Display current stack
  s      Alias for 'stack'
  clear  Clear the stack
  c      Alias for 'clear'

Other Commands:
  help   Show this help
  q/exit Exit calculator

Examples:
  > 2 3 +
  5.0
  > 4 *
  20.0
  > stack
  [20.0]
  > 10 5 -
  5.0
  > s
  [5.0]
  > clear
  Stack cleared
  > stack
  []
"""
    print(help_text)
```

## Testing Strategy

### Unit Tests (mindestens 8)

```python
# test_stack_management.py

import pytest
from upn_calculator import UPNCalculator

class TestStackDisplay:
    def test_get_empty_stack(self):
        calc = UPNCalculator()
        assert calc.get_stack() == []
    
    def test_get_stack_with_elements(self):
        calc = UPNCalculator()
        calc.evaluate("2 3 +")
        assert calc.get_stack() == [5.0]
    
    def test_stack_copy_not_reference(self):
        """get_stack() sollte Copy sein, nicht Reference"""
        calc = UPNCalculator()
        calc.evaluate("2 3 +")
        
        stack1 = calc.get_stack()
        stack1.append(999)  # Modify returned list
        
        stack2 = calc.get_stack()
        assert stack2 == [5.0]  # Original unchanged
        assert 999 not in stack2

class TestClearStack:
    def test_clear_empty_stack(self):
        calc = UPNCalculator()
        calc.clear_stack()
        assert calc.get_stack() == []
    
    def test_clear_non_empty_stack(self):
        calc = UPNCalculator()
        calc.evaluate("2 3 + 4 *")
        assert len(calc.get_stack()) == 1
        
        calc.clear_stack()
        assert calc.get_stack() == []
    
    def test_clear_allows_new_calculation(self):
        calc = UPNCalculator()
        
        calc.evaluate("2 3 +")
        assert calc.get_stack() == [5.0]
        
        calc.clear_stack()
        
        calc.evaluate("10 5 -")
        assert calc.get_stack() == [5.0]  # Neue Berechnung, alte Werte weg

class TestStackDisplayFormat:
    def test_display_stack_format(self):
        calc = UPNCalculator()
        calc.evaluate("2 3 +")
        
        display = calc.display_stack()
        assert display == "[5.0]"
    
    def test_display_multiple_elements(self):
        calc = UPNCalculator()
        calc.stack = [1.0, 2.0, 3.0]  # Manuell setzen für Test
        
        display = calc.display_stack()
        assert display == "[1.0, 2.0, 3.0]"

class TestCLIStackCommands:
    def test_stack_command_via_cli(self):
        """Test stack command über CLI-Kommando"""
        calc = UPNCalculator()
        calc.evaluate("2 3 + 4 *")
        
        stack = calc.get_stack()
        assert stack == [20.0]
```

### Integration Tests

```python
def test_stack_workflow():
    """Typical user workflow with stack commands"""
    calc = UPNCalculator()
    
    # Step 1: Calculate
    calc.evaluate("2 3 +")
    assert calc.get_stack() == [5.0]
    
    # Step 2: Check stack
    stack_display = calc.display_stack()
    assert "[5.0]" == stack_display
    
    # Step 3: Continue calculation
    calc.evaluate("4 *")
    assert calc.get_stack() == [20.0]
    
    # Step 4: Check stack again
    stack_display = calc.display_stack()
    assert "[20.0]" == stack_display
    
    # Step 5: Clear
    calc.clear_stack()
    assert calc.get_stack() == []
    
    # Step 6: New calculation
    calc.evaluate("10 5 -")
    assert calc.get_stack() == [5.0]
```

## Usage Examples

```
> 2 3 +
5.0

> 4 *
20.0

> stack
[20.0]

> 10 5 -
5.0

> s
[5.0]

> clear
Stack cleared

> stack
[]

> c
Stack cleared
```

## Notes

**Referenced PRD Sections**:
- [FR-5: Stack-Display und Management](../../PRD.md#fr-5-stack-display-und-management)
- [US-1.3: Stack-Verwaltung](../../PRD.md#us-13-stack-verwaltung-und-clear-must-have)

**Stack Top Position**:
- Konvention: `[1, 2, 3]` bedeutet 3 ist oben (top of stack)
- Beim Display: Rechts ist oben, Links ist unten
- Push: neue Elemente rechts hinzufügen
- Pop: Elemente rechts entfernen

**Future Enhancements**:
- Stack mit mehr Details anzeigen (z.B. mit Indizes)
- Undo/Redo für Operationen
- Stack History speichern

---

**Status**: 🟡 Ready for Development (nach task-004)
**Next Task**: task-006 (Error Handling)
**Estimated Completion**: 18. Dezember 2025 (2 SP nach CLI-Task)
