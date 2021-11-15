"""
Name: Rayyan Lodhi
Date: October 28th 
Program Name: HangmanGUI.py, GameProgressModule, WordSelectionModule.py, TopicDictionary.json
Purpose: Big Gaming Assignment - runs a graphical user interface of Hangman 
Change log: Rayyan Lodhi - November 14th Refactored code
"""

# imports
import sys 
import pygame 
from pygame.locals import * 
import WordSelectionModule
import GameProgressModule
from BlittingHangManImages import blit_hangman_images
from DrawingLetters import draw_letters
from GetLetter import get_letter
from BlittingText import blitting_text
from BlittingStartMenu import blitting_start_menu
from BlittingHelpMenu import blitting_help_menu
from RefreshScreen import refresh_screen

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

# game status variables
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


def main():
    """
    Main game loop
    """
    # game_status starts in START_MENU
    global game_status

    # printing purpose
    print("Purpose: Big Gaming Assignment - runs a graphical user interface of Hangman \nChange log: Rayyan Lodhi - November 14th Refactored code\nFull Change log can be viewed here: https://github.com/Chess-Dude/Hangman-Game-V3")
    
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
                   word_selection_obj, 
                   game_progress_obj.system_message, 
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
                   TOTAL_WIDTH)
    
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
                        player_guess = get_letter(m_x, 
                                                  m_y, 
                                                  letters_to_print, 
                                                  GRID_LEFT_X1, 
                                                  COLUMN_WIDTH, 
                                                  GRID_RIGHT_X2, 
                                                  GRID_Y1, 
                                                  GRID_Y2, 
                                                  GRID_MID_Y, 
                                                  ASCII_A)
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
                   TOTAL_WIDTH)
        
        frame_per_sec.tick(FPS)

if __name__ == "__main__":
    main()