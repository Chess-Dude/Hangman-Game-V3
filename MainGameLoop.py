"""
Calling all classes/methods to create objects and run the Hangman game
"""


import WordSelectionModule
import GameProgressModule
import GameGraphicsModule

def main():
    """
    Creating instance variables
    """

    word_selection_obj = WordSelectionModule.WordSelection()
    game_progress_obj = GameProgressModule.GameProgress()
    game_graphics_obj = GameGraphicsModule.GameGraphics()
    
    game_progress_obj.updating_progress(word_selection_obj.selected_word) 

    print("The Selected Topic is ", word_selection_obj.selected_topic)
    print(word_selection_obj)
    print(game_progress_obj.word_progress)
    
    while True:
        game_graphics_obj.init_background()
        game_graphics_obj.importing_hangman_images()
        game_graphics_obj.draw_letters()
        game_graphics_obj.run_pygame()
        game_progress_obj.get_players_guess(game_graphics_obj.players_guess)
        game_progress_obj.evaluating(word_selection_obj.selected_word) # This method should end the game depending on player guesses
        game_progress_obj.updating_progress(word_selection_obj.selected_word)
        game_progress_obj.print_progress() 


if __name__ == "__main__":
    main()