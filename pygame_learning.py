import os # help with getting/formatting file path locations
import sys # helps with systems level commands (exiting programs, gettings command line info)
import time 
import pygame 
from pygame.locals import * 


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

    # setting up color objects
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Setup a 300x300 pixel display with caption

    DISPLAYSURF = pygame.display.set_mode(size=(300, 300))
    DISPLAYSURF.fill(WHITE)
    
    while True:
        # Run game

        # Update game display so the user can see
        pygame.display.update()

        print(pygame.event)
        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit event occured")
                pygame.quit()
                sys.exit()
       
        frame_per_sec.tick(FPS)

if __name__ == "__main__":
    main()