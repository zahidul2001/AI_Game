# -------------------------------
# NIM Game with Minimax AI using Tkinter
# -------------------------------

import tkinter as tk
from tkinter import messagebox
from random import randint 

# -------------------------------
# Game Configuration / Constants
# -------------------------------
stone_symbol = "🥚"   # Visual representation of a stone
max_take = 5          # Maximum stones a player can take per turn
AI_DEPTH = 6          # Depth limit for Minimax AI (controls difficulty)

# Random initial number of stones
n = randint(40, 70)

# -------------------------------
# Minimax Algorithm with Depth Limit
# -------------------------------
def minimax_depth(stones, maximizing, depth):
    """
    Minimax algorithm with depth limit:
    - 'stones' = remaining stones
    - 'maximizing' = True if AI's turn
    - 'depth' = remaining search depth to prevent deep recursion
    Returns a score: +1 (AI wins), -1 (Player wins)
    """
    # Base case: game over or depth limit reached
    if stones == 0 or depth == 0:
        return -1 if maximizing else 1

    if maximizing:  # AI's turn
        best_score = -999
        for take in range(1, min(max_take, stones) + 1):
            score = minimax_depth(stones - take, False, depth - 1)
            best_score = max(best_score, score)
        return best_score
    else:           # Player's turn
        best_score = 999
        for take in range(1, min(max_take, stones) + 1):
            score = minimax_depth(stones - take, True, depth - 1)
            best_score = min(best_score, score)
        return best_score

# -------------------------------
# GUI Helper Functions
# -------------------------------
def enable_buttons():
    """Enable all take buttons"""
    for btn in take_buttons:
        btn.config(state="normal")

def disable_buttons():
    """Disable all take buttons"""
    for btn in take_buttons:
        btn.config(state="disabled")

# -------------------------------
# AI Move Function
# -------------------------------
def ai_move():
    """
    AI calculates best move using minimax and updates the board.
    Also updates status messages and checks for game over.
    """
    global n
    disable_buttons()  # Disable buttons while AI is thinking
    status.config(text="AI is thinking...")
    root.update_idletasks()  # Refresh GUI

    best_score = -999
    best_take = 1

    # Evaluate all possible moves for AI
    for take in range(1, min(max_take, n) + 1):
        score = minimax_depth(n - take, False, AI_DEPTH)
        if score > best_score:
            best_score = score
            best_take = take

    n -= best_take
    update()  # Update GUI with new stone count
    last_move.config(text=f"AI took: {best_take} stone{'s' if best_take > 1 else ''}")

    # Check if AI won
    if n == 0:
        messagebox.showinfo("Result", "💻 AI Wins!")
        reset_game()
    else:
        status.config(text="Your turn!")
        enable_buttons()  # Player can play

# -------------------------------
# Player Move Function
# -------------------------------
def player_take(x):
    """
    Handles player's move when a button is clicked.
    x = number of stones player wants to take
    """
    global n
    if x < 1 or x > min(max_take, n):
        messagebox.showinfo("Invalid", f"You can take between 1 and {min(max_take, n)} stones.")
        return

    disable_buttons()
    n -= x
    update()
    last_move.config(text=f"You took: {x} stone{'s' if x > 1 else ''}")

    # Check if player won
    if n == 0:
        messagebox.showinfo("Result", "🎉 You Win!")
        reset_game()
        return

    # AI plays after short delay
    root.after(400, ai_move)

# -------------------------------
# Update GUI Functions
# -------------------------------
def update():
    """Updates stone count and visual display of stones"""
    lbl.config(text=f"Stones left: {n}")
    stones_box.config(state="normal")
    stones_box.delete(1.0, tk.END)

    per_line = 12  # stones per line for display
    full = stone_symbol * n
    lines = [full[i:i + per_line] for i in range(0, len(full), per_line)]
    stones_box.insert(tk.END, "\n".join(lines))
    stones_box.config(state="disabled")

def reset_game():
    """Reset the game to a new random number of stones"""
    global n
    n = randint(40, 70)
    update()
    status.config(text="Your turn!")
    last_move.config(text="AI took: -")
    enable_buttons()

# -------------------------------
# GUI Setup
# -------------------------------
root = tk.Tk()
root.title("NIM GAME (Minimax AI)")
root.geometry("640x640")
root.resizable(False, False)

# Colors
bg_color = "#dadfe7"
panel_color = "#0b1220"
accent = "#B37321"
text_fg = "#0e861e"
root.configure(bg=bg_color)

# Title
tk.Label(root, text="🥚 NIM GAME", font=("Arial", 20, "bold"),
         bg=bg_color, fg=accent).pack(pady=(12, 6))

# Stones left label
lbl = tk.Label(root, font=("Consolas", 16, "bold"), bg=bg_color, fg="#d31e2d")
lbl.pack(pady=(4, 6))

# Stones display box
frame_box = tk.Frame(root, bg=panel_color, bd=2, relief="groove")
frame_box.pack(padx=18, pady=8, fill="both", expand=False)

stones_box = tk.Text(frame_box, font=("Consolas", 18), bg=panel_color, fg="#c2beb6",
                     wrap="char", height=6, width=28, relief="flat", state="disabled")
stones_box.pack(padx=8, pady=8)

# Status and last move
status = tk.Label(root, text="Your turn!", bg=bg_color, fg="#12db48", font=("Arial", 12, "bold"))
status.pack(pady=(8, 4))

last_move = tk.Label(root, text="AI took: -", bg=bg_color, fg=text_fg, font=("Arial", 12))
last_move.pack(pady=(2, 8))

# Buttons frame
frame = tk.Frame(root, bg=bg_color)
frame.pack(pady=6)

take_buttons = []
for i in range(1, max_take + 1):
    btn = tk.Button(frame, text=f"Take {i}", font=("Arial", 12, "bold"),
                    bg="#eca41e", fg="white", width=8,
                    activebackground="#b20849",
                    command=lambda x=i: player_take(x))
    btn.grid(row=0, column=i - 1, padx=6, pady=6)
    take_buttons.append(btn)

# Reset button
reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 11, "bold"),
                      bg="#9b8f8f", fg="white", width=14, command=reset_game)
reset_btn.pack(pady=(12, 4))

# -------------------------------
# Start Game
# -------------------------------
root.after(100, ai_move)  # AI can start first optionally
update()
enable_buttons()
root.mainloop()
