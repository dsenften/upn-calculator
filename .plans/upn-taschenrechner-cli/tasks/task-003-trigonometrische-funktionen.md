# Task-003: Trigonometrische Funktionen (sin, cos, tan)

## Metadata
- **ID**: task-003
- **Status**: pending
- **Priority**: must
- **Estimate**: 3 Story Points
- **Labels**: [core, math, trigonometric]
- **Assignee**: `python-expert`
- **Created**: 28. November 2025
- **Updated**: 28. November 2025

## Description

Implementiere **trigonometrische Funktionen** (sin, cos, tan) als UPN-Operationen. Diese sind Must-Have und zentral für die Anforderung "welche neben den Grundfunktionen auch sin(), cos() und tan() kennt."

**Input-Einheit**: **Radianten** (nicht Grad!) - das ist mathematischer Standard.

**User Story**: 
Als *Precise Peter* möchte ich `1.5707963267948966 sin` eingeben und ca. `1.0` erhalten, damit ich trigonometrische Berechnungen durchführe.

**Rationale**:
- Direkte Anforderung vom Nutzer ("neben den Grundfunktionen auch sin(), cos() und tan()")
- Must-Have für MVP
- Nutzer sind Mathematiker/Ingenieure die mit Radianten arbeiten
- Mathematisch präzise erforderlich

## Acceptance Criteria

- [ ] **sin() Implementation**: `0 sin` → `0.0`
- [ ] **cos() Implementation**: `0 cos` → `1.0`
- [ ] **tan() Implementation**: `0 tan` → `0.0`
- [ ] **Radianten-Input**: `1.5707963267948966 sin` → ≈ `1.0` (sin(π/2) = 1)
- [ ] **Negative Winkel**: `-1.5707963267948966 sin` → ≈ `-1.0`
- [ ] **Large Angles**: `10 sin` (in radianten) → Korrekt berechnet
- [ ] **Precision**: Genauigkeit ≥ 1e-10 relativ zu erwarteten Wert
- [ ] **Math Module Integration**: Nutzt Python `math.sin`, `math.cos`, `math.tan`
- [ ] **Error Handling**: Ungültige Inputs werden gehandhabt
- [ ] **Test Coverage**: Mindestens 15 Unit-Tests mit bekannten Werten
- [ ] **Documentation**: Docstrings erklären Radianten-Einheit

## Dependencies

- **Requires**: task-001 (UPN Parser - Funktions-Handling)
- **Blocks**: task-004 (CLI REPL), task-009 (Precision Tests)
- **Related**: task-002 (Grundoperationen - parallel entwickelbar)

## Agent Recommendation

**Recommended Agent**: `python-expert`

**Rationale**: 
- Python `math` Module Expertise
- Floating-Point Precision Handling
- Trigonometrische Mathematik

## Implementation Notes

### Trigonometrische Funktionen

```python
# math_functions.py

import math
from upn_calculator.errors import UPNCalculatorError

class InvalidAngleError(UPNCalculatorError):
    """Raised when angle input is invalid"""
    pass

def sin(angle: float) -> float:
    """
    Sine function.
    
    Args:
        angle: Angle in radians
    
    Returns:
        sin(angle) as float
    
    Raises:
        InvalidAngleError: If angle is NaN or infinite
    """
    if math.isnan(angle) or math.isinf(angle):
        raise InvalidAngleError(f"Invalid angle for sin: {angle}")
    
    return math.sin(angle)

def cos(angle: float) -> float:
    """
    Cosine function.
    
    Args:
        angle: Angle in radians
    
    Returns:
        cos(angle) as float
    
    Raises:
        InvalidAngleError: If angle is NaN or infinite
    """
    if math.isnan(angle) or math.isinf(angle):
        raise InvalidAngleError(f"Invalid angle for cos: {angle}")
    
    return math.cos(angle)

def tan(angle: float) -> float:
    """
    Tangent function.
    
    Args:
        angle: Angle in radians
    
    Returns:
        tan(angle) as float
    
    Note:
        tan(π/2 + n*π) is undefined mathematically but Python returns very large values.
        This is expected behavior.
    
    Raises:
        InvalidAngleError: If angle is NaN or infinite
    """
    if math.isnan(angle) or math.isinf(angle):
        raise InvalidAngleError(f"Invalid angle for tan: {angle}")
    
    return math.tan(angle)

# Funktion-Mapping für Parser
FUNCTIONS = {
    'sin': sin,
    'cos': cos,
    'tan': tan,
}
```

