import tkinter as tk
from tkinter import messagebox

# Initialize the board
board = [" " for _ in range(9)]
current_player = "X"
game_over = False

# Method to check if the game is over
def check_game_over():
    global game_over
    # Check for a win
    for i in range(3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != " ":
            messagebox.showinfo("Game Over", "Player " + current_player + " wins!")
            game_over = True
            return
        elif board[i] == board[i + 3] == board[i + 6] != " ":
            messagebox.showinfo("Game Over", "Player " + current_player + " wins!")
            game_over = True
            return
    if board[0] == board[4] == board[8] != " ":
        messagebox.showinfo("Game Over", "Player " + current_player + " wins!")
        game_over = True
        return
    elif board[2] == board[4] == board[6] != " ":
        messagebox.showinfo("Game Over", "Player " + current_player + " wins!")
        game_over = True
        return
    # Check for a tie
    if " " not in board:
        messagebox.showinfo("Game Over", "It's a tie!")
        game_over = True
        return

# Method to handle button clicks
def button_click(index):
    global current_player
    global game_over

    # Check if the selected position is valid
    if board[index] == " " and not game_over:
        # Update the board
        board[index] = current_player
        buttons[index].config(text=current_player, state=tk.DISABLED)

        # Check for game over conditions
        check_game_over()

        # Switch players
        current_player = "O" if current_player == "X" else "X"

        # Check if the game is over
        if game_over:
            restart_button.config(state=tk.NORMAL)

# Method to restart the game
def restart_game():
    global board
    global current_player
    global game_over

    board = [" " for _ in range(9)]
    current_player = "X"
    game_over = False

    for button in buttons:
        button.config(text=" ", state=tk.NORMAL)

    restart_button.config(state=tk.DISABLED)

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Create the buttons
buttons = []
for i in range(9):
    button = tk.Button(window, text=" ", width=10, height=5, command=lambda index=i: button_click(index))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Restart button
restart_button = tk.Button(window, text="Restart", command=restart_game, state=tk.DISABLED)
restart_button.grid(row=3, columnspan=3)

# Run the event loop
window.mainloop()
