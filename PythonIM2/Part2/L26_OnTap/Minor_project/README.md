https://realpython.com/pygame-a-primer/
## Basic Game Design

The goal of the game is to avoid incoming obstacles:
    The player starts on the left side of the screen.
    The obstacles enter randomly from the right and move left in a straight line.
The player can move left, right, up, or down to avoid the obstacles.
The player cannot move off the screen.
The game ends either when the player is hit by an obstacle or when the user closes the window.

## Setting Up the Game Loop

Processes user input
Updates the state of all game objects
Updates the display and audio output
Maintains the speed of the game

## Events

event.type
    keypresses: KEYDOWN/KEYRELEASE
    window closure: QUIT

## Using surface
