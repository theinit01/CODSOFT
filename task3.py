import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")

        self.choices = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Rock, Paper, Scissors", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Choice Buttons
        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play("rock"))
        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play("paper"))
        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play("scissors"))

        self.rock_button.pack(side=tk.LEFT, padx=10)
        self.paper_button.pack(side=tk.LEFT, padx=10)
        self.scissors_button.pack(side=tk.LEFT, padx=10)

        # Result Label
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        # Score Label
        self.score_label = tk.Label(self.root, text="User: 0 | Computer: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        # Play Again Button
        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)
        self.update_scores(result)
        self.display_result(user_choice, computer_choice, result)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "win"
        else:
            return "lose"

    def update_scores(self, result):
        if result == "win":
            self.user_score += 1
        elif result == "lose":
            self.computer_score += 1

    def display_result(self, user_choice, computer_choice, result):
        result_message = f"User chose: {user_choice}\nComputer chose: {computer_choice}\n"
        if result == "win":
            result_message += "You win!"
        elif result == "lose":
            result_message += "You lose!"
        else:
            result_message += "It's a tie!"

        self.result_label.config(text=result_message)
        self.score_label.config(text=f"User: {self.user_score} | Computer: {self.computer_score}")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.result_label.config(text="")
        self.score_label.config(text="User: 0 | Computer: 0")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
