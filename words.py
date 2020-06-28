import json

class Words:

    __WORD_PATH = 'english-words/words_dictionary.json'

    @classmethod
    def load_dictionary(cls):
        with open(Words.__WORD_PATH, 'r') as file:
            dictionary = json.load(file)

        return dictionary
