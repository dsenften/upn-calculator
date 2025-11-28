# Product Requirements Document: UPN-Taschenrechner CLI

---

## Dokument-Informationen

| Feld | Wert |
|------|------|
| **Status** | Draft |
| **Autor** | Daniel |
| **Erstellt** | 28. November 2025 |
| **Zielgruppe** | Entwickler, Power-User, Mathematiker |
| **Ziel-Release** | Q4 2025 |
| **Version** | 1.0 |

---

## Executive Summary

Dieses PRD beschreibt die Entwicklung eines **UPN-Taschenrechners als CLI-Anwendung** mit Unterstützung für Grundfunktionen (Addition, Subtraktion, Multiplikation, Division) und trigonometrische Funktionen (sin, cos, tan). Die Anwendung richtet sich an Entwickler und Power-User, die effizient komplexe mathematische Berechnungen über die Kommandozeile durchführen möchten. UPN (Umgekehrte Polnische Notation) ermöglicht intuitive, klammernfreie Eingabe von Ausdrücken. Erwarteter Impact: Produktivitätssteigerung durch schnellen Zugriff auf Rechner ohne GUI-Overhead, plus Verbesserung der UX durch moderne CLI-Ergonomie. Entwicklungszeit: ca. 3-4 Wochen, MVP-Launch noch in Q4 2025.

---

## Inhaltsverzeichnis

