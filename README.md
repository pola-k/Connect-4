# Connect 4 Game

## Overview

This is a Python implementation of the classic **Connect 4** game using the Pygame library. The game can be played between two players locally, where the objective is to connect four of your pieces either horizontally, vertically, or diagonally on a 6x7 grid before your opponent.

## Features
- Two-player gameplay (Player 1 vs Player 2).
- Visual representation of the game board using circles (red for Player 1, yellow for Player 2).
- Turn-based system where each player alternates placing their pieces in any available column.
- Automatic checking for win conditions: horizontal, vertical, and diagonal.
- Declares a winner or a draw when all slots are filled.

## Prerequisites

- Python 3.x
- Pygame

You can install Pygame using pip:

```bash
pip install pygame
```

## How to Play

1. Clone or download the repository.
2. Open the terminal in the project folder and run the script:
```bash
python connect4.py
```
3. A game window will open with a blue background representing the board.
4. Click on the columns to drop your piece.
5. The game alternates between Player 1 (red) and Player 2 (yellow).
6. The game ends when one player connects 4 pieces in a row, column, or diagonally, or when all slots are filled resulting in a draw.

## Game Controls

- **Mouse Click**: Choose the column where you want to drop your piece.

## Code Structure

- **initialise()**: Initializes the game board as a 6x7 grid filled with zeros (empty slots).
- **change_turns()**: Alternates turns between Player 1 and Player 2.
- **check_winner()**: Checks for a winning condition (4 consecutive pieces) in the rows, columns, or diagonals.
- **play()**: Handles the placement of a piece on the board, updates the board, and checks for a win.
- **display_board()**: Visualizes the game board with circles representing the state of the board.

## Win Conditions

A player wins if they connect four of their pieces consecutively in:
- A row (horizontal).
- A column (vertical).
- A diagonal.

---

Enjoy the game!
