# NIM Game - Player vs AI 🥚

## 1. How to Run the Code (Run Instructions)

### Method 1: Using Command Line/Terminal
```bash
# Save the code as nim_game.py
python nim_game.py
```

### Method 2: Using Python IDLE
1. Open Python IDLE
2. Create new file and paste the code
3. Save as `nim_game.py`
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
# Random module is also built-in

# Verification Command:
python --version
```

**Note:** This game uses only Python's built-in libraries:
- `tkinter` for the graphical interface
- `random` for generating random numbers
- `messagebox` for popup dialogs

## 3. How to Play the Game

### Game Basics:
- **Objective**: Avoid taking the last stone
- **You play against AI**: Take turns removing stones
- **Starting Stones**: 40-70 random eggs (🥚)
- **Maximum Take**: 5 stones per turn

### Game Rules:
- **Players Alternate**: You → AI → You → AI
- **Take 1-5 Stones**: Click buttons to take stones
- **Losing Condition**: Player who takes the LAST stone LOSES
- **Winning Strategy**: Force opponent to take the last stone

### Step-by-Step Gameplay:
1. **Start the game** - Window opens with random number of eggs
2. **Your turn** - Click "Take 1" to "Take 5" buttons
3. **AI responds** - Computer automatically makes its move
4. **Continue playing** - Alternate turns
5. **Game result** - Popup shows who took the last stone (loser)
6. **Play again** - Click "Reset Game" to start new game

### Controls:
- **Take 1**: Remove 1 stone
- **Take 2**: Remove 2 stones
- **Take 3**: Remove 3 stones
- **Take 4**: Remove 4 stones
- **Take 5**: Remove 5 stones
- **Reset Game**: Start new game with new random stones

## 4. Game Screenshots & Visual Description

![NIM_Game image 1](images/NIM_Game1.png)
![NIM_Gameimage 2](images/NIM_Game2.png)
![NIM_Gameimage 3](images/NIM_Game3.png)

### Game Interface Layout:
```
🥚 NIM GAME
Stones left: 45

[🥚🥚🥚🥚🥚🥚🥚🥚🥚🥚🥚🥚]
[🥚🥚🥚🥚🥚🥚🥚🥚🥚🥚🥚🥚]
[🥚🥚🥚🥚🥚🥚🥚🥚🥚🥚🥚🥚]
[🥚🥚🥚🥚🥚🥚🥚🥚🥚]

Your turn!
AI took: -

[Take 1] [Take 2] [Take 3] [Take 4] [Take 5]
[Reset Game]
```

### Visual Elements:
- **Title**: "🥚 NIM GAME" in large bold font
- **Stone Counter**: Red number showing remaining stones
- **Stone Display**: Egg symbols (🥚) arranged in rows
- **Status Message**: "Your turn!" or "AI is thinking..."
- **Last Move**: Shows what each player took last
- **Take Buttons**: Orange buttons numbered 1-5
- **Reset Button**: Gray button to restart game

### Color Scheme:
- **Background**: Light blue-gray (#dadfe7)
- **Stone Panel**: Dark blue-black (#0b1220)
- **Buttons**: Orange (#eca41e)
- **Text**: Green for status (#12db48), red for stone count (#d31e2d)

## 5. AI Algorithm Used

### 🤖 **Minimax Algorithm with Depth Limiting**

### How the AI Works:

**1. Minimax Algorithm:**
- **Purpose**: Finds the optimal move to force player to take last stone
- **Depth**: Looks 6 moves ahead (AI_DEPTH = 6)
- **Strategy**: 
  - **MAXIMIZING** for AI (tries to get best position)
  - **MINIMIZING** for player (assumes you'll make best moves)

**2. Scoring System:**
```python
If AI wins (player takes last stone): +1
If Player wins (AI takes last stone): -1
Depth limit reached: 0 (neutral)
```

**3. Decision Process:**
- AI evaluates all possible moves (1-5 stones)
- Simulates future game states up to 6 moves deep
- Chooses move with highest guaranteed score
- Always plays to force player into losing position

### AI Features:
- **Strategic**: Plans multiple moves ahead
- **Adaptive**: Responds to your moves intelligently
- **Optimal**: Makes mathematically best decisions
- **Fast**: Computes moves quickly with depth limiting

### Algorithm Code Structure:
```python
def minimax_depth(stones, maximizing, depth):
    if stones == 0: return -1 if maximizing else 1
    if depth == 0: return 0
    
    if maximizing:
        find move with highest score
    else:
        find move with lowest score
```

## Game Features

### 🎮 User Experience:
- **Visual Stone Display**: Egg symbols make it engaging
- **Clear Status Updates**: Always know whose turn it is
- **Move History**: See what each player took last
- **Smooth Transitions**: Buttons disable during AI thinking

### ⚡ Technical Features:
- **Input Validation**: Prevents taking more stones than available
- **Random Starting**: Different stone count each game (40-70)
- **Responsive UI**: Buttons enable/disable appropriately
- **Game State Management**: Tracks turns and results accurately

### 🏆 Game Outcomes:
- **Player Wins**: "🎉 You Win!" (AI took last stone)
- **AI Wins**: "💻 AI Wins!" (You took last stone)
- **Automatic Reset**: Game restarts after completion

## Game Strategy Tips

### Winning Strategies:
- **Control the Endgame**: Aim to leave 1 stone for opponent
- **Mathematical Pattern**: Target positions where (stones % (max_take+1)) == 1
- **Force Moves**: Make moves that limit opponent's options
- **Think Ahead**: Consider what positions you'll leave for AI

### Common Patterns:
- If stones = 6, 12, 18, 24... you're in losing position
- Always try to leave stones in multiples of (max_take+1) + 1 for opponent

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
- Make sure it's your turn (status says "Your turn!")
- AI might be thinking (status says "AI is thinking...")

**4. Egg symbols not displaying**
- Use a modern operating system that supports emoji
- The game uses Unicode egg symbol (🥚)

## Why This Game is Interesting

### Educational Value:
- **Perfect Minimax Example**: Demonstrates game tree search
- **Mathematical Game**: Based on modular arithmetic principles
- **AI Concepts**: Shows how computers solve combinatorial games

### Historical Significance:
- **Ancient Game**: One of the oldest known mathematical games
- **AI Milestone**: Early computer game used in AI research
- **Strategy Game**: Teaches planning and foresight

### Challenge Level:
- **Difficult to Beat**: AI uses optimal strategy
- **Learning Curve**: Easy to learn, hard to master
- **Strategic Depth**: Simple rules but complex strategy

---

**Enjoy this classic mathematical game against a smart AI opponent!** 🎯
