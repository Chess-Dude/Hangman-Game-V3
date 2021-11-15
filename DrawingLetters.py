"""
Function that draws buttons to be pressed
"""

import pygame

def draw_letters(DISPLAYSURF, 
                 letters_to_print, 
                 FIRST_CIRCLE_X, 
                 FIRST_CIRCLE_Y_ROW_1, 
                 FIRST_CIRCLE_Y_ROW_2, 
                 BLACK, 
                 LETTER_FONT, 
                 LETTER_FONT_SIZE, 
                 RADIUS, 
                 LINE_THICKNESS, 
                 TOTAL_WIDTH):
    """
    to find the corrects values I used  the following formula:
    (width of screen - (radius of circcle + gap between circles)(# of alphabets/2)/2)
    This gave me the leftover pixels for each side, 34.5 which rounds up to 35.
    This info allowed me to start drawing from the left side of the first circle.
    Note that to draw the circle, we must give the draw.circle method the coordinate range, thius adding half the gap + half the diameter of the circle. 
    """

    # defining coords to draw buttons
    x_circle_coord = FIRST_CIRCLE_X
    y_circle_coord_row_1 = FIRST_CIRCLE_Y_ROW_1
    y_circle_coord_row_2 = FIRST_CIRCLE_Y_ROW_2

    # looping 13 times (13 buttons per row)
    for i in range(13):

        # checking if dictionary value of letter is True (from A-M) (top row)
        # if false - does not print (already guessed values)
        if letters_to_print[chr(65 + i)]:
            # Drawing buttons for top row buttons
            # draws circle, instantiates the letter then blits it
            pygame.draw.circle(DISPLAYSURF, BLACK, (x_circle_coord, y_circle_coord_row_1), RADIUS, LINE_THICKNESS)
            letters = LETTER_FONT.render(chr(65 + i), 1, BLACK)
            DISPLAYSURF.blit(letters, (x_circle_coord - (LETTER_FONT_SIZE / 4), y_circle_coord_row_1 - (LETTER_FONT_SIZE / 4)))  

        # checking if dictionary value of letter is True (from N-Z) (bottom row)
        # if false - does not print (already guessed values)
        if letters_to_print[chr(78 + i)]: 
            # Drawing letter for bottom row buttons
            # draws circle, instantiates the letter then blits it
            pygame.draw.circle(DISPLAYSURF, BLACK, (x_circle_coord, y_circle_coord_row_2), RADIUS, LINE_THICKNESS)
            letters = LETTER_FONT.render(chr(78 + i), 1, BLACK)
            DISPLAYSURF.blit(letters, (x_circle_coord - (LETTER_FONT_SIZE / 4), y_circle_coord_row_2 - (LETTER_FONT_SIZE / 4)))         
        
        # updates x_circle_coord each loop to get new circle x coord        
        x_circle_coord = x_circle_coord + TOTAL_WIDTH

