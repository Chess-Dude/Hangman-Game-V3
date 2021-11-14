"""
blits hangman images
"""

def blit_hangman_images(DISPLAYSURF, players_incorrect_guess, hangman_image_list):
    """
    Importing and blitting hangman images
    """
    
    hangman_status = len(players_incorrect_guess)
    
    DISPLAYSURF.blit(hangman_image_list[hangman_status], (130, 100))