# -------------------------------
# Tic Tac Toe Game (Player vs AI) using Tkinter
# -------------------------------

# Import Tkinter for GUI and messagebox for pop-up alerts
import tkinter as tk
from tkinter import messagebox

# -------------------------------
# Constants and Initial Setup
# -------------------------------
PLAYER = "X"  # Human player
AI = "O"      # Computer AI

# Initialize a 3x3 board with empty strings
board = [["" for _ in range(3)] for _ in range(3)]

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# -------------------------------
# Minimax Algorithm for AI
# -------------------------------
def minimax(board, depth, is_maximizing):
    """
    Minimax recursive function to calculate best move for AI
    """
    winner = check_winner(board)
    if winner == AI:
        return 1      # AI wins
    elif winner == PLAYER:
        return -1     # Player wins
    elif is_full(board):
        return 0      # Tie

    # Depth limit for faster response
    if depth >= 2:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = AI
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = PLAYER
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ""
                    best_score = min(score, best_score)
        return best_score

# -------------------------------
# Calculate and Make the Best AI Move
# -------------------------------
def best_move():
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = AI
                score = minimax(board, 0, False)
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        make_move(move[0], move[1], AI)

# -------------------------------
# Check Winner Function
# -------------------------------
def check_winner(b):
    """
    Check rows, columns, diagonals for a winner
    """
    for i in range(3):
        # Row check
        if b[i][0] == b[i][1] == b[i][2] != "":
            return b[i][0]
        # Column check
        if b[0][i] == b[1][i] == b[2][i] != "":
            return b[0][i]
    # Diagonal check
    if b[0][0] == b[1][1] == b[2][2] != "":
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != "":
        return b[0][2]
    return None

# -------------------------------
# Check if Board is Full (Tie)
# -------------------------------
def is_full(b):
    for row in b:
        for cell in row:
            if cell == "":
                return False
    return True

# -------------------------------
# Make a Move
# -------------------------------
def make_move(i, j, player):
    """
    Make a move for player or AI
    """
    if board[i][j] == "":
        board[i][j] = player
        buttons[i][j]["text"] = player

        winner = check_winner(board)
        if winner:
            messagebox.showinfo("Game Over", f"{winner} wins!")
            reset_board()
        elif is_full(board):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_board()
        # If human played, then AI makes a move after a short delay
        elif player == PLAYER:
            root.after(200, best_move)

# -------------------------------
# Reset Board Function
# -------------------------------
def reset_board():
    """
    Reset the board and button texts
    """
    global board
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""

# -------------------------------
# Create GUI Buttons
# -------------------------------
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(
            root,
            text="",
            font=("Arial", 40),
            width=5,
            height=2,
            command=lambda i=i, j=j: make_move(i, j, PLAYER)  # Call when player clicks
        )
        buttons[i][j].grid(row=i, column=j)

# -------------------------------
# Start the Tkinter Main Loop
# -------------------------------
root.mainloop()
