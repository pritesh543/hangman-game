import random
from enum import Enum
from guess import GoodGuess


class GameState(Enum):
    IN_PROGRESS = 0
    WON = 1
    LOST = 2


class GuessResult(Enum):
    CORRECT = 0
    INCORRECT = 1

    FAIL_INVALID_INPUT = 2
    FAIL_ALREADY_GAME_OVER = 3
    FAIL_ALREADY_GUESSED = 4


class HangmanGame:
    def __init__(self, word, failed_guesses_limit):
        if failed_guesses_limit <= 0:
            raise ValueError("failed_guesses_limit must be over 0")

        if len(word) <= 0:
            raise ValueError("word must have at least 1 letter")

        self.word = word

        self.state = GameState.IN_PROGRESS
        self.guesses = []
        self.failed_guess_limit = failed_guesses_limit
        self.num_failed_guesses_remaining = failed_guesses_limit
        self.revealed_word = "".join(["_" for i in range(len(word))])
        self.num_revealed_letters = 0

    def guess(self, input_letter):
        '''
        param:
        ------
            input_letter -> string, the input parameter
        '''
        
        # if input is present in word_to_guess
        # and not guessed already then adding it to guesses list
        # and incrementing - num_revealed_letters
        # if guess is wrong then decrementing - num_failed_guesses_remaining

        if input_letter in self.word and input_letter not in self.guesses:
            self.guesses.append(input_letter)
            self.num_revealed_letters += 1
        else:
            self.num_failed_guesses_remaining -= 1

        # getting updated revealed word

        good_guess = GoodGuess(self.word, self.guesses)
        self.revealed_word = good_guess.get_guessed_word()
        
        # checking if the game is over
        # either won

        if good_guess.is_word_guessed():
            self.state = GameState.WON

        # or failed attempts reached

        if self.num_failed_guesses_remaining == 0:
            self.state = GameState.LOST


class HangmanGameScorer:
    POINTS_PER_LETTER = 20
    POINTS_PER_REMAINING_GUESS = 10

    @classmethod
    def score(cls, game):
        points = game.num_revealed_letters * HangmanGameScorer.POINTS_PER_LETTER
        points += (
            game.num_failed_guesses_remaining
            * HangmanGameScorer.POINTS_PER_REMAINING_GUESS
        )
        return points


def create_hangman_game(words=None, guess_limit=5):
    if words is None:
        words = ["3dhubs", "marvin", "print", "filament"]
        
    if len(words) <= 0:
        raise ValueError("words must have at least 1 word")

    if guess_limit <= 0:
        raise ValueError("guess_limit must be greater than 0")

    rand_word = words[random.randint(0, len(words) - 1)]
    return HangmanGame(rand_word, guess_limit)
