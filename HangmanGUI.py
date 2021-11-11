import os # help with getting/formatting file path locations
import sys # helps with systems level commands (exiting programs, gettings command line info)
import time 
import pygame 
from pygame.locals import * 
import WordSelectionModule
import GameProgressModule

pygame.init()

# display size
WIDTH = 979
HEIGHT = 472
# BACKGROUND = pygame.image.load('hangmanbackgroundtest.jpg')

# FPS
FPS = 30

# Declaring font types
TITLE_FONT = pygame.font.SysFont('comicsans', 70)
WORD_FONT = pygame.font.SysFont('comicsans', 55)
LETTER_FONT_SIZE = 40
LETTER_FONT = pygame.font.SysFont('comicsans', LETTER_FONT_SIZE)


# setting up color objects
WHITE = (0, 0, 0)
BLACK = (0, 0, 0)
GREEN = (255, 0, 0)
RED = (0, 255, 77)

# Drawing/making circles/letters
RADIUS = 30
GAP = 10
TOTAL_WIDTH = RADIUS * 2 + GAP
LINE_THICKNESS = 3
FIRST_CIRCLE_X = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2) + RADIUS + (GAP / 2)
FIRST_CIRCLE_Y_ROW_1 = 350
FIRST_CIRCLE_Y_ROW_2 = 420

# creating grid for letters
X1 = 35
X2 = WIDTH - 35
PADDING = GAP / 2
Y_MID = 385
Y1 = 350 - RADIUS - PADDING
Y2 = 420 + RADIUS + PADDING
ASCII_A = 65
COLUMN_WIDTH = (RADIUS * 2) + GAP # this should be 70 


def load_hangman_images(DISPLAYSURF, players_incorrect_guess):
    """
    Import hangman images
    """
    # players_incorrect_guess is a list of incorrect guesses from the GameProgressModule class/file, which was imported and
    # passed as a parameter to this function 
    hangman_image_list = []
    hangman_status = len(players_incorrect_guess)
    for i in range(7):
        hangman_image = pygame.image.load("hangman" + str(i) + ".png")
        hangman_image_list.append(hangman_image)
        DISPLAYSURF.blit(hangman_image_list[hangman_status], (150, 100))

    

def draw_letters(DISPLAYSURF, letters_to_print):
    """
    to find the corrects values I used  the following formula:
    (width of screen - (radius of circcle + gap between circles)(# of alphabets/2)/2)
    This gave me the leftover pixels for each side, 34.5 which rounds up to 35.
    This info allowed me to start drawing from the left side of the first circle.
    Note that to draw the circle, we must give the draw.circle method the coordinate range, thius adding half the gap + half the diameter of the circle. 
    refer to the official documentation of the code below:    
    """

    x_circle_coord = FIRST_CIRCLE_X
    y_circle_coord_row_1 = FIRST_CIRCLE_Y_ROW_1
    y_circle_coord_row_2 = FIRST_CIRCLE_Y_ROW_2

    for i in range(13):

        if letters_to_print[chr(65 + i)]:
            
            # Drawing letter for top row
            pygame.draw.circle(DISPLAYSURF, WHITE, (x_circle_coord, y_circle_coord_row_1), RADIUS, LINE_THICKNESS)
            letters = LETTER_FONT.render(chr(65 + i), 1, WHITE)
            DISPLAYSURF.blit(letters, (x_circle_coord - (LETTER_FONT_SIZE / 4), y_circle_coord_row_1 - (LETTER_FONT_SIZE / 4)))  

        if letters_to_print[chr(78 + i)]: 
            # Drawing letter for bottom row
            pygame.draw.circle(DISPLAYSURF, WHITE, (x_circle_coord, y_circle_coord_row_2), RADIUS, LINE_THICKNESS)
            letters = LETTER_FONT.render(chr(78 + i), 1, WHITE)
            DISPLAYSURF.blit(letters, (x_circle_coord - (LETTER_FONT_SIZE / 4), y_circle_coord_row_2 - (LETTER_FONT_SIZE / 4)))         
            
        x_circle_coord = x_circle_coord + TOTAL_WIDTH


def get_letter(m_x, m_y, letters_to_print):
    """
    Returns letter that is clicked on
    """
    player_guess = None
    
    column_number = (((m_x - X1) / COLUMN_WIDTH) + 1) 
    column_number = int(column_number)
    
    top_row = False

    if ((X1 <= m_x < X2) and (Y1 <= m_y <= Y2)):
        print("in grid")

        if m_y > Y_MID:
            print("mouse pos > 385, bottom row")
            top_row = False 

        elif m_y < Y_MID:
            print("mouse pos < 385, top row")
            top_row = True


        if top_row:
            player_guess = str(chr(column_number + ASCII_A - 1)) # subtract 1 due to column number starting from 1, not 0 

        else:
            player_guess = str(chr(column_number + ASCII_A + 13 - 1))


    if (player_guess is not None) and (letters_to_print[player_guess]):
        print(player_guess)
        return player_guess
        

    else:
        return None


def refresh_screen(DISPLAYSURF, letters_to_print, word_progress, players_incorrect_guess):
    """
    """
    
    # Loading Background Images
    # DISPLAYSURF.blit(BACKGROUND, (0, 0))
    DISPLAYSURF.fill((100, 100, 100))  

    # Printing Title
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    DISPLAYSURF.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    text = WORD_FONT.render(word_progress, 1, BLACK)
    DISPLAYSURF.blit(text, (WIDTH / 2, HEIGHT / 2))
    
    load_hangman_images(DISPLAYSURF, players_incorrect_guess)
    draw_letters(DISPLAYSURF, letters_to_print)


def main():
    """
    Main game loop
    Do not run outside this module, as it initializes the pygame here.
    """

    word_selection_obj = WordSelectionModule.WordSelection()
    game_progress_obj = GameProgressModule.GameProgress()
    game_progress_obj.updating_progress(word_selection_obj.selected_word) 

    # Assign FPS a value

    frame_per_sec = pygame.time.Clock()

    
    # Setup a 979x472 pixel display with caption
    # set the screen size according to the background image proportions.

    DISPLAYSURF = pygame.display.set_mode(size=(WIDTH, HEIGHT))
    pygame.display.set_caption("Hangman")
    

    letters_to_print = {}
    for letter in range(0, 26):
        letters_to_print[chr(65 + letter)] = True


    refresh_screen(DISPLAYSURF, letters_to_print, game_progress_obj.word_progress, game_progress_obj.players_incorrect_guess)
    pygame.display.update()
    
    
    while True:
        # Run game
        player_guess = None

        # Update game display so the user can see
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit event occured")
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                print(m_x, m_y)
                player_guess = get_letter(m_x, m_y, letters_to_print)
                letters_to_print[player_guess] = False
            
            if player_guess is not None:
                game_progress_obj.evaluating(word_selection_obj.selected_word, player_guess.lower())
                game_progress_obj.updating_progress(word_selection_obj.selected_word) 
        
        refresh_screen(DISPLAYSURF, letters_to_print, game_progress_obj.word_progress, game_progress_obj.players_incorrect_guess)
        frame_per_sec.tick(FPS)

if __name__ == "__main__":
    main()

# if len (incorrect guesses) == 1
# print hangman1 file

# create function that prints out the "hanged man", takes arguments of # of incorrect guesses made