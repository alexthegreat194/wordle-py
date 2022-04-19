from wordle.classes import Guess, Letter

def generate_guess_results(word: str, correct: str) -> list[Letter]:
    '''generate_guess_results Generates a list of Letter objects based on the guess.

    Args:
        word (_type_): The word to guess.
        correct (_type_): The correct word.

    Returns:
        list[Letter]: A list of Letter objects.
    '''
    # make sure that the word and correct are 5 characters long
    if len(word) != 5 or len(correct) != 5:
        raise ValueError('Word and correct must be 5 characters long.')

    guesses = []
    for i in range(len(word)):
        if word[i] == correct[i]:
            guesses.append(Letter.correct)
        elif word[i] in correct:
            guesses.append(Letter.known)
        else:
            guesses.append(Letter.unknown)
    return guesses