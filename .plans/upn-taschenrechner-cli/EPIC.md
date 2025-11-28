# UPN-Taschenrechner CLI

## Status
- **Created**: 28. November 2025
- **Status**: planned
- **Priority**: high
- **Target Release**: Q4 2025 (23. Dezember 2025)

## Executive Summary

Ein **CLI-basierter UPN-Taschenrechner** mit Grundfunktionen (Addition, Subtraktion, Multiplikation, Division) und trigonometrischen Funktionen (sin, cos, tan). Das Tool adressiert die Produktivitätsverluste bei Entwicklern und Power-Usern, die häufig zwischen Terminal und externen Rechner-Anwendungen wechseln müssen. UPN-Notation ermöglicht intuitive, klammernfreie Eingabe und ist ideal für präzise mathematische Berechnungen.

**Kernvorteil**: Schneller Zugriff auf Rechner direkt im Terminal ohne GUI-Overhead oder externe Abhängigkeiten.

## Business Value

**Problem**: 
- Entwickler/Wissenschaftler wechseln täglich zwischen Terminal und Rechner-Tools
- Ø 5-10 Minuten Zeitverschwendung täglich durch Tool-Switching
- Keine spezialisierte UPN-Unterstützung in Standard-Tools
- Fehlerquoten bei komplexen Kalkulationen durch unkomfortable UI

**Lösung**: 
- CLI-Tool direkt im Terminal verfügbar
- UPN-Eingabe für präzise, klammernfreie Berechnungen
- Alle mathematischen Funktionen schnell verfügbar

**Impact**:
- **Zeit**: 5-10 Minuten/Tag eingespart pro Nutzer
- **Qualität**: Fehlerquoten durch intuitive Bedienung reduziert
- **Produktivität**: Nahtlose Integration in Developer Workflow

**Zielgruppe Segmente**:
- Entwickler (30%)
- Mathematiker/Ingenieure (40%)
- Studenten/Anfänger (30%)

## Success Metrics

| Metrik | Baseline | Target | Messmethode |
|--------|----------|--------|-------------|
| **Feature Completeness** | 0% | 100% (Must-Have) | Feature Checklist |
| **Test Coverage** | 0% | ≥ 80% | pytest Coverage |
| **Performance** | N/A | < 100ms/Berechnung | Timing Test |
| **Usability** | N/A | < 5% Fehlerquote | User Testing (5 Personen) |
| **User Adoption** | 0 | ≥ 5 aktive Nutzer | Usage Logs (2 Wochen post-launch) |
| **Fehlerrate** | N/A | < 1% | Error Tracking |
| **Code Quality** | 0 | 80%+ Test Coverage | Coverage Report |

### Guardrail Metriken
- Mathematische Korrektheit: 100% (keine falschen Berechnungen)
- Stabilität: Keine Crashes bei normalem Gebrauch
- Dokumentation: Vollständiges README + Help-System

## Timeline & Milestones

| Milestone | Target Date | Sprint | Description |
|-----------|-------------|--------|-------------|
| **M1**: Design & Planning Approval | 30. Nov | Sprint 0 | PRD & Architecture finalisiert |
| **M2**: Core Implementation | 9. Dez | Sprint 1 | UPN Parsing + Grundfunktionen |
| **M3**: Trig Functions Complete | 13. Dez | Sprint 1-2 | sin, cos, tan implementiert |
| **M4**: CLI & Testing | 20. Dez | Sprint 2 | REPL, Error Handling, Tests |
| **M5**: Documentation & Polish | 22. Dez | Sprint 3 | Help-System, Docs, Edge-Cases |
| **M6**: Final QA | 22. Dez | Sprint 3 | Regression Testing |
| **M7**: Launch v1.0 | 23. Dez | Sprint 3 | Release to GitHub |
| **M8**: Post-Launch Support | 23. Dez+ | Sprint 4 | Bug Fixes, User Feedback |

**Critical Path**: M1 → M2 → M3 → M4 → M7
**Estimated Total Duration**: 4 Wochen (22 Tage Development)

## Dependencies

### External Dependencies
- **Python 3.13.1+**: Stdlib `math`, `sys`, `re` Module (verfügbar)
- **Terminal/CLI Support**: Standard zsh/bash auf macOS/Linux/Windows
- **GitHub**: Repository-Hosting und Release-Management

### Internal Dependencies
- Architecture Design vor Implementation
- Test-Suite schreiben vor Feature-Release
- Documentation vor Launch

