"""
Name: Rayyan Lodhi
Date: October 28th 
Program Name: HangmanGUI.py, GameProgressModule, WordSelectionModule.py, TopicDictionary.json
Purpose: Big Gaming Assignment - runs a graphical user interface of Hangman 
Change log: Rayyan Lodhi - November 11th added comments
"""

# imports
import sys 
import pygame 
from pygame.locals import * 
import WordSelectionModule
import GameProgressModule
from BlittingHangManImages import blit_hangman_images
from DrawingLetters import draw_letters

# initializes pygame
pygame.init()

# display size
WIDTH = 979
HEIGHT = 472

# FPS
FPS = 30

# Declaring font types
TITLE_FONT = pygame.font.SysFont('comicsans', 80)
SUB_TITLE_FONT = pygame.font.SysFont('comicsans', 60)
WORD_FONT = pygame.font.SysFont('comicsans', 55)
LETTER_FONT_SIZE = 40
LETTER_FONT = pygame.font.SysFont('comicsans', LETTER_FONT_SIZE)
SYSTEM_FONT_MESSAGE = pygame.font.SysFont('comicsans', 30)
HELP_FONT_MESSAGE = pygame.font.SysFont('comicsans', 20)

# setting up color objects
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (255, 0, 0)
RED = (0, 255, 77)

# Drawing/making circles/letters variables
RADIUS = 30
GAP = 10
TOTAL_WIDTH = RADIUS * 2 + GAP
LINE_THICKNESS = 3
FIRST_CIRCLE_X = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2) + RADIUS + (GAP / 2)
FIRST_CIRCLE_Y_ROW_1 = 350
FIRST_CIRCLE_Y_ROW_2 = 420

# creating grid for letters variables
GRID_LEFT_X1 = 35
GRID_RIGHT_X2 = WIDTH - 35
PADDING = GAP / 2
GRID_MID_Y = 385
GRID_Y1 = 350 - RADIUS - PADDING
GRID_Y2 = 420 + RADIUS + PADDING
ASCII_A = 65
COLUMN_WIDTH = (RADIUS * 2) + GAP # this should be 70 

GAME_STATE = {
                "START_MENU": 0,  
                "GAME_IN_PROGRESS": 1,
                "GAME_WON": 2,
                "GAME_LOST": 3,
                "GAME_HELP": 4
             }
game_status = 0

# help button variables
HELP_X = WIDTH - 150
HELP_Y = 40
HELP_WIDTH = 100
HELP_HEIGHT = 20
        

def get_letter(m_x, m_y, letters_to_print):
    """
    Determines what button is pressed
    """

    player_guess = None
    column_number = (((m_x - GRID_LEFT_X1) / COLUMN_WIDTH) + 1) 
    column_number = int(column_number)
    top_row = False

    # determining if mouse button is in grid (if a button is pressed) via mouse pressed coordinates
    if ((GRID_LEFT_X1 <= m_x < GRID_RIGHT_X2) and (GRID_Y1 <= m_y <= GRID_Y2)):

        # determining what row the mouse was clicked
        # if mouse y coordinate was greater than the 
        if m_y > GRID_MID_Y:
            top_row = False 

        elif m_y < GRID_MID_Y:
            top_row = True

        # if mouse was clicked in top row
        if top_row:
            player_guess = str(chr(column_number + ASCII_A - 1)) # subtract 1 due to column number starting from 1, not 0 

        # else (if mouse was clicked in bottom row)
        else:
            player_guess = str(chr(column_number + ASCII_A + 13 - 1))


    if (player_guess is not None) and (letters_to_print[player_guess]):
        return player_guess
        

    else:
        return None


def blitting_text(DISPLAYSURF, word_progress, selected_topic, system_message):
    """
    blits/renders text
    """

    word_text = WORD_FONT.render(word_progress, 1, BLACK)
    DISPLAYSURF.blit(word_text, word_text.get_rect(center = DISPLAYSURF.get_rect().center))
    
    topic_text = SUB_TITLE_FONT.render(("Topic: " + selected_topic), 1, BLACK) 
    DISPLAYSURF.blit(topic_text, (WIDTH/2 - topic_text.get_width()/2, 75))

    system_message_text = SYSTEM_FONT_MESSAGE.render(system_message, 1, BLACK)
    DISPLAYSURF.blit(system_message_text, (WIDTH/2 - system_message_text.get_width()/2, 150))

    help_text_button = HELP_FONT_MESSAGE.render("Click Here For Help", 1, BLACK)
    DISPLAYSURF.blit(help_text_button, (WIDTH - 150, 40))
    help_text_width, helpt_text_height = help_text_button.get_size()


def blitting_start_menu(DISPLAYSURF):
    """
    blits start menu
    """
    clicking_anywhere = WORD_FONT.render("click anywhere to play", 1, BLACK)
    DISPLAYSURF.blit(clicking_anywhere, (WIDTH/2 - clicking_anywhere.get_width()/2, HEIGHT / 2))


