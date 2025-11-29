# Contributing to UPN Calculator

Vielen Dank für Ihr Interesse an diesem Projekt! 🎉

## Wie Sie beitragen können

### Issues melden

- Nutzen Sie die [Issue Templates](https://github.com/dsenften/upn-calculator/issues/new/choose) für Bug Reports oder Feature Requests
- Durchsuchen Sie zuerst bestehende Issues, um Duplikate zu vermeiden
- Geben Sie so viele Details wie möglich an

### Code beitragen

1. **Fork erstellen**
   ```bash
   # Repository forken über GitHub UI
   git clone https://github.com/YOUR_USERNAME/upn-calculator.git
   cd upn-calculator
   ```

2. **Feature-Branch erstellen**
   ```bash
   git checkout -b feature/mein-feature
   # oder
   git checkout -b fix/mein-bugfix
   ```

3. **Änderungen vornehmen**
   - Folgen Sie dem bestehenden Code-Stil
   - Schreiben Sie Tests für neue Funktionalität
   - Aktualisieren Sie die Dokumentation falls nötig

4. **Tests ausführen**
   ```bash
   uv sync
   uv run pytest
   uv run ruff check .
   ```

5. **Commit erstellen**
   - Verwenden Sie aussagekräftige Commit-Messages
   - Folgen Sie dem [Conventional Commits](https://www.conventionalcommits.org/) Format:
     ```
     feat: Neue Funktion hinzugefügt
     fix: Bug behoben
     docs: Dokumentation aktualisiert
     test: Tests hinzugefügt
     refactor: Code refactored
     ```

6. **Pull Request erstellen**
   - Pushen Sie Ihren Branch zu Ihrem Fork
   - Erstellen Sie einen PR gegen den `main` Branch
   - Füllen Sie das PR-Template vollständig aus
   - Warten Sie auf Code Review

## Entwicklungsumgebung

### Voraussetzungen

- Python >= 3.13.1
- [uv](https://github.com/astral-sh/uv) (empfohlen) oder pip

### Setup

```bash
# Mit uv (empfohlen)
uv sync

# Tests ausführen
uv run pytest

# Linting
uv run ruff check .
uv run ruff format .
```

## Code-Stil

- Wir verwenden [Ruff](https://github.com/astral-sh/ruff) für Linting und Formatting
- Alle Funktionen sollten Docstrings haben
- Type Hints werden empfohlen

## Pull Request Richtlinien

- PRs müssen alle CI-Checks bestehen
- PRs benötigen mindestens eine Approval
- PRs sollten auf einen Fokus beschränkt sein
- Große Änderungen sollten vorher als Issue diskutiert werden

## Fragen?

Bei Fragen erstellen Sie gerne ein Issue oder kontaktieren Sie den Maintainer.

Vielen Dank für Ihren Beitrag! 🙏