### Parser Integration

```python
# calculator.py (Erweiterung)

from math_functions import FUNCTIONS

class UPNCalculator:
    def __init__(self):
        self.stack = []
        self.operators = OPERATORS  # von task-002
        self.functions = FUNCTIONS
    
    def evaluate(self, expression: str) -> float:
        tokens = expression.split()
        
        for token in tokens:
            if self.is_number(token):
                self.stack.append(float(token))
            elif token in self.operators:
                # Operatoren: brauchen 2 Operanden
                if len(self.stack) < 2:
                    raise InsufficientOperandsError(f"Operator '{token}' needs 2 operands")
                
                b = self.stack.pop()
                a = self.stack.pop()
                result = self.operators[token](a, b)
                self.stack.append(result)
            
            elif token in self.functions:
                # Funktionen: brauchen 1 Operand
                if len(self.stack) < 1:
                    raise InsufficientOperandsError(f"Function '{token}' needs 1 operand")
                
                angle = self.stack.pop()
                result = self.functions[token](angle)
                self.stack.append(result)
            
            else:
                raise InvalidTokenError(f"Unknown token: '{token}'")
        
        if len(self.stack) != 1:
            raise InvalidExpressionError(f"Invalid expression: stack has {len(self.stack)} elements")
        
        return self.stack[0]
```

### Bekannte Trigonometrische Werte für Tests

```python
# Konstanten
PI = math.pi
PI_2 = PI / 2      # 90°
PI_4 = PI / 4      # 45°
PI_3 = PI / 3      # 60°
PI_6 = PI / 6      # 30°
TWO_PI = 2 * PI    # 360°

# Bekannte Werte
sin(0) = 0
sin(PI/6) ≈ 0.5           # sin(30°)
sin(PI/4) ≈ 0.707         # sin(45°) = √2/2
sin(PI/3) ≈ 0.866         # sin(60°) = √3/2
sin(PI/2) ≈ 1.0           # sin(90°)
sin(PI) ≈ 0               # sin(180°)

cos(0) = 1
cos(PI/6) ≈ 0.866         # cos(30°) = √3/2
cos(PI/4) ≈ 0.707         # cos(45°) = √2/2
cos(PI/3) ≈ 0.5           # cos(60°)
cos(PI/2) ≈ 0             # cos(90°)
cos(PI) ≈ -1              # cos(180°)

tan(0) = 0
tan(PI/6) ≈ 0.577         # tan(30°) = 1/√3
tan(PI/4) = 1.0           # tan(45°)
tan(PI/3) ≈ 1.732         # tan(60°) = √3
```

### Datei-Struktur Update

```
upn_calculator/
├── __init__.py
├── calculator.py          # UPNCalculator class
├── parser.py             # Tokenize & Parsing
├── operators.py          # +, -, *, /
├── math_functions.py     # ← NEW: sin, cos, tan ← task-003
├── errors.py             # Exception classes
└── tests/
    ├── test_operators.py
    └── test_math_functions.py  # ← NEW: Trig Tests
```

## Testing Strategy

### Unit Tests (mindestens 15)