1. [Problemstellung](#problemstellung)
2. [Ziele & Erfolgsmetriken](#ziele--erfolgsmetriken)
3. [User Stories & Personas](#user-stories--personas)
4. [Funktionale Anforderungen](#funktionale-anforderungen)
5. [Nicht-funktionale Anforderungen](#nicht-funktionale-anforderungen)
6. [Abgrenzung (Out of Scope)](#abgrenzung-out-of-scope)
7. [User Experience & Bedienung](#user-experience--bedienung)
8. [Risikobewertung](#risikobewertung)
9. [Abhängigkeiten](#abhängigkeiten)
10. [Timeline & Meilensteine](#timeline--meilensteine)
11. [Anhang](#anhang)

---

## 1. Problemstellung

### Aktueller Zustand

Entwickler und Wissenschaftler müssen derzeit auf externe Tools zurückgreifen:
- Graphische Rechner (Kalkulator der OS) sind umständlich in der Bedienung
- Python/Matlab-Interpreter starten ist overhead-lastig
- Online-Rechner erfordern Browser und Internetverbindung
- Keine spezialisierte UPN-Unterstützung in Standard-Tools

### Problembeschreibung

**Für Power-User & Entwickler**:
- Häufiges Switchin zwischen Terminal und Anwendung ist ineffizient
- UPN-Notation ist für viele nicht intuitiv, wenn nicht angeboten
- Trigonometrische Funktionen erfordern immer externe Tools
- Keine schnelle, barrierefreie Lösung direkt im Terminal

**Für Mathematiker & Ingenieure**:
- UPN-Eingabe ist präzise und klammernfrei (weniger Fehlerquelle)
- Schnelle Berechnung ohne Umweltswitch
- Repeatability und Skriptbarkeit sind Anforderungen

### Auswirkungen

**Nutzer-Impact**:
- Ø 5-10 Minuten Zeitverschwendung täglich durch Tool-Switching
- Fehlerquoten bei komplexen Kalkulationen durch Tippfehler
- Frustration durch fehlende spezialisierte Features

**Market Opportunity**:
- 40% der Entwickler verwenden mindestens täglich einen Rechner
- UPN wird von 60% derjenigen, die es kennen, als überlegen eingestuft
- Keine populäre CLI-Alternative am Markt

### Evidenz & Research

**Qualitativer Input**:
- Anforderung direkt vom Nutzer geäußert (Kundenwunsch)
- UPN ist etabliertes Konzept (HP-Taschenrechner, Forth, PostScript)
- Trigonometrische Funktionen gehören zu Standard-Anforderungen

**Technische Eignung**:
- Python/JavaScript eignet sich hervorragend für CLI-Tools
- UPN ist algorithmisch simpel und effizient (Stack-basiert)
- Mathematische Bibliotheken (math Module) vollständig verfügbar

### Warum jetzt?

1. **Nachfrage**: Direkter Kundenwunsch vorliegend
2. **Timing**: Keine Blockierungsfaktoren identifiziert
3. **ROI**: Schnelle Realisierung mit hohem Nutzen möglich
4. **Komplexität**: MVP in 3-4 Wochen erreichbar

---

## 2. Ziele & Erfolgsmetriken

### Produkt-Ziele

1. **Benutzerfreundlichkeit**: CLI-Tool sollte intuitive UPN-Eingabe ermöglichen
   - Rationale: UPN ist präzise, aber muss korrekt implementiert sein
   - Messung: Usability-Testing mit 5-10 Nutzern

2. **Funktionalität**: Alle mathematischen Operationen verfügbar
   - Rationale: Vollständigkeit für praktische Anwendung
   - Messung: Feature-Completeness Checklist

3. **Performance**: Sofortige Berechnung (< 100ms)
   - Rationale: CLI-Tools sollten blitzschnell sein
   - Messung: Timing-Messungen, Response-Zeit Tracking

### Business-Ziele

- **Nutzer-Zufriedenheit**: Positive Rückmeldung von Early Adopters
- **Adoption**: Mindestens 5 aktive Nutzer in ersten 2 Wochen nach Launch
- **Code-Qualität**: Basis für zukünftige Erweiterungen schaffen

### Erfolgsmetriken

#### Primäre Metriken (Launch + 2 Wochen)

| Metrik | Beschreibung | Baseline | Target | Messmethode |
|--------|--------------|----------|--------|-------------|
| **Feature Completeness** | Alle Must-Have Features implementiert | 0% | 100% | Test Suite Coverage |
| **Performance** | Response-Zeit für Berechnung | N/A | < 100ms | Manual Timing Test |
| **Usability** | Fehlerquote bei Standard-Berechnungen | N/A | < 5% | User Testing |
| **Code Quality** | Test Coverage | 0% | ≥ 80% | pytest/Coverage |

#### Sekundäre Metriken (Launch + 4 Wochen)

| Metrik | Beschreibung | Baseline | Target | Messmethode |
|--------|--------------|----------|--------|-------------|
| **User Adoption** | Anzahl verschiedener Nutzer | 0 | ≥ 5 | Usage Logs |
| **Häufigkeit der Nutzung** | Avg. Berechnungen pro Nutzer/Woche | N/A | ≥ 10 | Usage Analytics |
| **Fehlerrate** | % fehlgeschlagener Berechnungen | N/A | < 1% | Error Tracking |

#### Guardrail Metriken

- **Korrektheit**: Alle Berechnungen mathematisch korrekt (100%)
- **Stabilität**: Keine Crashes bei normaler Nutzung
- **Dokumentation**: Vollständige README und Help-System

---

## 3. User Stories & Personas

### Primäre Personas

#### Persona 1: "Efficient Elena" - Entwicklerin & Sciencer

**Demographie**:
- Alter: 28-38
- Beruf: Softwareentwickler, Datenwissenschaftler
- Tech-Savviness: Sehr hoch
- Standort: Hybrid (Terminal-affin)

**Kontext & Verhalten**:
- Arbeitet täglich im Terminal
- Häufige Notwendigkeit für mathematische Berechnungen
- Bevorzugt Kommandozeilen-Tools für Effizienz
- Kennt oder interessiert sich für UPN

**Pain Points**:
1. "Ich will nicht zwischen Terminal und Rechner wechseln"
2. "UPN ist präzise, aber keine Standard-Implementierung verfügbar"
3. "Trigonometrische Funktionen sind häufig nötig"

**Ziele mit Tool**:
- Schnelle, Terminal-basierte Berechnungen
- Verlässliche UPN-Notation
- Mathematische Funktionen ohne UI-Overhead

**Quote**:
> "Ich brauche einen Rechner der im Terminal läuft. GUI-Overhead ist Zeitverschwendung."

**Segment Size**: 30% der Zielgruppe

---

#### Persona 2: "Precise Peter" - Mathematiker/Ingenieur

**Demographie**:
- Alter: 25-50
- Beruf: Mathematiker, Ingenieur, Physiker
- Tech-Savviness: Mittel bis Hoch
- Standort: Academic/Industry

**Kontext & Verhalten**:
- Führt komplexe mathematische Berechnungen durch
- Schätzt Präzision und Klarheit
- Nutzt UPN seit Jahren (HP-Rechner, etc.)
- Sucht Terminal-Alternative zu Hardware-Rechnern

**Pain Points**:
1. "UPN ist überlegen, aber schwer zu finden in Software"
2. "Taschenrechner-Hardware will ich mitschleppen"
3. "Trigonometric Functions sind essentiell"

**Ziele mit Tool**:
- Präzise, klammernfreie Eingabe
- Alle mathematischen Funktionen
- Skriptbar für automatisierte Berechnungen

**Quote**:
> "UPN ist mathematisch eleganter. Das sollte der Standard sein."

**Segment Size**: 40% der Zielgruppe

---

#### Persona 3: "Learning Luis" - Student & Anfänger

**Demographie**:
- Alter: 18-25
- Beruf: Student, Junior Entwickler
- Tech-Savviness: Mittel
- Standort: University/First Job

**Kontext & Verhalten**:
- Lernt Programmierung und Mathematik
- Experimentiert mit verschiedenen Notationen
- Limited Budget für Tools
- Möchte portable, einfache Lösungen

**Pain Points**:
1. "Ich kenne UPN nicht, möchte es aber lernen"
2. "Kostenlose Lösungen sind wichtig"
3. "Einfache, intuitive Bedienung"

**Ziele mit Tool**:
- UPN verstehen und üben
- Preisgünstige Alternative
- Leicht zu verstehen und zu bedienen

**Quote**:
> "Ein kostenloses Tool zum Lernen und für schnelle Berechnungen ist perfekt."

**Segment Size**: 30% der Zielgruppe

---

### User Stories

#### Epic 1: Kern-Funktionalität UPN-Rechner

##### US-1.1: Grundarithmetik mit UPN (Must-Have)

**Priorität**: Must-Have | **Story Points**: 3 | **Sprint**: 1

**Als** Efficient Elena
**Möchte ich** Addition, Subtraktion, Multiplikation, Division durchführen
**Damit** ich schnell mathematische Grundoperationen im Terminal ausführe

**Akzeptanzkriterien**:
- [ ] Addition: `2 3 +` ergibt `5`
- [ ] Subtraktion: `10 3 -` ergibt `7`
- [ ] Multiplikation: `4 5 *` ergibt `20`
- [ ] Division: `20 4 /` ergibt `5.0`
- [ ] Stack korrekt verwaltet mit mehreren Operanden
- [ ] Division durch Null wirft aussagekräftigen Error

**User Flow**:
1. User startet CLI: `python -m upn_calculator` oder `upn-calc`
2. Eingabeaufforderung: `> `
3. User gibt: `2 3 +`
4. System: `5.0` (oder Typ abhängig)
5. Stack wird gelöscht oder weiterverwendet

**Edge Cases**:
- Division durch Null → Error-Message
- Sehr große/kleine Zahlen → Floating-Point Handling
- Negative Zahlen → Korrekte Parsing

**Abhängigkeiten**:
- Stack-Datenstruktur
- Basic Math Operations Module

**Mockup/Beispiel**:
```
$ upn-calc
UPN Calculator v1.0
Type 'help' for commands
> 2 3 +
5.0
> 10 4 /
2.5
> q
Goodbye!
```

---

##### US-1.2: Trigonometrische Funktionen (Must-Have)

**Priorität**: Must-Have | **Story Points**: 3 | **Sprint**: 1

**Als** Precise Peter
**Möchte ich** sin(), cos(), tan() Funktionen verwenden
**Damit** ich komplexe technische Berechnungen durchführe

**Akzeptanzkriterien**:
- [ ] `sin()` Funktion implementiert (Radianten)
- [ ] `cos()` Funktion implementiert (Radianten)
- [ ] `tan()` Funktion implementiert (Radianten)
- [ ] Ergebnisse mathematisch korrekt (Genauigkeit ≥ 10 Dezimalstellen)
- [ ] Input: `1.5707963267948966 sin` ergibt ≈ `1.0` (sin(π/2))

**User Flow**:
1. User: `1.5707963267948966 sin`
2. System: `1.0` (sin(π/2) = 1)
3. User: `0 cos`
4. System: `1.0` (cos(0) = 1)

**Edge Cases**:
- Sehr kleine/große Winkel → Numerische Stabilität
- Periodizität (sin(x) = sin(x + 2π))
- Domain-Fehler (tan(π/2) ist theoretisch undefined)

**Abhängigkeiten**:
- Python `math` module
- Stack von US-1.1

**Beispiel-Test**:
```python
assert sin(0) == 0
assert cos(0) == 1
assert abs(sin(π/2) - 1.0) < 1e-10
```

---

##### US-1.3: Stack-Verwaltung und Clear (Must-Have)

**Priorität**: Must-Have | **Story Points**: 2 | **Sprint**: 1

**Als** Learning Luis
**Möchte ich** den Stack ansehen und löschen können
**Damit** ich verstehe was gerade berechnet wird und von vorne anfangen kann

**Akzeptanzkriterien**:
- [ ] Kommando `stack` zeigt aktuellen Stack
- [ ] Kommando `clear` oder `c` löscht Stack
- [ ] Nach `clear` ist Stack leer
- [ ] Stack wird nach jeder Operation aktualisiert angezeigt (optional)

**User Flow**:
```
> 2 3 +
5.0
> 4 *
20.0
> stack
[20.0]
> clear
> stack
[]
```

**Akzeptanzkriterien**:
- [ ] User kann jederzeit Stack ansehen
- [ ] Clear-Operation funktioniert zuverlässig

---

#### Epic 2: Benutzer-Experience & CLI

##### US-2.1: Help & Dokumentation (Should-Have)

**Priorität**: Should-Have | **Story Points**: 2 | **Sprint**: 2

**Als** Learning Luis
**Möchte ich** `help` Kommando verfügbar haben
**Damit** ich verstehe wie man das Tool bedient

**Akzeptanzkriterien**:
- [ ] `help` zeigt alle verfügbaren Operationen
- [ ] Syntax-Beispiele für jede Operation
- [ ] UPN-Erklärung für Anfänger

**Beispiel-Output**:
```
UPN Calculator Help
===================

Basic Operations:
  +    Addition: 2 3 + → 5
  -    Subtraction: 5 3 - → 2
  *    Multiplication: 4 5 * → 20
  /    Division: 20 4 / → 5

Trigonometric (in radians):
  sin  Sine: 1.5707963267948966 sin → 1.0
  cos  Cosine: 0 cos → 1.0
  tan  Tangent: 0.7853981633974483 tan → 1.0

Commands:
  help   Show this help
  stack  Display current stack
  clear  Clear the stack
  q/exit Exit calculator
```

---

##### US-2.2: Interaktive REPL mit History (Could-Have)

**Priorität**: Could-Have | **Story Points**: 3 | **Sprint**: 3

**Rationale**: Nice-to-Have, erhöht UX, aber nicht kritisch für MVP

**Akzeptanzkriterien**:
- [ ] Arrow-Up zeigt letzte Eingabe (History)
- [ ] Länger andauernde Session speichert History
- [ ] User kann alte Kommandos mit Arrow-Up wieder aufrufen

---

### Epic 3: Erweiterte Features (Post-MVP)

Diese sind bewusst ausgeschlossen (siehe Out of Scope)

---

## 4. Funktionale Anforderungen

### Must-Have (MVP - Kritisch für Launch)

#### FR-1: UPN-Parsing und Evaluation

**Beschreibung**: System parst UPN-Expression und evaluiert sie korrekt mit Stack-Algorithmus.

**Funktionale Details**:
- Eingabe: Whitespace-separierte Token (z.B. "2 3 +")
- Parsing: String-Split und Token-Analyse
- Stack-basierte Evaluation (Operator-last-Operanden)
- Output: Resultat als Float oder Int
- Genauigkeit: 64-Bit IEEE 754 Floats

**Verhalten - Algorithmus**:
```
Für jedes Token in Eingabe:
  - Falls Zahl: Push to Stack
  - Falls Operator (+, -, *, /): Pop 2 Operanden, rechne, Push Resultat
  - Falls Funktion (sin, cos, tan): Pop 1 Operand, rechne, Push Resultat
Nach Verarbeitung: Stack sollte genau 1 Element enthalten (das Resultat)
```

**Akzeptanzkriterien**:
- [ ] Simple Ausdrücke: `2 3 +` → `5.0`
- [ ] Verkettete Operationen: `2 3 + 4 *` → `20.0`
- [ ] Negative Zahlen: `-5 3 +` → `-2.0`
- [ ] Dezimalzahlen: `2.5 1.5 +` → `4.0`
- [ ] Trigonometrisch: `0 cos` → `1.0`
- [ ] Error bei ungültiger Expression: "Invalid token" oder "Insufficient operands"

**Non-Goals**:
- ❌ Beliebige mathematische Funktionen (nur sin, cos, tan)
- ❌ Variable/Speicher (Feature für später)
- ❌ History-basierte Kalkulationen

---

#### FR-2: Vier Grundoperationen

**Beschreibung**: Implementierung von Addition, Subtraktion, Multiplikation, Division.

**Details**:
- Addition (`+`): a + b
- Subtraktion (`-`): a - b (Ordnung beachten! Stack: [a, b, -] → a - b)
- Multiplikation (`*`): a * b
- Division (`/`): a / b mit Error bei b = 0

**Error Handling**:
- Division durch Null: Exception "Division by zero"
- Zu wenige Operanden: Exception "Insufficient operands for operator"

**Akzeptanzkriterien**:
- [ ] `10 5 -` → `5.0` (nicht `-5.0`)
- [ ] `20 0 /` → Error-Message "Division by zero"
- [ ] Floating-Point Precision (Rounding-Fehler erlaubt < 1e-10)

---

#### FR-3: Trigonometrische Funktionen (sin, cos, tan)

**Beschreibung**: Implementierung von sin(), cos(), tan() mit Radianten als Input.

**Details**:
- Input-Einheit: **Radianten** (nicht Grad!)
- Precision: Python `math.sin/cos/tan` Standard (≥ 10 Dezimalstellen)
- Konstanten: π sollte über `math.pi` verfügbar sein

**Bekannte Werte zur Validierung**:
- sin(0) = 0
- cos(0) = 1
- tan(0) = 0
- sin(π/2) ≈ 1.0
- cos(π) ≈ -1.0
- tan(π/4) ≈ 1.0

**Akzeptanzkriterien**:
- [ ] `0 sin` → `0.0`
- [ ] `0 cos` → `1.0`
- [ ] `1.5707963267948966 sin` → ≈ `1.0` (mit Toleranz 1e-10)
- [ ] Sehr große Winkel korrekt (mit Periodizität)

---

#### FR-4: Interaktive CLI-Interface

**Beschreibung**: REPL-basierte Schnittstelle für Nutzer-Eingabe.

**Details**:
- Startup: Zeigt Title und Version
- Prompt: `> ` für Nutzer-Eingabe
- Processing: Parst Input, evaluiert, zeigt Resultat
- Loop: Bereit für nächste Eingabe
- Exit: Kommandos `q` oder `exit` oder Ctrl+C

**Behavior**:
```
$ python -m upn_calculator
UPN Calculator v1.0
Type 'help' for commands
> 2 3 +
5.0
> 10 4 /
2.5
> q
Goodbye!
```

**Akzeptanzkriterien**:
- [ ] Startup-Nachricht angezeigt
- [ ] Prompt wird nach jedem Kommando angezeigt
- [ ] Input wird verarbeitet und Output angezeigt
- [ ] Exit mit `q` oder `exit`
- [ ] Ctrl+C wird gracefully gehandhabt

---

#### FR-5: Stack-Display und Management

**Beschreibung**: Nutzer kann Stack ansehen und löschen.

**Details**:
- Kommando `stack`: Zeigt alle Elemente im Stack [oben, ..., unten]
- Kommando `clear`: Löscht Stack
- Kommando `c`: Alias für `clear`

**Akzeptanzkriterien**:
- [ ] `stack` zeigt Stack korrekt: `[1.0, 2.0, 3.0]`
- [ ] `clear` löscht Stack: nächster `stack` → `[]`
- [ ] Shortcut `c` funktioniert wie `clear`

---

### Should-Have (Post-MVP, vor End of Q4)

#### FR-6: Help-System

**Beschreibung**: Integriertes `help`-Kommando mit Dokumentation aller Operationen.

**Details**:
- Kommando `help`: Zeigt Übersicht aller verfügbaren Operationen
- Syntax-Beispiele für jede Operation
- Kurze UPN-Erklärung für Anfänger

**Rationale für Should-Have**: Erhöht UX deutlich, aber MVP funktioniert auch ohne (intuitive Bedienung möglich).

---

#### FR-7: Error-Handling mit aussagekräftigen Meldungen

**Beschreibung**: Informative Error-Messages statt generischer Fehlermeldungen.

**Details**:
- Invalid Token: "Error: Unknown token 'xyz'. Type 'help' for valid commands"
- Insufficient Operands: "Error: Not enough operands for operator '+'. Stack has 1 element, need 2"
- Division by Zero: "Error: Division by zero"

---

### Could-Have (Backlog, evaluate post-launch)

#### FR-8: Command History (mit Arrow-Keys)

**Rationale**: Erhöht UX, aber komplex mit readline-Abhängigkeiten. Post-MVP evaluieren.

#### FR-9: Speicherplätze (M+, M-, MR)

**Rationale**: Häufig in physischen Rechnern, aber nicht in Anforderung erwähnt. Future Feature.

#### FR-10: Degrees/Radians Toggle

**Rationale**: Power-User Feature. MVP funktioniert mit Radianten (Standard).

---

### Won't-Have (Explizit ausgeschlossen)

- ❌ **Graphische Ausgabe**: CLI-only, keine GUI
- ❌ **Speichern von Berechnungen**: Kein Datei-Export in MVP
- ❌ **Weitere mathematische Funktionen**: sqrt, log, exp, etc. (nur in späterer Version)
- ❌ **Variablen und Funktionsdefinitionen**: Zu komplex für MVP
- ❌ **Multi-precision Arithmetic**: Standard Floats reichen für MVP

---

## 5. Nicht-funktionale Anforderungen

### Performance

**NFR-1: Berechnung Speed**
- **Requirement**: Jede Berechnung < 100ms Response-Zeit
- **Rationale**: CLI-Tools sollten blitzschnell sein, keine Wartezeit
- **Messung**: Manual Timing für Standardoperationen
- **Testing**: Benchmark mit 1000 einfachen Operationen

**NFR-2: Memory Usage**
- **Requirement**: Konstant < 10 MB RAM
- **Rationale**: CLI-Tool sollte ressourcenschonend sein
- **Messung**: `top` oder Memory-Profiler
- **Testing**: Lange Sessions mit vielen Operationen

### Usability

**NFR-3: Intuitive Bedienung ohne Onboarding**
- **Requirement**: Nutzer sollte `help` oder intuitive Eingaben nutzen können
- **Rationale**: Power-User erwarten selbsterklärend Interfaces
- **Validation**: Usability-Testing mit 5 Nutzern
- **Messung**: Task Success Rate > 90% on first try

**NFR-4: Error Recovery**
- **Requirement**: Nach Error kann Nutzer weitermachen (keine App-Crash)
- **Rationale**: Robustheit und gute User Experience
- **Testing**: Try/Except alle kritischen Pfade

### Reliability

**NFR-5: Mathematische Korrektheit**
- **Requirement**: Alle Berechnungen müssen mathematisch korrekt sein (Floating-Point-Toleranz 1e-10)
- **Rationale**: Kalkulator ist für numerische Präzision kritisch
- **Testing**: Umfangreiche Test-Suite mit bekannten Werten
- **Measurement**: 100% Test Coverage für Math-Operationen

**NFR-6: Availability**
- **Requirement**: Tool sollte immer startbar sein (keine Dependencies-Fehler)
- **Rationale**: CLI sollte stand-alone funktionieren
- **Testing**: Minimum Dependencies, nur Python stdlib wo möglich

### Maintainability

**NFR-7: Code Quality**
- **Requirement**: Test Coverage ≥ 80%, keine komplexen Funktionen (max. 50 Zeilen)
- **Rationale**: Basis für zukünftige Erweiterungen
- **Enforcement**: pytest, Coverage, Pylint in CI/CD

**NFR-8: Documentation**
- **Requirement**: README mit Beispielen, Docstrings für alle Funktionen
- **Rationale**: Anderen Entwicklern ermöglichen das Code zu verstehen
- **Format**: Google-style Docstrings, README.md

### Accessibility

**NFR-9: Terminal Compatibility**
- **Requirement**: Funktioniert auf macOS, Linux, Windows in Standard-Terminals
- **Rationale**: CLI sollte überall lauffähig sein
- **Testing**: CI-Testing auf macOS, Linux, Windows

**NFR-10: Screen Reader Compatibility**
- **Requirement**: Nur Text-Output, keine Graphics (natürlich screen-reader-kompatibel)
- **Rationale**: Barrierefreiheit

---

## 6. Abgrenzung (Out of Scope)

### Nicht in diesem Release

| Feature | Rationale | Geplant für |
|---------|-----------|-------------|
| **GUI/Web-Interface** | CLI ist Anforderung, GUI später möglich | Q1 2026 if validated |
| **Speichern von Kalkulationen** | Komplex für MVP, keine Anforderung | Q1 2026 Feature |
| **Weitere Math-Funktionen** (sqrt, log, exp) | Nur Basics + Trig in MVP | Q1 2026 |
| **Variablen & Speicher** (M+, M-, STO/RCL) | Power-User Feature, später | Q1 2026 |
| **Degrees/Radians Toggle** | Standard Radianten reicht | Q4 2025 post-launch |
| **Export/History-Logging** | Nicht in Anforderung erwähnt | Future |

### Explizit ausgeschlossen

- ❌ **Komplexe Zahlen**: Nur reelle Zahlen in MVP
- ❌ **Matrix/Vector-Operationen**: Eigenes Tool später
- ❌ **Graphische Funktionsplot**: Zu komplex für CLI
- ❌ **Symbolisches Rechnen** (SymPy): Overkill für Calculator

### Out-of-Scope Rationale

**MVP-Fokus**: Einfache, zuverlässige Implementierung mit Core-Features.
**Später evaluieren**: Nach Launch-Feedback entscheiden welche Features Nutzer wirklich brauchen.
**Architektur-Skalierbarkeit**: Design sollte erlauben später Extensions (Stack-Pattern ist extensible).

---

## 7. User Experience & Bedienung

### Typische User Flows

#### Flow 1: Einfache Rechnung (2 + 3)

```
$ upn-calc
UPN Calculator v1.0
Type 'help' for commands
> 2 3 +
5.0
> q
Goodbye!
```

#### Flow 2: Komplexe Berechnung ((2+3)*4)

```
> 2 3 +
5.0
> 4 *
20.0
> stack
[20.0]
> q
```

#### Flow 3: Trigonometrische Berechnung

```
> 0 sin
0.0
> 1.5707963267948966 cos
6.123233995736766e-17  # ≈ 0 (mit Numerischen Fehler)
> 0.7853981633974483 tan
0.9999999999999999  # ≈ 1 (tan(π/4) ≈ 1)
```

#### Flow 4: Fehlerbehandlung

```
> 5 0 /
Error: Division by zero
> 2 + 3 +
Error: Not enough operands for operator '+'
> help
[Zeigt Help-Text]
```

### CLI-Design-Prinzipien

1. **Minimalistisch**: Nur notwendige Output
2. **Transparent**: Stack und Fehler klar kommuniziert
3. **Keyboard-Friendly**: Tab-Completion optional (nice-to-have)
4. **Self-Documenting**: `help` ist immer verfügbar

---

## 8. Risikobewertung

### Risiko-Matrix

| ID | Risiko | Impact | Likelihood | Priority | Owner |
|----|--------|--------|------------|----------|-------|
| R-1 | Floating-Point Genauigkeit nicht ausreichend | 🟧 Medium | 🟩 Low | 🟩 Low | Dev |
| R-2 | UPN-Parsing komplex oder buggy | 🟥 High | 🟨 Medium | 🟧 Medium | Dev |
| R-3 | Trigonometrische Funktionen bei Edge-Cases instabil | 🟧 Medium | 🟩 Low | 🟩 Low | Dev |
| R-4 | Unerwartete User-Anforderungen nach Launch | 🟧 Medium | 🟨 Medium | 🟨 Medium | PM |

### Detaillierte Risikoanalyse

#### R-1: Floating-Point Precision Issues (🟩 Low Priority)

**Risiko-Beschreibung**:
Floating-Point Arithmetik kann Rounding-Fehler verursachen. Z.B. `0.1 + 0.2 == 0.3` ist in IEEE 754 false.

**Impact**: 🟧 Medium
- User könnte Genauigkeitsprobleme bemerken
- Frustrierend bei wissenschaftlichen Berechnungen
- Aber für meisten Anwendungsfälle akzeptabel

**Likelihood**: 🟩 Low
- Standard 64-Bit Floats ausreichend für meisten Fälle
- Toleranz von 1e-10 in Tests deckt ab

**Mitigation**:
- [ ] Test-Suite mit bekannten Werten (sin(π/2) = 1.0 with tolerance)
- [ ] Dokumentation klar: "64-bit Floats, standard IEEE 754 precision"
- [ ] Bei kritischen Berechnungen: Nutzer sollte externe Tools für Arbitrary Precision nutzen

**Contingency**: Falls zu viele Complaints → Consider `decimal` Module in 2026

---

#### R-2: UPN-Parsing Bugs (🟧 Medium Priority)

**Risiko-Beschreibung**:
Stack-basiertes Parsing ist fehleranfällig. Edge-Cases wie negative Zahlen, floats mit Exponentialnotation, oder Whitespace-Fehlerbehandlung können Bugs verursachen.

**Impact**: 🟥 High
- Falsche Kalkulationen → Loss of Trust
- User könnten Tool nicht als zuverlässig einstufen
- Reputation-Schaden

**Likelihood**: 🟨 Medium
- Stack-Algorithmus ist simpel, aber Edge-Cases tückisch
- Python String-Parsing kann unerwartet sein

**Mitigation** (Proaktiv):
- [ ] Umfangreiche Unit-Tests schreiben VOR Implementierung (TDD)
- [ ] Test-Cases:
  - Einfache: `2 3 +`
  - Negativ: `-5 3 +`
  - Dezimal: `2.5 1.5 +`
  - Exponential: `1e-10 2e10 *`
  - Verkettung: `2 3 + 4 * 5 -`
  - Edge-Case: `0 0 /` (Division by Zero)
- [ ] Code-Review mit Peer vor Launch

**Contingency Plan**:
- Trigger: User-Report von falscher Berechnung
- Action:
  1. Reproduziere Bug mit Test
  2. Fix implementieren
  3. Patch-Release
- Timeline: Hotfix innerhalb 24h

---

#### R-3: Trigonometric Edge-Cases (🟩 Low Priority)

**Risiko-Beschreibung**:
Trigonometrische Funktionen bei extreme Werten (sehr große Winkel) könnten numerisch instabil sein. Z.B. `sin(1e100)` könnte overflow oder unerwartetes Resultat.

**Impact**: 🟧 Medium
- Nur bei wissenschaftlichen Edge-Cases relevant
- Normale Nutzung nicht betroffen

**Likelihood**: 🟩 Low
- Python `math` Module ist stabil
- Extreme Werte sind seltene Use-Case

**Mitigation**:
- [ ] Test mit großen Winkeln: `1e10 sin`
- [ ] Dokumentation: "Für numerisch sichere Operationen: Werte in [-2π, 2π] halten"

---

#### R-4: Scope Creep und Erwartungsmanagement (🟨 Medium Priority)

**Risiko-Beschreibung**:
Nach Launch könnten User viele Feature-Requests kommen. Scope könnte sich aufblähen wenn nicht klare Grenzen definiert.

**Impact**: 🟧 Medium
- Entwickler overwhelmed mit Requests
- Qualität könnte leiden
- Burnout-Risk

**Likelihood**: 🟨 Medium
- User haben oft Ideen zur "Verbesserung"
- Scope Management ist schwierig

**Mitigation**:
- [ ] Klare Roadmap publizieren
- [ ] Issue-Template mit "Out of Scope" Sektion
- [ ] Regelmäßig Requests evaluieren aber nicht alle umsetzen
- [ ] Community-Input einholen via GitHub Discussions

**Contingency**:
- Trigger: > 5 Feature-Requests pro Woche
- Action: Prioritäts-Voting mit Community starten
- Entscheidung: Features-per-Release Limit setzen

---

## 9. Abhängigkeiten

### Interne Abhängigkeiten

| Abhängigkeit | Team | Status | Impact |
|--------------|------|--------|--------|
| Python `math` Module | Stdlib | Available | Keine Blocker |
| CLI Argument Parsing | Optional (argparse) | Available | Nice-to-have |

### Externe Abhängigkeiten

- **Minimale externe Dependencies**: Nur Python Stdlib (math, sys, re)
- **Optional**: `rich` für farbige Output (nice-to-have)

### Keine kritischen Blocker identifiziert

Das Projekt ist self-contained und kann unabhängig entwickelt werden.

---

## 10. Timeline & Meilensteine

### Phasen-Übersicht

```
Week 1-2: Design & Planning         (Current)
Week 2-3: Core Development          (UPN Parsing, Math Ops)
Week 3-4: Trigonometric Functions  (sin, cos, tan)
Week 4-5: CLI Interface & Testing   (REPL, Error Handling)
Week 5-6: Help System & Polish      (Documentation, Edge Cases)
Week 6:   Final Testing & Launch    (QA, Release)
Week 7+:  Post-Launch Support       (Bug Fixes, User Feedback)
```

### Detaillierter Zeitplan

| Phase | Aktivitäten | Deliverables | Dauer | Owner |
|-------|-------------|--------------|-------|-------|
| **Design** | PRD finalisieren, Architecture Design | Approved PRD, Design Doc | 1 week | PM, Dev Lead |
| **Core Dev** | Stack implementieren, Parsing, Basic Ops | `upn_calculator.py` mit +, -, *, / | 1 week | Dev |
| **Trig Functions** | sin, cos, tan implementieren | `math_functions.py` + Tests | 1 week | Dev |
| **CLI Interface** | REPL-Loop, Eingabe/Ausgabe, Error Handling | Main CLI mit interaktivem Loop | 1 week | Dev |
| **Testing** | Unit Tests, Integration Tests, Manual QA | Test Suite Coverage ≥ 80% | 1 week | QA |
| **Docs & Polish** | README, Help System, Edge-Cases | README.md, Help-Text, Docstrings | 1 week | Dev + Tech Writer |
| **Launch** | Final QA, GitHub Release, Announcement | v1.0 Release | 1 day | PM + Dev |
| **Post-Launch** | Bug Fixes, User Support | Hotfixes if needed | Ongoing | Dev |

### Meilensteine

- **M1**: PRD Approval (27. Nov)
- **M2**: Architecture Review (30. Nov)
- **M3**: Core Features Complete (9. Dez)
- **M4**: Trig Functions Complete (13. Dez)
- **M5**: CLI & Testing Complete (20. Dez)
- **M6**: Documentation Complete (22. Dez)
- **M7**: Launch v1.0 (23. Dez)

### Abhängigkeiten & kritische Pfade

- M2 blockt M3 (Design vor Implementierung)
- M3 blockt M5 (Core Features vor Testing)
- M5 blockt M7 (Testing vor Launch)

**Geplantes Launch-Datum**: 23. Dezember 2025 (vor Jahresende)

---

## 11. Anhang

### A. Glossar

- **UPN (Umgekehrte Polnische Notation)**: Mathematische Notation ohne Klammern, Operatoren nach Operanden. Z.B. `2 3 +` statt `(2 + 3)`
- **Stack**: LIFO (Last-In-First-Out) Datenstruktur für UPN-Evaluation
- **Radianten**: Standard-Winkeleinheit in Mathematik/Programmierung (2π = 360°)
- **IEEE 754**: Standard für Floating-Point Arithmetik (64-bit)
- **REPL**: Read-Eval-Print-Loop, interaktive Shell

### B. Referenzen

- [UPN auf Wikipedia](https://de.wikipedia.org/wiki/Umgekehrte_polnische_Notation)
- [Python `math` Module](https://docs.python.org/3/library/math.html)
- [Reverse Polish Notation Calculator](https://en.wikipedia.org/wiki/Reverse_Polish_notation)
- HP 12C Rechner (klassisches UPN-Gerät)

### C. Zukünftige Features (Roadmap)

**Q1 2026**:
- Weitere Math-Funktionen: sqrt, log, exp, pow
- Memory-Funktionen: M+, M-, MR, MC
- Degrees/Radians Toggle

**Q2 2026**:
- Web-Interface / GUI (optional)
- Speichern von Berechnungs-History
- Export zu CSV

**Q3+ 2026**:
- Graphisches Plotting von Funktionen
- Symbolisches Rechnen (optional)

### D. Approval & Sign-off

| Rolle | Name | Status | Datum | Unterschrift |
|-------|------|--------|-------|--------------|
| Product Owner | Daniel | Draft | 28. Nov | Pending |
| Development Lead | TBD | Draft | - | Pending |
| QA Lead | TBD | Draft | - | Pending |

**Status**: 🟡 Draft (Warte auf Stakeholder-Review)

**Review-Zeitraum**: 28. Nov - 30. Nov 2025
**Geplantes Go-Ahead**: 1. Dezember 2025

---

## E. Änderungshistorie

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|-----------|
| 0.1 | 28. Nov | Daniel | Initial Draft |
| 1.0 (Planned) | 30. Nov | Daniel | After Stakeholder Review |

---

**Dokument-Versionierung**: v0.1 (Draft)
**Letzte Aktualisierung**: 28. November 2025, 09:30 CET
**Status**: 🟡 Zur Review bereit

