"""This module will provide the updated revealed word
    and also if the game is WON
"""

class GoodGuess:
    def __init__(self, word_to_guess, letters_guessed):
        '''
        initializing the word and gussed letters
        for use in throught the class

        '''
        self.word_to_guess = word_to_guess
        self.letters_guessed = letters_guessed

    def get_guessed_word(self):
        '''
        param:
        ------
            word_to_guess ->  string, the word the user is guessing
            lettersGuessed -> list, what letters have been guessed so far

        return:
        -------   
            string, comprised of letters and underscores that represents
                    what letters in word_to_guess have been guessed so far.
        '''

        # taking all the letters matched in variable
        
        letters_matched = []
        for char in self.word_to_guess:
            if char in self.letters_guessed:
                letters_matched.append(char)
        
        # preparing reveal word with good guesses
        # the correct letters are added in their
        # respective position in the reveal_word

        new_reveled_word = ''
        for char in self.word_to_guess:
            if char in letters_matched:
                new_reveled_word += char
            else:
                new_reveled_word += '_ '
        
        return new_reveled_word

    def get_match_count(self, input_letter):
        '''

        param:
        ------
            word_to_guess -> string, the word the user is guessing
            letters_guessed -> list, what letters have been guessed so far

        return:
        -------
            int, len of the total match from the word_to_guess

        '''

        # iterating over word to find total count of letter in a word
        return len([i for i, letter in enumerate(self.word_to_guess) if letter == input_letter])

    def is_word_guessed(self):
        '''

        param: 
        ------
            word_to_guess -> string, the word the user is guessing
            letters_guessed -> list, what letters have been guessed so far
        
        return:
        ------- 
            boolean, True if all the letters of word_to_guess are in letters_guessed; False otherwise

        '''

        # summing up the correct guesses

        char_match_count = 0
        for letter in self.letters_guessed:
            char_match_count += self.get_match_count(letter)
        
        # if the word is revealed then 
        # user is WON

        if char_match_count == len(self.word_to_guess):
            return True
        else:
            return False