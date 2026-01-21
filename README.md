# Pygame Hotel Piccolo Game

Kaikki sankarit ei juokse ilmassa.
Jotkut boingaa arvokkaasti tasajalkaa 🐸

Tervetuloa kumiukkopiccolon maailmaan - hotellin pikkoloon, jonka tavaramerkki on legendaarinen tasajalkahyppy.
“Legendan mukaan Tasajalka-Boing™ on muinainen taito, jonka Piccolo oppi Sifulta.” 🐸

A small Pygame-based platform game demonstrating the [Mediator design pattern](https://en.wikipedia.org/wiki/Mediator_pattern).

## Video

![Gameplay preview](video_1.gif)

## Description

Hotel Piccolo is a small Pygame-based platform game focused on learning clean game architecture and software design patterns in practice.

The player controls a hotel piccolo navigating different areas of a hotel environment using simple movement and jump mechanics. While the current gameplay is intentionally minimal, the project is structured to support gradual expansion with new interactions, environments, and mechanics.

From a technical perspective, the game emphasizes separation of responsibilities and testable design. User input is translated into semantic commands and routed through a Mediator, decoupling input handling from game object behavior. This makes the codebase easier to reason about, refactor, and extend as the project grows.

The primary goal of the project is educational: to explore how design patterns, clean structure, and explicit communication between components can be applied in a real, working Pygame project.

The game is developed in Python using Pygame, with modern development tools such as Visual Studio Code, Cursor, and ChatGPT used to support iterative design and refactoring. The primary focus of the project is learning software design patterns, clean code structure, and testable architecture rather than building a feature-complete game.

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

**[0.0.8] - Jan 18, 2026:**
- Added piccolo run images.

**[0.0.9] - Jan 20, 2026:**
- Added boing. “Hetki jolloin Piccolo oppi muinaisemman taidon: Tasajalka-Boing™.” 🐸

## License

This project is licensed under the MIT License.
