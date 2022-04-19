from wordle.classes import Guess
from wordle.words import load_words

correct = 'words'
guess_word = 'worms'

words = load_words()

print(correct in words)
print(guess_word in words)

guess = Guess(guess_word, correct)
next_words = guess.next_possible_words()

print(next_words)