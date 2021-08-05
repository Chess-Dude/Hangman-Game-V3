"""
Get's Player's input and sends input to other classes
"""

import random
import re


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
            self.players_guess = str(input("Please enter a letter: ")).lower

            for letters in self.players_guess:
                total = total + 1
        

            if total > 1:
                print("")

            else: break
    

    def print_progress(self):
        """
        Checking for number of blanks to print
        """
        # Using a for loop to loop/itterate through the chosen word to see how many letters 
        # To print the number of blanks
        print("Word Progress: ", self.word_progress)
        print("Your Incorrect Guesses: ", self.players_incorrect_guess)


    def updating_progress(self, selected_word):
        """
        Updating the correct guesses of the player
        """
        
        self.word_progress = ""
        for character in selected_word:
            
            if character.isalpha() or character.isdigit():                
                if character in self.players_correct_guess:
                    self.word_progress = self.word_progress + character + " " 
                
                else:
                    self.word_progress = self.word_progress + "_ " 
            else:
                self.word_progress = self.word_progress + character + " "


    def evaluating(self):
        """
        Evaluating if the player's guess is right or wrong
        After Evaluation, the player's guess will either be 
        """
        def find(string):
            special_char=re.compile('[@_!$%^&*()<>?/\|}{~:]#')
    
            if special_char.search(self.players_guess) == None:
                return "Your Guess is Valid"
            
            else:
                return "Your Guess is Invalid"
        


