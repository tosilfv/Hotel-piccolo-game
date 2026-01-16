# Pygame Hotel Piccolo Game

A small Pygame-based platform game demonstrating the Mediator design pattern.

## Video

![Video](video_1.gif)
Gameplay preview.

## Description

Hotel Piccolo is a small Pygame-based platform game focused on learning clean game architecture and software design patterns in practice.

The player controls a hotel piccolo navigating different areas of a hotel environment using simple movement and jump mechanics. While the current gameplay is intentionally minimal, the project is structured to support gradual expansion with new interactions, environments, and mechanics.

From a technical perspective, the game emphasizes separation of responsibilities and testable design. User input is translated into semantic commands and routed through a Mediator, decoupling input handling from game object behavior. This makes the codebase easier to reason about, refactor, and extend as the project grows.

The primary goal of the project is educational: to explore how design patterns, clean structure, and explicit communication between components can be applied in a real, working Pygame project.

## Background

The game is developed in Python using Cursor, Visual Studio Code, and ChatGPT as development tools.
The focus of the project is on learning software design patterns, code structure, and testable architecture. 
The architecture is based on the [Mediator Pattern](https://en.wikipedia.org/wiki/Mediator_pattern), 
where user input is translated into commands that are routed through a mediator,
decoupling input handling from game object behavior.

## Architecture overview

The game loop is managed by a central Game class that orchestrates rendering, input handling, and updates.

User input is processed by an InputHandler, which converts keyboard state into semantic commands.
These commands are forwarded to a Mediator, which dispatches them to the appropriate game object methods.

Game objects such as Player and Background encapsulate their own logic and rendering,
while shared services like Screen provide display and timing functionality.

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

**[0.0.7] - Jan 15, 2026:**
- Change of outdoor backgrounds.

## License

This project is licensed under the MIT License.
