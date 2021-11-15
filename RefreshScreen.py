"""
Refreshes/updates game
"""

import sys
from BlittingHangManImages import blit_hangman_images
from DrawingLetters import draw_letters
from BlittingText import blitting_text
from BlittingStartMenu import blitting_start_menu
from BlittingHelpMenu import blitting_help_menu

def refresh_screen(DISPLAYSURF, 
                   letters_to_print, 
                   word_progress, 
                   players_incorrect_guess, 
                   selected_topic, 
                   system_message, 
                   hangman_image_list, 
                   WHITE, 
                   TITLE_FONT, 
                   BLACK, 
                   WIDTH, 
                   game_status, 
                   GAME_STATE, 
                   WORD_FONT, 
                   HEIGHT, 
                   SUB_TITLE_FONT, 
                   SYSTEM_FONT_MESSAGE, 
                   HELP_FONT_MESSAGE,
                   FIRST_CIRCLE_X, 
                   FIRST_CIRCLE_Y_ROW_1, 
                   FIRST_CIRCLE_Y_ROW_2,  
                   LETTER_FONT, 
                   LETTER_FONT_SIZE, 
                   RADIUS, 
                   LINE_THICKNESS, 
                   TOTAL_WIDTH):
    """
    refreshes screen
    """
    
    # Loading Background Images
    # DISPLAYSURF.blit(BACKGROUND, (0, 0))
    DISPLAYSURF.fill(WHITE)  

    # Printing Text
    title_text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    DISPLAYSURF.blit(title_text, (WIDTH/2 - title_text.get_width()/2, 20))

    # depending on current game status, the display will be updated based on game state
    if game_status == GAME_STATE["START_MENU"]:
        blitting_start_menu(DISPLAYSURF, WORD_FONT, BLACK, WIDTH, HEIGHT)
    
    elif game_status == GAME_STATE["GAME_IN_PROGRESS"]:
        blitting_text(DISPLAYSURF, 
                      word_progress, 
                      selected_topic, 
                      system_message, 
                      WORD_FONT, BLACK, 
                      SUB_TITLE_FONT, 
                      WIDTH, 
                      SYSTEM_FONT_MESSAGE, 
                      HELP_FONT_MESSAGE)

        # callling functions to blit hangman images and draw letters/buttons
        blit_hangman_images(DISPLAYSURF, players_incorrect_guess, hangman_image_list)
        draw_letters(DISPLAYSURF, 
                     letters_to_print, 
                     FIRST_CIRCLE_X, 
                     FIRST_CIRCLE_Y_ROW_1, 
                     FIRST_CIRCLE_Y_ROW_2, 
                     BLACK, 
                     LETTER_FONT, 
                     LETTER_FONT_SIZE, 
                     RADIUS, 
                     LINE_THICKNESS, 
                     TOTAL_WIDTH)

    elif game_status == GAME_STATE["GAME_WON"]:
        blitting_text(DISPLAYSURF, 
                      word_progress, 
                      selected_topic, 
                      system_message, 
                      WORD_FONT, BLACK, 
                      SUB_TITLE_FONT, 
                      WIDTH, 
                      SYSTEM_FONT_MESSAGE, 
                      HELP_FONT_MESSAGE)

        # callling functions to blit hangman images and draw letters/buttons
        blit_hangman_images(DISPLAYSURF, players_incorrect_guess, hangman_image_list)
        draw_letters(DISPLAYSURF, 
                     letters_to_print, 
                     FIRST_CIRCLE_X, 
                     FIRST_CIRCLE_Y_ROW_1, 
                     FIRST_CIRCLE_Y_ROW_2, 
                     BLACK, 
                     LETTER_FONT, 
                     LETTER_FONT_SIZE, 
                     RADIUS, 
                     LINE_THICKNESS, 
                     TOTAL_WIDTH)

    elif game_status == GAME_STATE["GAME_LOST"]:
        blitting_text(DISPLAYSURF, 
                      word_progress, 
                      selected_topic, 
                      system_message, 
                      WORD_FONT, BLACK, 
                      SUB_TITLE_FONT, 
                      WIDTH, 
                      SYSTEM_FONT_MESSAGE, 
                      HELP_FONT_MESSAGE)

        # callling functions to blit hangman images and draw letters/buttons
        blit_hangman_images(DISPLAYSURF, players_incorrect_guess, hangman_image_list)
        draw_letters(DISPLAYSURF, 
                     letters_to_print, 
                     FIRST_CIRCLE_X, 
                     FIRST_CIRCLE_Y_ROW_1, 
                     FIRST_CIRCLE_Y_ROW_2, 
                     BLACK, 
                     LETTER_FONT, 
                     LETTER_FONT_SIZE, 
                     RADIUS, 
                     LINE_THICKNESS, 
                     TOTAL_WIDTH)

    elif game_status == GAME_STATE["GAME_HELP"]:
        blitting_help_menu(DISPLAYSURF, WHITE, WORD_FONT, BLACK)
        
    else:
        system_message_text = "An unexpected error has occured. Game status is out of range."
        sys.exit()