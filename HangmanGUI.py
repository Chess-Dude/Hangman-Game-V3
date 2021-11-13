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

# initializes pygame
pygame.init()

# display size
WIDTH = 979
HEIGHT = 472
# BACKGROUND = pygame.image.load('hangmanbackgroundtest.jpg')

# FPS
FPS = 30

# Declaring font types
TITLE_FONT = pygame.font.SysFont('comicsans', 80)
SUB_TITLE_FONT = pygame.font.SysFont('comicsans', 60)
WORD_FONT = pygame.font.SysFont('comicsans', 55)
LETTER_FONT_SIZE = 40
LETTER_FONT = pygame.font.SysFont('comicsans', LETTER_FONT_SIZE)
SYSTEM_FONT_MESSAGE = pygame.font.SysFont('comicsans', 30)

# setting up color objects
WHITE = (0, 180, 0)
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
    Importing and blitting hangman images
    """
    
    hangman_image_list = []
    hangman_status = len(players_incorrect_guess)
    for i in range(7):
        hangman_image = pygame.image.load("hangman" + str(i) + ".png")
        hangman_image_list.append(hangman_image) 
        print(hangman_status) # do not forget to remove
        DISPLAYSURF.blit(hangman_image_list[hangman_status], (130, 100))
        

def draw_letters(DISPLAYSURF, letters_to_print):
    """
    to find the corrects values I used  the following formula:
    (width of screen - (radius of circcle + gap between circles)(# of alphabets/2)/2)
    This gave me the leftover pixels for each side, 34.5 which rounds up to 35.
    This info allowed me to start drawing from the left side of the first circle.
    Note that to draw the circle, we must give the draw.circle method the coordinate range, thius adding half the gap + half the diameter of the circle. 
    refer to the official documentation of the code below:    
    """

    # defining coords to draw buttons
    x_circle_coord = FIRST_CIRCLE_X
    y_circle_coord_row_1 = FIRST_CIRCLE_Y_ROW_1
    y_circle_coord_row_2 = FIRST_CIRCLE_Y_ROW_2

    # looping 13 times (13 buttons per row)
    for i in range(13):

        # checking if dictionary value of letter is True (from A-M)
        # if false - does not print (already guessed values)
        if letters_to_print[chr(65 + i)]:
            # Drawing buttons for top row buttons
            pygame.draw.circle(DISPLAYSURF, WHITE, (x_circle_coord, y_circle_coord_row_1), RADIUS, LINE_THICKNESS)
            letters = LETTER_FONT.render(chr(65 + i), 1, WHITE)
            DISPLAYSURF.blit(letters, (x_circle_coord - (LETTER_FONT_SIZE / 4), y_circle_coord_row_1 - (LETTER_FONT_SIZE / 4)))  

        # checking if dictionary value of letter is True (from N-Z)
        # if false - does not print (already guessed values)
        if letters_to_print[chr(78 + i)]: 
            # Drawing letter for bottom row buttons
            pygame.draw.circle(DISPLAYSURF, WHITE, (x_circle_coord, y_circle_coord_row_2), RADIUS, LINE_THICKNESS)
            letters = LETTER_FONT.render(chr(78 + i), 1, WHITE)
            DISPLAYSURF.blit(letters, (x_circle_coord - (LETTER_FONT_SIZE / 4), y_circle_coord_row_2 - (LETTER_FONT_SIZE / 4)))         
        
        x_circle_coord = x_circle_coord + TOTAL_WIDTH


def get_letter(m_x, m_y, letters_to_print):
    """
    Determines what button is pressed
    """

    player_guess = None
    column_number = (((m_x - X1) / COLUMN_WIDTH) + 1) 
    column_number = int(column_number)
    top_row = False

    # determining if mouse button is in grid (if a button is pressed) via mouse pressed coordinates
    if ((X1 <= m_x < X2) and (Y1 <= m_y <= Y2)):

        # determining what row the mouse was clicked
        # if mouse y coordinate was greater than the 
        if m_y > Y_MID:
            print("mouse pos > 385, bottom row")
            top_row = False 

        elif m_y < Y_MID:
            print("mouse pos < 385, top row")
            top_row = True

        # if mouse was clicked in top row
        if top_row:
            player_guess = str(chr(column_number + ASCII_A - 1)) # subtract 1 due to column number starting from 1, not 0 

        # else (if mouse was clicked in bottom row)
        else:
            player_guess = str(chr(column_number + ASCII_A + 13 - 1))


    if (player_guess is not None) and (letters_to_print[player_guess]):
        print(player_guess)
        return player_guess
        

    else:
        return None


def refresh_screen(DISPLAYSURF, letters_to_print, word_progress, players_incorrect_guess, selected_topic, system_message):
    """
    refreshes screen
    """
    
    # Loading Background Images
    # DISPLAYSURF.blit(BACKGROUND, (0, 0))
    DISPLAYSURF.fill((0, 130, 0))  

    # Printing Text
    title_text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    DISPLAYSURF.blit(title_text, (WIDTH/2 - title_text.get_width()/2, 20))
    
    word_text = WORD_FONT.render(word_progress, 1, BLACK)
    DISPLAYSURF.blit(word_text, word_text.get_rect(center = DISPLAYSURF.get_rect().center))
    
    topic_text = SUB_TITLE_FONT.render(("Topic: " + selected_topic), 1, BLACK) 
    DISPLAYSURF.blit(topic_text, (WIDTH/2 - topic_text.get_width()/2, 75))

    system_message_text = SYSTEM_FONT_MESSAGE.render(system_message, 1, BLACK)
    DISPLAYSURF.blit(system_message_text, (WIDTH/2 - topic_text.get_width()/2, 100))

    # callling functions to load hangman images and draw letters/buttons
    load_hangman_images(DISPLAYSURF, players_incorrect_guess)
    draw_letters(DISPLAYSURF, letters_to_print)


def main():
    """
    Main game loop
    """

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
    # set the screen size according to the background image proportions.
    DISPLAYSURF = pygame.display.set_mode(size=(WIDTH, HEIGHT))
    pygame.display.set_caption("Hangman")
    
    # append all letters of alphabet to letters_to_print dictionary (used in drawing_letters)
    letters_to_print = {}
    for letter in range(0, 26):
        letters_to_print[chr(65 + letter)] = True

    # refreshing screen
    refresh_screen(DISPLAYSURF, letters_to_print, game_progress_obj.word_progress, game_progress_obj.players_incorrect_guess, word_selection_obj.selected_topic, game_progress_obj.system_message)
    pygame.display.update()
    
    # running game
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

            # checking if mouse was clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # getting where mouse was clicked (coords)
                m_x, m_y = pygame.mouse.get_pos()
                
                # getting player guess
                player_guess = get_letter(m_x, m_y, letters_to_print)
                # settings the letter value that was guessed to "false" (to not print)
                letters_to_print[player_guess] = False

            # calling methods from GameProgress class to evaluate and update the progress/score            
            if player_guess is not None:
                game_progress_obj.evaluating(word_selection_obj.selected_word, player_guess.lower())
                game_progress_obj.updating_progress(word_selection_obj.selected_word) 
        
        refresh_screen(DISPLAYSURF, letters_to_print, game_progress_obj.word_progress, game_progress_obj.players_incorrect_guess, word_selection_obj.selected_topic, game_progress_obj.system_message)
        frame_per_sec.tick(FPS)

if __name__ == "__main__":
    main()
