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
        self.max_score = 6

    def get_players_guess(self):
        """
        Get's any input needed
        """

        while True:
            self.players_guess = str(input("Please enter a letter: ")).lower()

            if len(self.players_guess) > 1:
                print("Please enter only one letter at a time")
                continue

            if not (97 <= ord(self.players_guess) <= 122):
                print("Please enter an alphabet only.")
                continue
            
            if (
                (self.players_guess in self.players_correct_guess) or  
                (self.players_guess in self.players_incorrect_guess)
               ):
                
                print("You have already guessed this character. ")
                continue


    def print_progress(self):
        """
        Checking for number of blanks to print
        """
        # Using a for loop to loop/itterate through the chosen word to see how many letters 
        # To print the number of blanks
        print("Word Progress: ", self.word_progress)
        print("Your Incorrect Guesses: ", self.players_incorrect_guess)
        print("You have ", self.max_score, "incorrect guesses remaining")


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


    def evaluating(self, selected_word):
        """
        Evaluating if the player's guess is right or wrong
        After Evaluation, the player's guess will be appended to the appropriate list. 
        """
        if self.players_guess in selected_word:
            if self.players_guess in self.players_correct_guess:
                print("please guess a letter you have not guessed yet!")

            else:
                self.players_guess.append(self.players_correct_guess)


        else:
            if self.players_guess in self.players_incorrect_guess:
                print("Please guess a letter you have not guessed yet!")
            
            else:
                self.players_guess.append(self.players_incorrect_guess)
                self.max_score = self.max_score - 1
                if self.max_score == 0:
                    print("You have guessed incorrectly 6 times, you have lost the game. GG")
                    exit()