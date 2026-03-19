# Tic Tac Toe Game - Player vs AI ❌⭕

## 1. How to Run the Code (Run Instructions)

### Method 1: Using Command Line/Terminal
```bash
# Save the code as tic_tac_toe.py
python tic_tac_toe.py
```

### Method 2: Using Python IDLE
1. Open Python IDLE
2. Create new file and paste the code
3. Save as `tic_tac_toe.py`
4. Press `F5` or click `Run → Run Module`

### Method 3: Using VS Code or Other Editors
1. Open the code in your editor
2. Make sure Python extension is installed
3. Press `Ctrl+F5` (Run without debugging)

## 2. Required Software & Libraries

### Must Install First:

**Python 3.6 or higher**
- Download from: https://www.python.org/downloads/
- During installation, check "Add Python to PATH"

**Required Python Libraries:**
```bash
# Tkinter comes built-in with Python (no need to install separately)
# Only need to verify Python installation

# Verification Command:
python --version
```

**Note:** Tkinter is included with standard Python installations. If you get Tkinter errors, you may need to:
- On Windows: Reinstall Python and check "tcl/tk" during installation
- On Mac: Tkinter is included by default
- On Linux: Install with `sudo apt-get install python3-tk`

## 3. How to Play the Game

### Game Basics:
- **You play as X** (Player)
- **AI plays as O** (Computer)
- **You go first** - click any empty square to start

### Game Rules:
- **Objective**: Get 3 of your marks in a row (horizontal, vertical, or diagonal)
- **Turns Alternate**: Player → AI → Player → AI
- **Game Ends**: When someone wins or all squares are filled

### Step-by-Step Gameplay:
1. **Start the game** - Window opens with 3x3 grid
2. **Make your move** - Click any empty square
3. **AI responds** - Computer automatically makes its move
4. **Continue playing** - Alternate turns until game ends
5. **Game result** - Popup shows winner or tie
6. **Play again** - Game automatically resets after result

### Controls:
- **Mouse**: Click squares to place your X
- **Automatic**: No keyboard controls needed

## 4. Game Screenshots & Visual Description

![tic_tac_toe1 game image screenshort](images/tic_tac_toe1.png)
![tic_tac_toe1 game image screenshort](images/tic_tac_toe2.png)

### Game Board Layout:
```
[ ] [ ] [ ]
[ ] [ ] [ ] 
[ ] [ ] [ ]
```

### Visual Elements:
- **3x3 Grid**: 9 buttons arranged in rows and columns
- **Player Mark**: "X" appears in blue (default color)
- **AI Mark**: "O" appears in blue (default color)
- **Buttons**: Large clickable areas with clear text
- **Font**: Arial size 40 for clear visibility

### Game States:
- **Start**: All squares empty
- **Mid-game**: Mix of X and O marks
- **Win**: Three same marks in a row
- **Tie**: All squares filled with no winner

## 5. AI Algorithm Used

### 🤖 **Minimax Algorithm**

### How the AI Works:

**1. Minimax Algorithm:**
- **Purpose**: Finds the optimal move for the AI
- **Depth**: Looks 2 moves ahead in the game tree
- **Strategy**: 
  - **MAXIMIZING** for AI (tries to get best score)
  - **MINIMIZING** for player (assumes you'll make best moves)

**2. Scoring System:**
```python
AI Wins: +1 point
Player Wins: -1 point  
Tie: 0 points
```

**3. Decision Process:**
- AI evaluates all possible moves
- Simulates future game states
- Chooses move with highest guaranteed score
- Always plays optimally

### AI Features:
- **Unbeatable**: With perfect play, cannot lose (can only win or tie)
- **Strategic**: Blocks player wins and creates its own threats
- **Fast**: Computes moves quickly due to small search space
- **Optimal**: Always makes the mathematically best move

### Algorithm Code Structure:
```python
def minimax(board, depth, is_maximizing):
    if AI wins: return 1
    if Player wins: return -1
    if tie: return 0
    
    if maximizing:
        find move with highest score
    else:
        find move with lowest score
```

## Game Features

### 🎮 User Experience:
- **Simple Interface**: Clean 3x3 grid
- **Instant Feedback**: Immediate response to clicks
- **Clear Results**: Popup messages for game outcomes
- **Auto-Reset**: Game restarts automatically after completion

### ⚡ Technical Features:
- **Legal Move Validation**: Prevents invalid moves
- **Win Detection**: Checks all possible winning combinations
- **Tie Detection**: Identifies when board is full
- **Smooth Gameplay**: No delays or lag

### 🏆 Game Outcomes:
- **Player Wins**: "X wins!" message
- **AI Wins**: "O wins!" message  
- **Tie Game**: "It's a tie!" message

## Troubleshooting

### Common Issues:

**1. "Tkinter not found" error**
```bash
# On Windows: Reinstall Python with Tkinter support
# On Linux: 
sudo apt-get install python3-tk
# On Mac: Usually included by default
```

**2. Game window doesn't open**
- Check if Python is properly installed
- Verify file is saved with .py extension
- Ensure no syntax errors in code

**3. Buttons not responding**
- Make sure you're clicking empty squares
- Check if game is waiting for AI move

**4. AI moves too slowly**
- Normal behavior - AI is calculating optimal move
- Usually takes less than 1 second

## Why This Game is Interesting

### Educational Value:
- **Perfect Minimax Example**: Demonstrates classic AI algorithm
- **Simple but Deep**: Easy to understand, hard to master
- **Algorithm Visualization**: See AI thinking process in action

### Challenge Level:
- **Impossible to Beat**: With perfect play from both sides, always ends in tie
- **Great for Learning**: Understand game tree search concepts
- **Foundation for Complex AI**: Same principles used in chess, checkers, etc.

---

**Enjoy playing against an unbeatable AI opponent!** 🎯
