import json
from pprint import pprint

def load_words() -> list[str]:
    '''load_words loads the words from the words.json file

    Returns:
        list[str]: list of words from the words.json file
    '''

    with open('wordle/words.json', 'r') as file:
        data = json.load(file)
        return data['words']


def scrape_words():
    data = {}
    with open('wordle/words.json', 'r') as file:
        data = json.load(file)

    # get all the words from usr/share/dict/words
    found_words = []
    with open('/usr/share/dict/words', 'r') as file:
        for line in file:
            found_words.append(line.strip())
    
    # remove all non 4 letter words from words
    words = []
    for word in words:
        if len(word) == 4:
            words.append(word)

    # add 's' to all words in words
    for word in words:
        words.append(word + 's')

    # add words to data
    data['words'].extend(words)

    print(data)

    # write data to words.json
    with open('wordle/words.json', 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    scrape_words()