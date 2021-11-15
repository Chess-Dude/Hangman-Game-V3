"""
Blits GAME_IN_PROGRESS text
"""

def blitting_text(DISPLAYSURF, 
                  word_progress, 
                  selected_topic, 
                  system_message, 
                  WORD_FONT, BLACK, 
                  SUB_TITLE_FONT, 
                  WIDTH, 
                  SYSTEM_FONT_MESSAGE, 
                  HELP_FONT_MESSAGE):
    """
    blits/renders text
    """

    word_text = WORD_FONT.render(word_progress, 1, BLACK)
    DISPLAYSURF.blit(word_text, word_text.get_rect(center = DISPLAYSURF.get_rect().center))
    
    topic_text = SUB_TITLE_FONT.render(("Topic: " + selected_topic), 1, BLACK) 
    DISPLAYSURF.blit(topic_text, (WIDTH/2 - topic_text.get_width()/2, 75))

    system_message_text = SYSTEM_FONT_MESSAGE.render(system_message, 1, BLACK)
    DISPLAYSURF.blit(system_message_text, (WIDTH/2 - system_message_text.get_width()/2, 150))

    help_text_button = HELP_FONT_MESSAGE.render("Click Here For Help", 1, BLACK)
    DISPLAYSURF.blit(help_text_button, (WIDTH - 150, 40))
    help_text_width, helpt_text_height = help_text_button.get_size()
