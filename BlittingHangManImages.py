"""
blits hangman images
"""

def blit_hangman_images(DISPLAYSURF, players_incorrect_guess, hangman_image_list):
    """
    Importing and blitting hangman images
    """
    # sets hangman_status to the amount of indexes in players_incorrect_guesses
    hangman_status = len(players_incorrect_guess)
    # blits the following image depending on total of players_incorrect_guess indexes (is a list) 
    DISPLAYSURF.blit(hangman_image_list[hangman_status], (130, 100))