"""
The topic and then the word for the Hangman game will be auto selected here.
"""

import random
import json


class WordSelection:
    """
    Select the topic then the word
    """

    def __init__(self):
        """
        Constructor Function
        """
        
        with open("TopicDictionary.json", 'r') as config_reader:

            self.topic_dictionary = json.loads(config_reader.read())
        
        self.topic_list = list(self.topic_dictionary.keys())
        self.selected_topic = random.choice(self.topic_list)                   
        self.selected_word = random.choice(self.topic_dictionary[self.selected_topic])


    def __str__(self):
        """
        Made for Debugging purposes
        """    
        status_1 = "selected_topic is " + self.selected_topic + "\n"
        status_2 = "selected_word is " + self.selected_word + "\n"    
        return status_1 + status_2
        
        
