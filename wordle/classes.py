import enum
from time import sleep
import wordle.words

class Letter(enum.Enum):
    unknown = 0
    known = 1
    correct = 2

class Guess(object):

    def __init__(self, word: str, correct: str) -> None:

        self.letters = []

        if len(word) != 5 and len(correct) != 5:
            raise ValueError('Word and letters must be 5 letters long')

        for i in range(len(word)):
            if word[i] == correct[i]:
                self.letters.append(Letter.correct)
            elif word[i] in correct:
                self.letters.append(Letter.known)
            else:
                self.letters.append(Letter.unknown)

        self.word = word

        print(self.letters, self.word)

    def next_possible_words(self) -> list[str]:

        words = wordle.words.load_words()

        contained_letters = [] # list of letters that are in the word
        letter_data = {} # {letter[str]: index[int]}

        buffer_list = list(zip(list(self.word), self.letters)) # [(letter[str], letter_status[Letter])]
        for i, pair in enumerate(buffer_list):
            if pair[1] == Letter.correct:
                letter_data[pair[0]] = i
                contained_letters.append(pair[0])
            elif pair[1] == Letter.correct:
                letter_data[pair[0]] = -1
                contained_letters.append(pair[0])
        print('letter_data:', letter_data)
        input('...')

        possible_words = words

        for word in possible_words:
            for letter in contained_letters:
                if letter not in word:
                    possible_words.remove(word)
                    break
                    

        while len(contained_letters) > 0:
            for word in possible_words:
                if word[letter_data[contained_letters[0]]] != contained_letters[0]:
                    print('removing', word)
                    possible_words.remove(word)
            contained_letters.pop(0)


        return possible_words