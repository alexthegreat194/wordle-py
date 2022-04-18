import json

def load_words() -> list[str]:
    '''load_words loads the words from the words.json file

    Returns:
        list[str]: list of words from the words.json file
    '''

    with open('wordle/words.json', 'r') as file:
        data = json.load(file)
        return data['words']