# Example

Ein einfaches Python-Projekt als Beispiel.

## Beschreibung

Dieses Projekt dient als Vorlage für Python-Anwendungen mit moderner Projektstruktur.

## Anforderungen

- Python >= 3.13.1

## Installation

```bash
uv sync
```

## Verwendung

Das Projekt kann als Kommandozeilen-Anwendung ausgeführt werden:

```bash
python main.py
```

Oder direkt aufgerufen werden:

```bash
python -m example
```

## Projektstruktur

```
example/
├── main.py          # Haupteinstiegspunkt
├── pyproject.toml   # Projektkonfiguration
└── README.md        # Diese Datei
```

## Entwicklung

Abhängigkeiten installieren:

```bash
uv sync
```

Mit der virtuellen Umgebung arbeiten:

```bash
uv run python main.py
```

## Lizenz

MIT