```python
# test_math_functions.py

import pytest
import math
from upn_calculator import UPNCalculator
from upn_calculator.math_functions import sin, cos, tan

TOLERANCE = 1e-10  # Numerical tolerance for floating-point

class TestSine:
    def test_sin_zero(self):
        assert abs(sin(0) - 0.0) < TOLERANCE
    
    def test_sin_pi_half(self):
        """sin(π/2) = 1"""
        assert abs(sin(math.pi/2) - 1.0) < TOLERANCE
    
    def test_sin_pi(self):
        """sin(π) = 0"""
        assert abs(sin(math.pi) - 0.0) < 1e-9  # Tolerance für numerische Fehler
    
    def test_sin_pi_quarter(self):
        """sin(π/4) ≈ √2/2 ≈ 0.707"""
        assert abs(sin(math.pi/4) - math.sqrt(2)/2) < TOLERANCE
    
    def test_sin_negative(self):
        """sin(-x) = -sin(x)"""
        assert abs(sin(-math.pi/2) - (-1.0)) < TOLERANCE

class TestCosine:
    def test_cos_zero(self):
        assert abs(cos(0) - 1.0) < TOLERANCE
    
    def test_cos_pi_half(self):
        """cos(π/2) = 0"""
        assert abs(cos(math.pi/2) - 0.0) < 1e-9
    
    def test_cos_pi(self):
        """cos(π) = -1"""
        assert abs(cos(math.pi) - (-1.0)) < TOLERANCE
    
    def test_cos_pi_quarter(self):
        """cos(π/4) = √2/2"""
        assert abs(cos(math.pi/4) - math.sqrt(2)/2) < TOLERANCE

class TestTangent:
    def test_tan_zero(self):
        assert abs(tan(0) - 0.0) < TOLERANCE
    
    def test_tan_pi_quarter(self):
        """tan(π/4) = 1"""
        assert abs(tan(math.pi/4) - 1.0) < TOLERANCE
    
    def test_tan_negative(self):
        """tan(-x) = -tan(x)"""
        assert abs(tan(-math.pi/4) - (-1.0)) < TOLERANCE
    
    def test_tan_pi_half_undefined(self):
        """tan(π/2) ist mathematisch undefined, Python gibt große Zahl"""
        result = tan(math.pi/2)
        # Einfach checken dass es ein Number ist (und sehr groß)
        assert isinstance(result, float)

class TestIntegrationWithCalculator:
    def test_sin_via_calculator(self):
        calc = UPNCalculator()
        result = calc.evaluate("0 sin")
        assert result == 0.0
    
    def test_cos_via_calculator(self):
        calc = UPNCalculator()
        result = calc.evaluate("0 cos")
        assert result == 1.0
    
    def test_trig_with_operations(self):
        """Trigonometric mixed with arithmetic"""
        calc = UPNCalculator()
        # 2 * sin(0) = 2 * 0 = 0
        result = calc.evaluate("2 0 sin *")
        assert result == 0.0
```

### Edge Cases

1. **Sehr große Winkel**: `1e100 sin`
   - Numerisch stabil bei Python `math.sin`
   - Periodizität: sin(x + 2π) = sin(x)

2. **Sehr kleine Winkel**: `1e-100 sin`
   - Für kleine x: sin(x) ≈ x
   - Python handhab dies korrekt

3. **Negative Winkel**: `-π/2 sin`
   - Symmetrie: sin(-x) = -sin(x)
   - tan ist odd function: tan(-x) = -tan(x)

4. **Periodizität**: `sin(π/2) = sin(π/2 + 2π)`
   - Sollte gleiches Resultat geben (mit numerischen Fehlern)

## Notes

**Referenced PRD Sections**:
- [FR-3: Trigonometrische Funktionen](../../PRD.md#fr-3-trigonometrische-funktionen-sin-cos-tan)
- [US-1.2: Trigonometrische Funktionen](../../PRD.md#us-12-trigonometrische-funktionen-must-have)
- [NFR-5: Mathematische Korrektheit](../../PRD.md#nfr-5-mathematische-korrektheit)

**Key Decision: Radianten vs. Grad**:
- **Entscheidung**: Radianten (mathematischer Standard)
- **Rationale**: 
  - Python `math` Module nutzt Radianten
  - Zielgruppe (Mathematiker/Ingenieure) arbeitet mit Radianten
  - Standard in wissenschaftlichen Anwendungen
  - Grad-Conversion kann später als "nice-to-have" hinzugefügt werden

**Numerical Stability**:
- Python `math.sin/cos/tan` sind numerisch stabil
- Kleine Fehler bei extremen Winkeln sind akzeptabel
- Test-Toleranz: 1e-10 für meisten Fälle

---

**Status**: 🟡 Ready for Development (parallel zu task-002)
**Next Task**: task-004 (CLI REPL) → nach task-001,002,003 fertig
**Estimated Completion**: 13. Dezember 2025 (3 SP parallel zu task-002)
