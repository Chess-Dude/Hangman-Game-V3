"""
blits help menu once help menu button is clicked
"""

def blitting_help_menu(DISPLAYSURF, WHITE, WORD_FONT, BLACK):
    """
    blitting help_menu
    """

    # fills background with white (to hide any game progress)
    DISPLAYSURF.fill(WHITE)

    # sets game_help_menu variable (a long string of the rules and objective)  
    game_help_menu =    "Rules:\nThis game will be a remake of the classic game Hangman!\n\n"
    game_help_menu =    game_help_menu + "Objective:\n" 
    game_help_menu =    game_help_menu + "The computer/system randomizes a topic and a word from that topic. The users/players must try to guess the word by guessing letters (clicking the on-screen letters)."
    game_help_menu =    game_help_menu + "Each incorrect guess brings the user/player closer to being hanged (6 lives)." 
    game_help_menu =    game_help_menu + "\n\nClick Anywhere to go back." 

    # 2D array where each row is a list of words.
    words = [word.split(' ') for word in game_help_menu.splitlines()]  

    # The width of a space.
    space = WORD_FONT.size(' ')[0]  

    # gettubg max display size and position
    max_width, max_height = DISPLAYSURF.get_size()
    pos = (0, 0)
    x, y = pos

    for line in words:

        for word in line:

            help_box = WORD_FONT.render(word, 0, BLACK)

            word_width, word_height = help_box.get_size()

            if x + word_width >= max_width:

                x = pos[0]  # Reset the x.

                y += word_height  # Start on new row.

            DISPLAYSURF.blit(help_box, (x, y))

            x += word_width + space

        x = pos[0]  # Reset the x.

        y += word_height  # Start on new row.    
