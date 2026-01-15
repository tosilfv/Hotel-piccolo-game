# Pygame Hotel Piccolo Game

A small Pygame-based platform game demonstrating the Mediator design pattern.

## Video

![Video](video_1.gif)
Gameplay preview.

## Description

This is a small game built with Pygame.  
You control a piccolo working in a hotel environment.

## Background

The game is developed in Python using Cursor, Visual Studio Code, and ChatGPT.  
The architecture is based on the [Mediator Pattern](https://en.wikipedia.org/wiki/Mediator_pattern),  
where game objects communicate indirectly through a central mediator.

## Installation

Install Python 3.10 or newer.

Install required libraries from the project root directory:
```bash
pip install pygame pytest
```

## Running the game

Run the following command from the project root directory:
```bash
python main.py
```

## Testing

All unit tests are written using pytest.
Run the full test suite with verbose output:
```bash
pytest -v
```

## Changelog

**[0.0.1] - Jan 6, 2026:**
- Initial upload.

**[0.0.2] - Jan 8, 2026:**
- Added tests.

**[0.0.3] - Jan 9, 2026:**
- Added Player class.

**[0.0.4] - Jan 11, 2026:**
- Added piccolo left and right movement.

**[0.0.5] - Jan 12, 2026:**
- Added piccolo jump.

**[0.0.6] - Jan 13, 2026:**
- Refactor.

## License

This project is licensed under the MIT License.
