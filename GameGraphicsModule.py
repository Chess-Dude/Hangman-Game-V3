"""
"""

import pygame 
from pygame.locals import * 
import sys

class GameGraphics:
    """
    """

    def __init__(self):
        """
        """
        pygame.init()
        # setting up fps
        self.FPS = 30
        self.frame_per_sec = pygame.time.Clock()
        
        # Setting up fonts
        self.TITLE_FONT = pygame.font.SysFont('comicsans', 70)
        self.LETTER_FONT_SIZE = 40
        self.LETTER_FONT = pygame.font.SysFont('comicsans', self.LETTER_FONT_SIZE)        

        # setting up colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (255, 0, 0)
        self.RED = (0, 255, 77)

        # screen dimensions (background image dimensions)
        self.SCREEN_WITDTH = 979
        self._SCREEN_HEIGHT = 472
        self.DISPLAYSURF = pygame.display.set_mode(size=(self.SCREEN_WITDTH, self._SCREEN_HEIGHT))

        # circle dimensions (for buttons)
        self.RADIUS_OF_CIRCLE = 30
        self.GAP = 10
        self.TOTAL_WIDTH = self.RADIUS_OF_CIRCLE * 2 + self.GAP
        self.LINE_THICKNESS = 3

        # circle coords (for buttons)
        self.x_circle_coord = round((self.SCREEN_WITDTH - (self.RADIUS_OF_CIRCLE * 2 + self.GAP) * 13) / 2) + self.RADIUS_OF_CIRCLE + (self.GAP / 2)
        self.y_circle_coord_row_1 = 350
        self.y_circle_coord_row_2 = 420

        # hangman variables
        self.hangman_image_list = []
        self.hangman_status = len(self.hangman_image_list)
        self.players_guess = ""

    def init_background(self):
        """
        """
        # creating screen
        
        pygame.display.set_caption("Hangman")

        # Loading Background Images
        BACKGROUND = pygame.image.load('hangmanbackgroundtest.jpg')
        self.DISPLAYSURF.blit(BACKGROUND, (0, 0))  


    def importing_hangman_images(self):
        """
        """
        
        
        for i in range(7):
            hangman_image = pygame.image.load("hangman" + str(i) + ".png")
            self.hangman_image_list.append(hangman_image)
            self.DISPLAYSURF.blit(self.hangman_image_list[self.hangman_status], (150, 100))
            pygame.display.update()


    def draw_letters(self):
        """
        """
        for i in range(13):

            pygame.draw.circle(self.DISPLAYSURF, self.WHITE, (self.x_circle_coord, self.y_circle_coord_row_1), self.RADIUS_OF_CIRCLE, self.LINE_THICKNESS)
            letters = self.LETTER_FONT.render(chr(65 + i), 1, self.WHITE)
            self.DISPLAYSURF.blit(letters, (self.x_circle_coord - (self.LETTER_FONT_SIZE / 4), self.y_circle_coord_row_1 - (self.LETTER_FONT_SIZE / 4)))  

            pygame.draw.circle(self.DISPLAYSURF, self.WHITE, (self.x_circle_coord, self.y_circle_coord_row_2), self.RADIUS_OF_CIRCLE, self.LINE_THICKNESS)
            letters = self.LETTER_FONT.render(chr(78 + i), 1, self.WHITE)
            self.DISPLAYSURF.blit(letters, (self.x_circle_coord - (self.LETTER_FONT_SIZE / 4), self.y_circle_coord_row_2 - (self.LETTER_FONT_SIZE / 4)))         
            self.x_circle_coord = self.x_circle_coord + self.TOTAL_WIDTH
            
            pygame.display.update()


    def delete_letters(self):
        """
        """
            # image auto 
            # make it so u can click on circle and it will disappear 
            # add the circle/letter to "clicked on" to list
            # stuff in this list will not be printed 
            # be able to detect when a mouse is clicked
            # 350 - RADIUS - GAP 
        
        clicked_on = []

    
    def run_pygame(self):
        """
        """
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
                    x2 = self.SCREEN_WITDTH - 35
                    PADDING = (x2 - x1) / 13 
                    y = 385
                    y1 = 350 - self.RADIUS_OF_CIRCLE - PADDING
                    y2 = 420 - self.RADIUS_OF_CIRCLE + PADDING
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
                            
                
                        self.player_guess = str(chr(COLUMN_NUMBER))
                        print(self.players_guess)

                        return self.players_guess


                    self.frame_per_sec.tick(self.FPS)
