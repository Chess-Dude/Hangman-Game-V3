"""
Get's Player's input and sends input to other classes
"""

class GameProgress:
    """
    Takes input from player. Processes the input, formats the output text.
    """

    def __init__(self):
        """
        Constructor function that defines needed data structures
        """
        self.players_guess = ""
        self.players_incorrect_guess = []
        self.players_correct_guess = []
        self.word_progress = ""
        self.system_message = ""


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


    def evaluating(self, selected_word, players_guess, GAME_STATE):
        """
        Evaluating if the player's guess is right or wrong
        After Evaluation, the player's guess will be appended to the appropriate list. 
        If players guess is repeated, it'll be solved in another method (get_players_guess)
        """

        game_status = GAME_STATE["GAME_IN_PROGRESS"]

        if players_guess in selected_word.lower():
            self.players_correct_guess.append(players_guess)
            if len(self.players_correct_guess) == len(set(selected_word.lower())):
                self.system_message = ("GG, you guessed all the letters!")
                game_status = GAME_STATE["GAME_WON"]
            
            else:
                self.system_message = ("Correct guess!")
                game_status = GAME_STATE["GAME_IN_PROGRESS"]

        else:  
            self.players_incorrect_guess.append(players_guess)
            if len(self.players_incorrect_guess) == 6:
                self.system_message = ("You hanged the man! GG") 
                game_status = GAME_STATE["GAME_LOST"]

            elif 0 < len(self.players_incorrect_guess) < 6:
                self.system_message = ("Incorrect guess. Guess again!")
                game_status = GAME_STATE["GAME_IN_PROGRESS"]

            else: 
                self.system_message = ("the program ran into some error during the incorrect_guess evaluation")
                exit()
        
        return game_status