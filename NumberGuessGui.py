"""
Author: Elijah McCann
Program: numberGuessGUI.py
Chapter 8 
1/22/2024

NOTE: the module breezypythonygui.py MUST be in the same directory as this file for the app to run correctly!

GUI-based version of a number guessing game

"""

from breezypythongui import EasyFrame
import random

# Define the GuessingGame class, which is a subclass of EasyFrame
class GuessingGame(EasyFrame):

    # Constructor method to initialize the GUI
    def __init__(self):
        # Call the constructor of the EasyFrame class
        EasyFrame.__init__(self, title="Guessing Game 2.0", width=300, height=200)

        # Initialize instance variables for the game
        self.magicNumber = random.randint(1, 100)
        self.count = 0

        # Create and add widgets to the window
        self.addLabel(text="Guess a Number Between 1 and 100", row=0, column=0, columnspan=2, sticky="NSEW")
        self.addLabel(text="Your guess:", row=1, column=0)
        self.guessField = self.addIntegerField(value=0, row=1, column=1)
        self.nextButton = self.addButton(text="Next", row=2, column=0, command=self.nextGuess)
        self.newButton = self.addButton(text="New Game", row=2, column=1, command=self.newGame)

    # Method to handle user's guess and update the GUI accordingly
    def nextGuess(self):
        self.count += 1
        guess = self.guessField.getNumber()
        if guess == self.magicNumber:
            self.hintLabel["text"] = f"Hooray! You got it in {self.count} attempts!"
            self.nextButton["state"] = "disabled"
        elif guess < self.magicNumber:
            self.hintLabel["text"] = "Sorry, your guess was too low!"
        else:
            self.hintLabel["text"] = "Sorry, your guess was too high!"

    # Method to reset the game to its initial state
    def newGame(self):
        self.magicNumber = random.randint(1, 100)
        self.count = 0
        self.hintLabel["text"] = "Guess a Number Between 1 and 100"
        self.guessField.setNumber(0)
        self.nextButton["state"] = "normal"

def main():
    GuessingGame().mainloop()

if __name__ == '__main__':
    main()
