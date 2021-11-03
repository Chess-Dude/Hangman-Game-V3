"""
Get's Player's input and sends input to other classes
"""

import random


class GameProgress:
    """
    Takes input from player. Processes the input, formats the output text.
    """

    
    def __init__(self):
        self.players_guess = ""
        self.players_incorrect_guess = []
        self.players_correct_guess = []
        self.word_progress = ""

    def get_players_guess(self):
        """
        Get's any input needed
        """

        while True:

            try:
                self.players_guess = str(input("Please enter a letter of the English alphabet: ")).lower()

                if ((not self.players_guess.isalpha()) or 
                    (len(self.players_guess) > 1)
                    ):
                    
                    raise TypeError

            except TypeError:
                print("Incorrect Input! You Entered: %s. Please enter one letter of the English alphabet." % (self.players_guess))
            
            else:
                 
                if (
                    (self.players_guess in self.players_correct_guess) or  
                    (self.players_guess in self.players_incorrect_guess)
                     ):
                    print("You have already guessed this character. ")
                    
                else:
                    break

    def print_progress(self):
        """
        Checking for number of blanks to print
        """
        # Using a for loop to loop/itterate through the chosen word to see how many letters 
        # To print the number of blanks
        print("Word Progress: ", self.word_progress)
        print("Your Incorrect Guesses: ", self.players_incorrect_guess)
        print("You have ", (6 - len(self.players_incorrect_guess)), "incorrect guesses remaining")


    def updating_progress(self, selected_word):
        """
        Updating the correct guesses of the player
        """
        
        self.word_progress = ""
        for character in selected_word.lower():
            
            if character.isalpha() or character.isdigit():                
                if character in self.players_correct_guess:
                    self.word_progress = self.word_progress + character + " " 
                
                else:
                    self.word_progress = self.word_progress + "_ " 
            else:
                self.word_progress = self.word_progress + character + " "


    def evaluating(self, selected_word):
        """
        Evaluating if the player's guess is right or wrong
        After Evaluation, the player's guess will be appended to the appropriate list. 
        If players guess is repeated, it'll be solved in another method (get_players_guess)
        """
        if self.players_guess in selected_word.lower():
            self.players_correct_guess.append(self.players_guess)
            if len(self.players_correct_guess) == len(set(selected_word.lower())):
                print("Word Progress: ", selected_word)
                print("GG, you guessed all the letters sucessfully! You win!")
                exit()
            
            else:
                print("Correct guess!")


        else:  
            self.players_incorrect_guess.append(self.players_guess)
            if len(self.players_incorrect_guess) == 6:
                print("You have hit 6 wrong guesses - you hanged the man! GG")
                exit()

            elif 0 < len(self.players_incorrect_guess) < 6:
                print("Incorrect guess. Guess again!")

            else: 
                print("the program ran into some error during the incorrect_guess evaluation")
                exit()