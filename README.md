# Pygame Hotel Piccolo Game

## Video

![Video](video_1.gif)

## Description

This is a [Pygame](https://www.pygame.org/docs/) game.<br />
You control the piccolo that works in a hotel.<br />

## Background

Program is developed with [Cursor](https://cursor.com/) in Python.<br />
Install Cursor, python 3 and required libraries.<br />
Run main.py in the root folder to start the program.<br />
The game is created using the 
[Mediator Pattern](https://en.wikipedia.org/wiki/Mediator_pattern),<br />
where the Mediator is notified of any actions in the game by the game<br />
objects. Mediator then notifies the relevant game objects in return to<br />
react to these actions.<br />

## Testing

Install pytest>=7.0.0<br />
Run all tests with verbose output: pytest -v<br />

## Changelog

**[0.0.1] - Jan 6. 2026:**<br />
_- Initial Upload._<br />

**[0.0.2] - Jan 8. 2026:**<br />
_- Added tests._<br />