### Technical Decisions Required
- [ ] Floating-Point Precision Strategy (IEEE 754 oder higher precision?)
- [ ] CLI Library: argparse (stdlib) vs. click vs. typer
- [ ] REPL Loop: Custom vs. readline Module
- [ ] Error Handling Strategy (Exception-basiert oder Error Codes)

## Key Risks

| Risiko | Impact | Likelihood | Mitigation |
|--------|--------|------------|-----------|
| **Floating-Point Precision** | 🟧 Medium | 🟩 Low | IEEE 754 ist Standard, Tests mit Toleranz |
| **UPN Parsing Bugs** | 🟥 High | 🟨 Medium | TDD + Comprehensive Test Suite vor Launch |
| **Trig Function Edge-Cases** | 🟧 Medium | 🟩 Low | Extensive Testing mit bekannten Werten |
| **Scope Creep** | 🟧 Medium | 🟨 Medium | Klare MVP-Definition, Feature-Gate für Post-MVP |
| **Time Estimation** | 🟧 Medium | 🟩 Low | Conservative SP-Estimation, Buffers einbauen |

**Mitigation-Strategie**: TDD, Peer-Review vor Launch, Conservative Estimation mit 20% Puffer

## MVP Scope

### MUST-HAVE Features (14 Story Points)
1. ✅ UPN Parsing & Evaluation (3 SP)
2. ✅ Grundfunktionen (+, -, *, /) (3 SP)
3. ✅ Trigonometrische Funktionen (sin, cos, tan) (3 SP)
4. ✅ Interaktive CLI REPL (2 SP)
5. ✅ Stack-Management (clear, stack) (2 SP)
6. ✅ Error Handling & User Feedback (1 SP)

### SHOULD-HAVE (Post-MVP in Sprint 3)
- Help-System mit Kommando-Dokumentation (2 SP)
- Bessere Error-Messages (1 SP)
- Mathematische Precision-Dokumentation (1 SP)

### COULD-HAVE (Future Release)
- Command History mit Arrow-Keys
- Memory-Funktionen (M+, M-, MR, MC)
- Degrees/Radians Toggle
- Weitere Math-Funktionen (sqrt, log, exp)

### WON'T-HAVE (Out of Scope)
- GUI/Web-Interface (separate Initiative)
- Speichern von Kalkulationen (Complex)
- Variable & Funktionsdefinitionen (Overkill)
- Komplexe Zahlen (Out of Scope)
- Symbolisches Rechnen (Too Advanced)

## Anforderungen Übersicht

### Funktionale Anforderungen (Must-Have)
- **FR-1**: UPN-Parsing und Stack-Evaluation
- **FR-2**: Vier Grundoperationen (+, -, *, /)
- **FR-3**: Trigonometrische Funktionen (sin, cos, tan)
- **FR-4**: Interaktive CLI REPL
- **FR-5**: Stack-Display und Management

### Nicht-funktionale Anforderungen
- **NFR-1**: Performance (< 100ms/Berechnung)
- **NFR-2**: Memory Usage (< 10 MB)
- **NFR-3**: Intuitive Bedienung
- **NFR-4**: Mathematische Korrektheit (IEEE 754)
- **NFR-5**: Terminal Compatibility (macOS, Linux, Windows)
- **NFR-6**: Test Coverage (≥ 80%)

**Details**: Siehe `/PRD.md` Abschnitt 4-5

## MVP vs Post-Launch

**MVP (23. Dezember)**:
- Core-Funktionalität stabil
- Alle Must-Have Features
- Test Coverage ≥ 80%
- Dokumentation vollständig

**Post-Launch Opportunities**:
- Should-Have Features (Sprint 3)
- Community Feedback integrieren
- Future Roadmap (Q1 2026+)

## Related Documents

- **PRD**: `/PRD.md` - Vollständiges Product Requirements Document
- **STATUS**: `./STATUS.md` - Aktuelle Progress & Dependencies
- **Tasks**: `./tasks/*.md` - Detaillierte Task-Beschreibungen

## Notes

**Architecture Decisions**:
- Stack-basierte UPN-Evaluation (Standard-Pattern)
- Modularer Aufbau (Parsing, Evaluation, CLI separat)
- Minimal Dependencies (nur Python stdlib)

**Quality Standards**:
- Test-First Development (TDD)
- Peer Code Review vor Merge
- Conservative Performance Goals
- Comprehensive Error Handling

**Future Roadmap** (Q1 2026+):
- Web-Interface / GUI
- Weitere Math-Funktionen
- Memory & Storage Features
- Degrees/Radians Support

---

**Status**: 🟡 Ready for Planning
**Next Step**: Detaillierte Task-Breakdown durchführen (siehe STATUS.md)
