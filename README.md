# Accent Game

An interactive voice-based accent classification game. Record yourself speaking in different accents and let the ML model guess which accent you're attempting. Built with SpeechBrain for accent classification and Streamlit for the UI.

## Features

- Real-time voice recording via browser microphone
- ML-powered accent classification using SpeechBrain pre-trained models
- Interactive scoring system with difficulty progression
- Phonetic coaching tips to improve your accent attempts
- Multiple accent targets to attempt

## Tech Stack

- **ML:** SpeechBrain (accent classification models)
- **UI:** Streamlit
- **Audio:** Real-time browser recording and processing
- **Build:** Poetry for dependency management

## Getting Started

### Install

```bash
poetry install
```

### Run

```bash
poetry run streamlit run src/accent_game/app.py
```

### Test

```bash
poetry run pytest
```

## Project Structure

```
src/accent_game/    # Main application code
tests/              # Unit tests
models/             # Trained models and configs
data/               # Training datasets and preprocessing scripts
```

## How It Works

1. The app presents a target accent (e.g., British, Australian, Southern US)
2. You record yourself speaking a given phrase in that accent
3. SpeechBrain's accent classifier analyzes your recording
4. You get scored on how close your attempt matches the target
5. Phonetic tips help you improve for the next round
