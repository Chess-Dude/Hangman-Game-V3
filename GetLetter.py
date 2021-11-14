"""
Gets what letter was pressed (user input)
"""

def get_letter(m_x, 
               m_y, 
               letters_to_print, 
               GRID_LEFT_X1, 
               COLUMN_WIDTH, 
               GRID_RIGHT_X2, 
               GRID_Y1, 
               GRID_Y2, 
               GRID_MID_Y, 
               ASCII_A):
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