def blitting_help_menu(DISPLAYSURF):
    """
    blitting help_menu
    """

    DISPLAYSURF.fill(WHITE)  
    game_help_menu =    "Rules:\nThis game will be a remake of the classic game Hangman!\n\n"
    game_help_menu =    game_help_menu + "Objective:\n" 
    game_help_menu =    game_help_menu + "The computer/system randomizes a topic and a word from that topic. The users/players must try to guess the word by guessing letters (clicking the on-screen letters)."
    game_help_menu =    game_help_menu + "Each incorrect guess brings the user/player closer to being hanged (6 lives)." 
    game_help_menu =    game_help_menu + "\n\nClick Anywhere to go back." 

    words = [word.split(' ') for word in game_help_menu.splitlines()]  # 2D array where each row is a list of words.

    space = WORD_FONT.size(' ')[0]  # The width of a space.

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

def changing_game_status():
    """

    """

def refresh_screen(DISPLAYSURF, 
                   letters_to_print, 
                   word_progress, 
                   players_incorrect_guess, 
                   selected_topic, 
                   system_message, 
                   hangman_image_list):
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
        blitting_start_menu(DISPLAYSURF)
    
    elif game_status == GAME_STATE["GAME_IN_PROGRESS"]:
        blitting_text(DISPLAYSURF, word_progress, selected_topic, system_message)
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
        blitting_text(DISPLAYSURF, word_progress, selected_topic, system_message)
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
        blitting_text(DISPLAYSURF, word_progress, selected_topic, system_message)
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
        blitting_help_menu(DISPLAYSURF)
        
    else:
        system_message_text = "An unexpected error has occured. Game status is out of range."
        sys.exit()

def main():
    """
    Main game loop
    """
    # game_status starts in START_MENU
    global game_status

    # printing purpose
    print("Purpose: Big Gaming Assignment - runs a graphical user interface of Hangman \n Change log: Rayyan Lodhi - November 11th added comments")
    
    # creating objects
    word_selection_obj = WordSelectionModule.WordSelection()
    game_progress_obj = GameProgressModule.GameProgress()
    
    # calling updating_progress method
    game_progress_obj.updating_progress(word_selection_obj.selected_word)
    
    # Assign FPS a value
    frame_per_sec = pygame.time.Clock()
   
    # Setup a 979x472 pixel display with caption
    DISPLAYSURF = pygame.display.set_mode(size=(WIDTH, HEIGHT))
    pygame.display.set_caption("Hangman")
    
    # load all 7 images here so it only needs to be once
    hangman_image_list = []
    for i in range(7):
        hangman_image = pygame.image.load("hangman" + str(i) + ".png")
        hangman_image_list.append(hangman_image)


    # append all letters of alphabet to letters_to_print dictionary (used in drawing_letters)
    letters_to_print = {}
    for letter in range(0, 26):
        letters_to_print[chr(65 + letter)] = True

    # refreshing screen to show inital display
    refresh_screen(DISPLAYSURF, 
                   letters_to_print, 
                   game_progress_obj.word_progress, 
                   game_progress_obj.players_incorrect_guess, 
                   word_selection_obj.selected_topic, 
                   game_progress_obj.system_message, 
                   hangman_image_list)
    
    pygame.display.update()
    
    # this is the START_MENU
    game_status = GAME_STATE["START_MENU"]
    start_flag = False
    while not start_flag:
        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit event occured")
                pygame.quit()
                sys.exit()

            # checking if mouse was clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                start_flag = True


    # GAME_IN_PROGRESS loop
    game_status = GAME_STATE["GAME_IN_PROGRESS"]
    while True:

        player_guess = None

        # Update game display so the user can see
        pygame.display.update()

        # checking if exit event occured
        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit event occured")
                pygame.quit()
                sys.exit()
            
            # if game status is set to the help menu we dont want to supervise the game in progress and 
            # we want to wait until we exit the GAME_HELP screen to return to supervising the GAME_IN_PROGRESS screen
            if game_status == GAME_STATE["GAME_HELP"]:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_status = GAME_STATE["GAME_IN_PROGRESS"]

            elif game_status == GAME_STATE["GAME_WON"]:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()

            elif game_status == GAME_STATE["GAME_LOST"]:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()

            else:

                # checking if mouse was clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # getting where mouse was clicked (coords)
                    m_x, m_y = pygame.mouse.get_pos()
                    
                    # checks if help button is pressed (via coordinate values)
                    if ((HELP_X < m_x < (HELP_X + HELP_WIDTH)) and 
                        (HELP_Y < m_y < (HELP_Y + HELP_HEIGHT))): 
                        
                        game_status = GAME_STATE["GAME_HELP"]
                    
                    # if help button has not be pressed, check for player_guess since there should be no 
                    # overlap between the guesses and help button
                    else: 
                        # getting player guess
                        player_guess = get_letter(m_x, m_y, letters_to_print)
                        # settings the letter value that was guessed to "false" (to not print)
                        letters_to_print[player_guess] = False

                # calling methods from GameProgress class to evaluate and update the progress/score            
                if player_guess is not None:
                    game_status = game_progress_obj.evaluating(word_selection_obj.selected_word, player_guess.lower(), GAME_STATE)
                    game_progress_obj.updating_progress(word_selection_obj.selected_word) 
        
            refresh_screen(DISPLAYSURF, 
                           letters_to_print, 
                           game_progress_obj.word_progress, 
                           game_progress_obj.players_incorrect_guess, 
                           word_selection_obj.selected_topic, 
                           game_progress_obj.system_message, 
                           hangman_image_list)
        
        frame_per_sec.tick(FPS)

if __name__ == "__main__":
    main()


# refactor
# comment code
