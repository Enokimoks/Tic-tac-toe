import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x320")
root.config(bg="#74b9ff")

player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return True
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def click(row, col):
    global player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = player
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            root.destroy()
        elif all(buttons[r][c]["text"] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("Game Over", "It's a draw!")
            root.destroy()
        else:
            player = "O" if player == "X" else "X"

for r in range(3):
    for c in range(3):
        btn = tk.Button(root, text="", font="lucida 20 bold", width=5, height=2, bg="white",
                        command=lambda r=r, c=c: click(r, c))
        btn.grid(row=r, column=c, padx=5, pady=5)
        buttons[r][c] = btn

root.mainloop()
