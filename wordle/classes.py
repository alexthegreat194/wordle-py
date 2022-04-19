import enum
from pprint import pprint
from time import sleep

from sqlalchemy import false
import wordle.words

class Letter(enum.Enum):
    unknown = 0
    known = 1
    correct = 2

class Guess(object):

    def __init__(self, word: str, correct: str) -> None:

        self.letters = []

        if len(word) != 5 or len(correct) != 5:
            raise ValueError('Word and letters must be 5 letters long')

        for i in range(len(word)):
            if word[i] == correct[i]:
                self.letters.append(Letter.correct)
            elif word[i] in correct:
                self.letters.append(Letter.known)
            else:
                self.letters.append(Letter.unknown)

        self.word = word

        # print(self.letters, self.word)

    def next_possible_words(self) -> list[str]:

        words = wordle.words.load_words()

        contained_letters = [] # list of letters that are in the word
        letter_data = {} # {letter[str]: index[int]}

        # create contained_letters and letter_data
        buffer_list = list(zip(list(self.word), self.letters)) # [(letter[str], letter_status[Letter])]
        for i, pair in enumerate(buffer_list):
            if pair[1] == Letter.correct:
                letter_data[pair[0]] = i
                contained_letters.append(pair[0])
            elif pair[1] == Letter.correct:
                letter_data[pair[0]] = -1
                contained_letters.append(pair[0])

        # print('letter_data:', letter_data)
        # input('...')

        possible_words = []
        # add possible words to possible_words
        for word in words:
            # check to see if the word contains all the letters in contained_letters
            in_word = True
            for letter in contained_letters:
                if letter not in word:
                    in_word = False
                    break
            if in_word:
                possible_words.append(word)

        # pprint(possible_words)

        # remove words that have the wrong letters
        correct_words = []
        for word in possible_words:
            is_possible = True

            for letter in contained_letters:
                letter_index = letter_data[letter]
                
                if letter_index != -1:
                    if word[letter_index] != letter:
                        is_possible = False
                        # print('letter', letter, 'is not at index', letter_index, 'in word', word)
                        break
                else:
                    if letter not in word:
                        is_possible = False
                        break

            if is_possible == True:
                # print('adding', word)
                correct_words.append(word)

        

    
        # pprint(correct_words)

        return possible_words