# Chess Game - Player vs AI ♟️

## Table of Contents
- [Overview](#overview)
- [Requirements & Installation](#requirements--installation)
- [How to Run the Game](#how-to-run-the-game)
- [How to Play](#how-to-play)
- [Game Features](#game-features)
- [AI Algorithm Used](#ai-algorithm-used)
- [Screenshots](#screenshots)

## Overview

This is a Python-based Chess game where you can play against an AI opponent. The game features a beautiful graphical interface, legal move validation, and a smart AI that uses the Minimax algorithm with Alpha-Beta pruning to challenge you.

## Requirements & Installation

### Required Software:
1. **Python 3.7 or higher** - [Download Python](https://www.python.org/downloads/)
2. **Required Python libraries**

### Installation Steps:

**Step 1: Install Python**
- Download and install Python from the official website
- During installation, check "Add Python to PATH"

**Step 2: Install Required Libraries**
Open Command Prompt/Terminal and run:
```bash
pip install pygame
pip install chess
```

**Step 3: Verify Installation**
```bash
python --version
pip list | grep -E "(pygame|chess)"
```

## How to Run the Game

### Method 1: Direct Python Execution
1. **Save the code** as `chess_game.py`
2. **Open terminal/command prompt** in the same folder
3. **Run the command:**
```bash
python chess_game.py
```

### Method 2: Using Python IDLE
1. Open Python IDLE
2. Create a new file and paste the code
3. Save as `chess_game.py`
4. Press `F5` or click `Run → Run Module`

## How to Play

### Basic Controls:
- **Select Piece**: Click on any of your pieces (white pieces)
- **Move Piece**: Click on a highlighted green circle
- **Promotion**: Pawns automatically promote to Queen when reaching the opposite side

### Game Rules:
- You play as **WHITE** pieces
- AI plays as **BLACK** pieces
- Standard chess rules apply
- Game ends with checkmate, stalemate, or draw conditions

### Step-by-Step Gameplay:
1. **Start the game** - White moves first
2. **Select your piece** - Click on any white piece
3. **See legal moves** - Green circles show where you can move
4. **Make your move** - Click on a green circle
5. **Wait for AI** - The computer will respond automatically
6. **Continue playing** until game ends

### Special Moves:
- **Castling**: Move king two squares toward rook
- **En Passant**: Special pawn capture
- **Promotion**: Pawn becomes Queen at opposite side
- **Check/Checkmate**: Standard rules apply

## Game Features

### 🎨 Visual Elements:
- **Chess Board**: Traditional 8x8 grid with brown and cream colors
- **Piece Symbols**: Unicode chess symbols for beautiful display
- **Move Highlights**: 
  - Yellow border for selected piece
  - Green circles for legal moves
- **Smooth Animations**: Clean visual feedback

### ⚡ Game Mechanics:
- **Legal Move Validation**: Only allowed moves can be played
- **Automatic Promotion**: Pawns promote to Queens
- **Game State Detection**: Checkmate, stalemate, draws
- **Turn Management**: Alternates between player and AI

### 🏆 End Conditions:
- **Checkmate**: King is in check with no escape
- **Stalemate**: No legal moves but king not in check
- **Draw**: Insufficient material, repetition, or 75-move rule

## AI Algorithm Used

### 🤖 **Minimax with Alpha-Beta Pruning**

### How the AI Works:

**1. Minimax Algorithm:**
- The AI explores possible future moves
- **MAXIMIZING** for AI (tries to get highest score)
- **MINIMIZING** for player (assumes you'll make best moves)
- Looks 2 moves ahead in the current implementation

**2. Alpha-Beta Pruning:**
- **Smart shortcut** that ignores bad moves early
- **Dramatically reduces** computation time
- **Maintains optimal play** while being efficient

**3. Board Evaluation:**
```python
Piece Values:
- Pawn: 1 point
- Knight: 3 points  
- Bishop: 3 points
- Rook: 5 points
- Queen: 9 points
- King: 0 points (infinite value in practice)
```
- AI calculates material advantage
- Positive score = advantage for WHITE
- Negative score = advantage for BLACK

### AI Strengths:
- **Strategic thinking** - considers multiple moves ahead
- **Optimal play** - always chooses best available move
- **Efficient** - uses pruning to think quickly
- **Adaptive** - responds to your moves intelligently

### AI Difficulty:
- **Current depth**: 2 moves ahead
- **Can be increased** by changing `depth` parameter in `minimax()` call
- **Higher depth** = stronger AI but slower moves

## Screenshots

![Minimax_Algorithm input and output example](images/chess1.png)
![Minimax_Algorithm  input and output example](images/chess2.png)

### Game Board:
```
♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
· · · · · · · ·
· · · · · · · ·
· · · · · · · ·
· · · · · · · ·
♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
```

### Visual Description:
- **Board**: 8x8 grid with alternating brown and cream squares
- **Pieces**: Black and white chess symbols (♔♕♖♗♘♙♚♛♜♝♞♟)
- **Highlights**: 
  - Selected piece has yellow border
  - Legal moves show as green circles
- **Clean interface**: No distractions, focused on gameplay

### Game States:
- **Normal Play**: Pieces on board, turn indicator
- **Check**: King in danger (visual highlight)
- **Checkmate**: Game over screen with winner announcement
- **Draw**: Game over with draw reason

## Troubleshooting

### Common Issues:

**1. "ModuleNotFoundError: No module named 'pygame'"**
```bash
pip install pygame
```

**2. "ModuleNotFoundError: No module named 'chess'"**
```bash
pip install chess
```

**3. Game window doesn't open**
- Ensure Python and libraries installed correctly
- Check if graphics drivers are updated

**4. Pieces not displaying properly**
- Use a font that supports Unicode symbols
- The code uses "segoeuisymbol" which works on Windows

### Performance Tips:
- **Lower AI depth** if moves are too slow
- **Close other applications** for smoother performance
- **Use latest Python version** for best performance

---

**Enjoy playing chess against your smart AI opponent!** 🎯

