"""
The topic and then the word for the Hangman game will be auto selected here.
"""

# importing modules used
import random
import json

# Instantiating class
class WordSelection:
    """
    Select the topic then the word
    """

    def __init__(self):
        """
        Constructor Function that chooses topic and word.
        """
        # reading TopicDictionary.json's dictionary
        with open("TopicDictionary.json", 'r') as config_reader:
            # imports dictionary of topics and words into self.topic_dictionary
            self.topic_dictionary = json.loads(config_reader.read())
        
        self.topic_list = list(self.topic_dictionary.keys())
        
        # randomizes topic then word
        self.selected_topic = random.choice(self.topic_list)                   
        self.selected_word = random.choice(self.topic_dictionary[self.selected_topic])


    def __str__(self):
        """
        Made for Debugging purposes
        """    
        status_1 = "selected_topic is " + self.selected_topic + "\n"
        status_2 = "selected_word is " + self.selected_word + "\n"    
        return status_1 + status_2
        
        
