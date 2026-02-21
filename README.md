# Accent Game

Interactive voice-based accent classification game built with SpeechBrain and Streamlit.

## Features
- Real-time voice recording
- ML-powered accent classification
- Interactive scoring system
- Phonetic coaching tips

## Setup

1. Install dependencies:
```bash
poetry install
```

2. Run the game:
```bash
poetry run streamlit run src/accent_game/app.py
```

## Development

Run tests:
```bash
poetry run pytest
```

## Project Structure
- `src/accent_game/` - Main application code
- `tests/` - Unit tests
- `models/` - Trained models and configs
- `data/` - Training datasets and preprocessing scripts
