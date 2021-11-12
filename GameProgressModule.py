"""
Get's Player's input and sends input to other classes
"""

import random
import sys # helps with systems level commands (exiting programs, gettings command line info)
import pygame 
from pygame.locals import * 

class GameProgress:
    """
    Takes input from player. Processes the input, formats the output text.
    """

    def __init__(self):
        self.players_guess = ""
        self.players_incorrect_guess = []
        self.players_correct_guess = []
        self.word_progress = ""
        self.system_message = ""


    def get_players_guess(self, players_guess):
        """
        Get's user input
        """
        while True:

            self.players_guess = players_guess

            if (
                (self.players_guess in self.players_correct_guess) or  
                (self.players_guess in self.players_incorrect_guess)
                ):
                print("You have already guessed this character. ")
                continue

            else:
                break


    def print_progress(self):
        """
        Checking for number of blanks to print
        """
        # Using a for loop to loop/itterate through the chosen word to see how many letters 
        # To print the number of blanks

        # text = pygame_drawing_shapes.LETTER_FONT.render(("Word Progress: ", self.word_progress), 1, pygame_drawing_shapes.BLACK)
       #  pygame_drawing_shapes.DISPLAYSURF.blit(text, (pygame_drawing_shapes.WITDTH/2 - text.get_width()/2, 20))
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


    def evaluating(self, selected_word, players_guess):
        """
        Evaluating if the player's guess is right or wrong
        After Evaluation, the player's guess will be appended to the appropriate list. 
        If players guess is repeated, it'll be solved in another method (get_players_guess)
        """

        if players_guess in selected_word.lower():
            self.players_correct_guess.append(players_guess)
            if len(self.players_correct_guess) == len(set(selected_word.lower())):
                print("Word Progress: ", selected_word)
                self.system_message = ("GG, you guessed all the letters sucessfully! You win!")
                exit()
            
            else:
                print("Correct guess!")


        else:  
            self.players_incorrect_guess.append(players_guess)
            if len(self.players_incorrect_guess) == 6:
                print(self.players_incorrect_guess)
                self.system_message = ("You have hit 6 wrong guesses - you hanged the man! GG")
                print(selected_word, self.players_correct_guess, self.players_incorrect_guess) 
                exit()

            elif 0 < len(self.players_incorrect_guess) < 6:
                self.system_message = ("Incorrect guess. Guess again!")

            else: 
                self.system_message = ("the program ran into some error during the incorrect_guess evaluation")
                exit()