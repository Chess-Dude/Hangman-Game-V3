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
        
        # set word_progress to empty string
        self.word_progress = ""
        
        # for loop to print a dash for each character in selected word
        for character in selected_word.lower():
            # checks if character is an alphabet or digit
            if character.isalpha() or character.isdigit():                
                # checks if character is in self.players_correct_guess
                if character in self.players_correct_guess:
                    # sets (new) self.word_progress to (previous) self.word_progress + character (current letter) + "" (empty string/space)
                    self.word_progress = self.word_progress + character + " " 
                
                # if false (else) set (new) self.word_progress to (old) self.word_progress + (string with underscore and space) "_"
                else:
                    self.word_progress = self.word_progress + "_ " 
            
            # if character is not an alphabet or digit 
            else:
                self.word_progress = self.word_progress + character + " "


    def evaluating(self, selected_word, players_guess, GAME_STATE):
        """
        Evaluating if the player's guess is right or wrong and only runs if the game_status is in "GAME_IN_PROGRESS"
        After Evaluation, the player's guess will be appended to the appropriate list. 
        """

        game_status = GAME_STATE["GAME_IN_PROGRESS"]

        # checking if player guessed letter is in selected_word
        if players_guess in selected_word.lower():
            # if it is append the letter to self.players_correct_guess list
            self.players_correct_guess.append(players_guess)
            # if self.player_correct_guess list has the amount of indexes in selected_word, update game status and self.system_message
            if len(self.players_correct_guess) == len(set(selected_word.lower())):
                self.system_message = ("GG, you guessed all the letters!")
                game_status = GAME_STATE["GAME_WON"]
            
            # if player guess is valid, however the list does not have the amount of indexes in selected_word,
            # change self.system_message notifying player it was a correct guess and update game_status.
            else:
                self.system_message = ("Correct guess!")
                game_status = GAME_STATE["GAME_IN_PROGRESS"]

        # (else) if players guessed letter is not in selected_word, append the guess to players_incorrect_guess list
        else:  
            self.players_incorrect_guess.append(players_guess)
            # check if self.players_incorrect_guesses indexes == 6
            # if true, change self.system_message and update game_status
            if len(self.players_incorrect_guess) == 6:
                self.system_message = ("You hanged the man! GG") 
                game_status = GAME_STATE["GAME_LOST"]

            # if false, change self.system_message and update game status
            elif 0 < len(self.players_incorrect_guess) < 6:
                self.system_message = ("Incorrect guess. Guess again!")
                game_status = GAME_STATE["GAME_IN_PROGRESS"]

            # if some unknown error occurs
            else: 
                self.system_message = ("the program ran into some error during the incorrect_guess evaluation")
                exit()
        
        # returns game_status, to update pygame screen accordingly
        return game_status