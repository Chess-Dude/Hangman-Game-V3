import os # help with getting/formatting file path locations
import sys # helps with systems level commands (exiting programs, gettings command line info)
import time 
import pygame 
from pygame.locals import * 
import math


def main():
    """
    Main game loop
    Do not run outside this module, as it initializes the pygame here.
    """

    # Initialize the pygame
    pygame.init()

    # Assign FPS a value
    FPS = 30
    frame_per_sec = pygame.time.Clock()

    # Declaring font types
    TITLE_FONT = pygame.font.SysFont('comicsans', 70)
    LETTER_FONT_SIZE = 40
    LETTER_FONT = pygame.font.SysFont('comicsans', LETTER_FONT_SIZE)
    

    # setting up color objects
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (255, 0, 0)
    RED = (0, 255, 77)
    
    # Setup a 979x472 pixel display with caption
    # set the screen size according to the background image proportions.
    WITDTH = 979
    HEIGHT = 472
    DISPLAYSURF = pygame.display.set_mode(size=(WITDTH, HEIGHT))
    pygame.display.set_caption("Hangman")
    DISPLAYSURF.fill(WHITE)

    # Loading Background Images
    background = pygame.image.load('hangmanbackgroundtest.jpg')
    DISPLAYSURF.blit(background, (0, 0))  

    # loading hangman images
    hangman_image_list = []
    hangman_status = 0
    for i in range(7):
        hangman_image = pygame.image.load("hangman" + str(i) + ".png")
        hangman_image_list.append(hangman_image)
        DISPLAYSURF.blit(hangman_image_list[hangman_status], (150, 100))
        pygame.display.update()
  

    # Drawing circles
    RADIUS = 30
    GAP = 10
    TOTAL_WIDTH = RADIUS * 2 + GAP
    LINE_THICKNESS = 3

    # to find the corrects values I used  the following formula:
    # (width of screen - (radius of circcle + gap between circles)(# of alphabets/2)/2)
    # This gave me the leftover pixels for each side, 34.5 which rounds up to 35.
    # This info allowed me to start drawing from the left side of the first circle.
    # Note that to draw the circle, we must give the draw.circle method the coordinate range, thius adding half the gap + half the diameter of the circle. 
    # refer to the official documentation of the code below:    
    x_circle_coord = round((WITDTH - (RADIUS * 2 + GAP) * 13) / 2) + RADIUS + (GAP / 2)
    y_circle_coord_row_1 = 350
    y_circle_coord_row_2 = 420
    for i in range(13):

        pygame.draw.circle(DISPLAYSURF, WHITE, (x_circle_coord, y_circle_coord_row_1), RADIUS, LINE_THICKNESS)
        letters = LETTER_FONT.render(chr(65 + i), 1, WHITE)
        DISPLAYSURF.blit(letters, (x_circle_coord - (LETTER_FONT_SIZE / 4), y_circle_coord_row_1 - (LETTER_FONT_SIZE / 4)))  

        pygame.draw.circle(DISPLAYSURF, WHITE, (x_circle_coord, y_circle_coord_row_2), RADIUS, LINE_THICKNESS)
        letters = LETTER_FONT.render(chr(78 + i), 1, WHITE)
        DISPLAYSURF.blit(letters, (x_circle_coord - (LETTER_FONT_SIZE / 4), y_circle_coord_row_2 - (LETTER_FONT_SIZE / 4)))         
        x_circle_coord = x_circle_coord + TOTAL_WIDTH
        # image auto 
        # make it so u can click on circle and it will disappear 
        # add the circle/letter to "clicked on" to list
        # stuff in this list will not be printed 
        # be able to detect when a mouse is clicked
        # 350 - RADIUS - GAP 

        # time.sleep(1)
        pygame.display.update()

    # Printing font
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    DISPLAYSURF.blit(text, (WITDTH/2 - text.get_width()/2, 20))
    

    

    while True:
        # Run game

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
                x1 = 35
                x2 = WITDTH - 35
                PADDING = (x2 - x1) / 13 
                y = 385
                y1 = 350 - RADIUS - PADDING
                y2 = 420 - RADIUS + PADDING
                ASCII_LETTER_VALUE = 65
                
                COLUMN_NUMBER = (m_x - x1) / PADDING 
                COLUMN_NUMBER = int(COLUMN_NUMBER + ASCII_LETTER_VALUE)

                if ((x1 <= m_x < x2) and (y1 <= m_y <= y2)):
                    print("in grid")

                    if m_y > y:
                        print("mouse pos > 385, bottom row")
                        COLUMN_NUMBER = int(COLUMN_NUMBER + 13)

                    elif m_x < y:
                        print("mouse pos < 385, top row")
                        
            
                    player_guess = str(chr(COLUMN_NUMBER))
                    print(player_guess)

                    return player_guess


                frame_per_sec.tick(FPS)

if __name__ == "__main__":
    main()