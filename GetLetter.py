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
    Determines what button is pressed and returns a letter value
    """
    # variables that are used to determine what cell was pressed on the grid
    player_guess = None
    column_number = (((m_x - GRID_LEFT_X1) / COLUMN_WIDTH) + 1) 
    column_number = int(column_number)
    top_row = False

    # determining if mouse button is in grid (if a button is pressed) via mouse pressed coordinates
    if ((GRID_LEFT_X1 <= m_x < GRID_RIGHT_X2) and (GRID_Y1 <= m_y <= GRID_Y2)):

        # determining what row the mouse was clicked
        # if mouse y coordinate was greater than the MID_Y (height) coordinate, set top_row variable false (used as a flag). 
        # we do this to identify if we should add +13 to the ascii table 
        if m_y > GRID_MID_Y:
            top_row = False 

        # elif mouse y coordinate < MID_Y (height) coordinate, set top_row variable True (used as a flag)
        elif m_y < GRID_MID_Y:
            top_row = True

        # if mouse was clicked in top row (flag)
        if top_row:
            player_guess = str(chr(column_number + ASCII_A - 1)) # subtract 1 due to column number starting from 1, not 0 

        # else (if mouse was clicked in bottom row) we add + 13 to the ascii table value (as first 13 letters are A - M)
        else:
            player_guess = str(chr(column_number + ASCII_A + 13 - 1))

    # returns player_guess only if player guess has a value and the letter has a "True" value
    # we want to make sure it has a "True" value to make sure the grid cell was not already pressed/guessed by the user 
    if (player_guess is not None) and (letters_to_print[player_guess]):
        return player_guess
        
    else:
        return None