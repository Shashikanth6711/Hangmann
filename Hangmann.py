import tkinter as tk
import random


class HangmanGame:
    def _init_(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.word = self.choose_word()
        self.guesses = []
        self.remaining_attempts = 6

        self.word_label = tk.Label(self.master, text=self.display_word())
        self.word_label.pack()

        self.guess_entry = tk.Entry(self.master)
        self.guess_entry.pack()

        self.submit_button = tk.Button(self.master, text="Guess", command=self.process_guess)
        self.submit_button.pack()

        self.message_label = tk.Label(self.master, text="")
        self.message_label.pack()

    def choose_word(self):
        words = ["apple", "banana", "orange", "grape", "strawberry", "pineapple"]
        return random.choice(words)

    def display_word(self):
        displayed_word = ""
        for letter in self.word:
            if letter in self.guesses:
                displayed_word += letter
            else:
                displayed_word += "_"
        return displayed_word

    def process_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            self.message_label.config(text="Please enter a single letter.")
            return

        if guess in self.guesses:
            self.message_label.config(text="You already guessed that letter.")
            return

        self.guesses.append(guess)

        if guess not in self.word:
            self.remaining_attempts -= 1
            if self.remaining_attempts == 0:
                self.message_label.config(text=f"Sorry, you lost! The word was '{self.word}'.")
                self.submit_button.config(state=tk.DISABLED)
            else:
                self.message_label.config(text=f"Incorrect guess! {self.remaining_attempts} attempts remaining.")
        else:
            self.message_label.config(text="Correct guess!")

        self.word_label.config(text=self.display_word())


def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()


if _name_ == "_main_":
    main()