import tkinter as tk
import random

# Game variables
score = 0
lives = 3
symbols = ["🍒", "🍋", "🍊", "⭐", "7"]


def start_game():
    global player

    player = name.get().strip()

    if player == "":
        message.config(text="⚠️ Please enter your name!")
        return

    welcome.config(text=f"👋 Welcome, {player}!")
    name.config(state="disabled")
    start.config(state="disabled")
    spin.config(state="normal")
    message.config(text="🎰 Press SPIN to play!")


def play():
    global score, lives

    result = [random.choice(symbols) for i in range(3)]

    # Show result
    box1.config(text=result[0])
    box2.config(text=result[1])
    box3.config(text=result[2])

    # Calculate points
    if result[0] == result[1] == result[2] == "7":
        score += 200
        message.config(text="🎉 JACKPOT! +200 points!")

    elif result[0] == result[1] == result[2]:
        score += 100
        message.config(text="🏆 THREE MATCHES! +100 points!")

    elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
        score += 20
        message.config(text="✨ TWO MATCHES! +20 points!")

    else:
        score -= 5
        lives -= 1
        message.config(text="😔 No match! -5 points")

    score_label.config(text=f"🏆 Score: {score}")
    lives_label.config(text=f"❤️ Lives: {lives}")

    if lives == 0:
        spin.config(state="disabled")
        message.config(text=f"💀 Game Over, {player}! Score: {score}")
        again.pack(pady=10)


def restart():
    global score, lives

    score = 0
    lives = 3

    box1.config(text="❓")
    box2.config(text="❓")
    box3.config(text="❓")

    score_label.config(text="🏆 Score: 0")
    lives_label.config(text="❤️ Lives: 3")
    message.config(text="🎰 Press SPIN to play!")

    spin.config(state="normal")
    again.pack_forget()


# Main window
window = tk.Tk()
window.title("🎰 Mini Matching Game")
window.geometry("650x600")
window.config(bg="#17102B")


# Title
tk.Label(
    window,
    text="🎰 MINI MATCHING GAME 🎰",
    font=("Arial", 26, "bold"),
    bg="#17102B",
    fg="#FFD700"
).pack(pady=25)

tk.Label(
    window,
    text="✨ Match the symbols and earn points! ✨",
    font=("Arial", 14),
    bg="#17102B",
    fg="white"
).pack()


# Name
tk.Label(
    window,
    text="👤 Enter your name:",
    font=("Arial", 14, "bold"),
    bg="#17102B",
    fg="white"
).pack(pady=(20, 5))

name = tk.Entry(
    window,
    font=("Arial", 14),
    width=22,
    justify="center"
)
name.pack()

start = tk.Button(
    window,
    text="🚀 START GAME",
    font=("Arial", 12, "bold"),
    bg="#00C9A7",
    fg="white",
    command=start_game
)
start.pack(pady=10)


welcome = tk.Label(
    window,
    text="",
    font=("Arial", 15, "bold"),
    bg="#17102B",
    fg="#00FF99"
)
welcome.pack()


# Slot boxes
frame = tk.Frame(
    window,
    bg="#2A1B3D",
    bd=5,
    relief="ridge"
)
frame.pack(pady=25)

box1 = tk.Label(frame, text="❓", font=("Arial", 50),
                width=3, bg="#FFF8DC")
box1.grid(row=0, column=0, padx=10, pady=15)

box2 = tk.Label(frame, text="❓", font=("Arial", 50),
                width=3, bg="#FFF8DC")
box2.grid(row=0, column=1, padx=10, pady=15)

box3 = tk.Label(frame, text="❓", font=("Arial", 50),
                width=3, bg="#FFF8DC")
box3.grid(row=0, column=2, padx=10, pady=15)


# Score and lives
info = tk.Frame(window, bg="#17102B")
info.pack()

score_label = tk.Label(
    info, text="🏆 Score: 0",
    font=("Arial", 15, "bold"),
    bg="#17102B", fg="white"
)
score_label.grid(row=0, column=0, padx=30)

lives_label = tk.Label(
    info, text="❤️ Lives: 3",
    font=("Arial", 15, "bold"),
    bg="#17102B", fg="white"
)
lives_label.grid(row=0, column=1, padx=30)


# Message
message = tk.Label(
    window,
    text="👤 Enter your name to start!",
    font=("Arial", 15, "bold"),
    bg="#17102B",
    fg="#00FF99"
)
message.pack(pady=20)


# Spin button
spin = tk.Button(
    window,
    text="🎰 SPIN",
    font=("Arial", 18, "bold"),
    width=12,
    height=2,
    bg="#FFB000",
    command=play,
    state="disabled"
)
spin.pack()


# Play again
again = tk.Button(
    window,
    text="🔄 PLAY AGAIN",
    font=("Arial", 13, "bold"),
    bg="#00C9A7",
    fg="white",
    command=restart
)


window.mainloop()
