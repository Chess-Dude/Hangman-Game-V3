"""
Blits start menu for the game status: START_MENU
"""

def blitting_start_menu(DISPLAYSURF, WORD_FONT, BLACK, WIDTH, HEIGHT):
    """
    blits start menu
    """
    # instantiates text to "cick anywhere to play" then blits clicking_anywhere text
    clicking_anywhere = WORD_FONT.render("click anywhere to play", 1, BLACK)
    DISPLAYSURF.blit(clicking_anywhere, (WIDTH/2 - clicking_anywhere.get_width()/2, HEIGHT / 2))