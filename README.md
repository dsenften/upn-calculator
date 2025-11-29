# UPN Calculator

Ein Beispielprojekt für modernen Python-Workflow mit Claude Code.

## Beschreibung

Dieses Projekt implementiert einen Calculator für Umgekehrte Polnische Notation (UPN) und dient als Referenzbeispiel für die Verwendung des Claude Code Workflows mit den dotfiles von [talent-factory/dotfiles](https://github.com/talent-factory/dotfiles).

## Workflow-Demo

Dieses Projekt demonstriert den kompletten Entwicklungs-Workflow:

1. **PRD erstellen** - Mit `/project:create-prd` wurde das Product Requirements Document erstellt
2. **Projektplan generieren** - Mit `/project:create-plan-fs` wurde aus dem PRD ein strukturierter Projektplan erstellt
3. **Tasks implementieren** - Mit `/develop:implement-fs-task` wurden die einzelnen Tasks umgesetzt

Siehe CLAUDE.md für detaillierte Informationen zum Workflow und zur Verwendung mit Claude Code.

## Anforderungen

- Python >= 3.13.1

## Installation

```bash
uv sync
```

## Verwendung

Das Projekt kann als Python-Modul verwendet werden:

```python
from upn_calculator.calculator import Calculator

calc = Calculator()
result = calc.evaluate("3 4 +")
print(result)  # 7.0
```

## Projektstruktur

```
upn-calculator/
├── .plans/                        # Filesystem-basierte Task-Verwaltung
│   └── upn-taschenrechner-cli/
│       ├── EPIC.md               # Epic-Beschreibung
│       ├── PRD.md                # Product Requirements Document
│       ├── STATUS.md             # Projekt-Status
│       └── tasks/                # Individuelle Task-Dateien
│           ├── task-001-upn-parser-core.md
│           ├── task-002-grundoperationen.md
│           └── ...
├── upn_calculator/               # Quellcode
│   ├── __init__.py
│   ├── calculator.py             # Haupt-Calculator
│   ├── errors.py                 # Error-Handling
│   ├── operators.py              # Operatoren-Implementierung
│   └── parser.py                 # UPN-Parser
├── tests/                        # Tests
│   ├── test_calculator.py
│   └── test_grundoperationen.py
├── pyproject.toml                # Projektkonfiguration
├── README.md                     # Diese Datei
└── CLAUDE.md                     # Claude Code Workflow-Dokumentation
```

## Verwendeter Workflow

Dieses Projekt wurde mit dem Claude Code Workflow aus den [talent-factory/dotfiles](https://github.com/talent-factory/dotfiles) entwickelt:

### 1. PRD erstellen

Der initiale Prompt war einfach:

```bash
/project:create-prd "Ich benötige ein CLI Program oder konkret ein UPN Taschenrechner, welche neben den Grundfunktionen auch sin(), cos() und tan() kennt."
```

Aus dieser natürlichsprachlichen Beschreibung generiert Claude automatisch ein umfassendes PRD mit:
- Problem Statement
- Funktionalen und nicht-funktionalen Anforderungen
- Technischen Spezifikationen
- Success Criteria

### 2. Projektplan generieren

```bash
/project:create-plan-fs
```

Dies erstellt die `.plans/` Struktur mit:

- `EPIC.md` - Epic-Beschreibung
- `PRD.md` - Product Requirements Document
- `STATUS.md` - Projekt-Status
- `tasks/` - Einzelne Task-Dateien

### 3. Tasks implementieren

```bash
/develop:implement-fs-task
```

Für jeden Task wird:

- Ein Feature-Branch erstellt
- Der Code implementiert
- Tests geschrieben
- Ein Pull Request erstellt

### Weitere Workflow-Kommandos

- `/develop:commit` - Professionelle Git-Commits erstellen
- `/develop:create-pr` - Pull Requests mit automatischer Beschreibung
- `/develop:ruff-check` - Python-Code linting und formatting

## Entwicklung

Abhängigkeiten installieren:

```bash
uv sync
```

Tests ausführen:

```bash
uv run pytest
```

## Lizenz

MIT
