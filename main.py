from wordle.classes import Guess
from wordle.words import load_words
from wordle.game import generate_guess_results

correct = 'word'
guess_word = 'worm'

words = load_words()

print(correct in words)
print(guess_word in words)

guess = Guess(guess_word, generate_guess_results(guess_word, correct))
next_words = guess.next_possible_words()

print(next_words)