# Hangman Game - v2.0
# Game to find a secret word by guessing each letter
# Developed by: Rodrigo bernardo
# Date: 21/04/2020

# Updating v2.0
# The word is read from a text file.

import random as rd


def main():

    print('**************************************')
    print('*           Hangman Game             *')
    print('**************************************')

    # Word to find
    secret_word = 'banana'
    word_file = open('words.txt', 'r')
    lines = word_file.readlines()

    secret_word = lines[rd.randint(0, len(lines) - 1)].rstrip('\n')

    empty_word = list(map(lambda x: x.replace(x, "_"), secret_word))

    # Define variables to control if the game continue or not.
    find_word = False
    hanged = False
    count_errors = 0
    max_errors = 6

    print(empty_word)

    # Loop to ask user for a letter
    while (not find_word) and (not hanged):

        letter = input('Guess a letter\n '
                       '>> ').lower()

        if letter in secret_word:

            index = 0
            print('Nice! We found {} in the secret word'.format(letter))

            # Replace _ for the letter at right position
            for char in secret_word:

                if letter == char:

                    empty_word[index] = char

                index += 1
            # Print the status of the word
            print(empty_word)

        else:

            count_errors += 1
            print('There is no {} in the secret word'.format(letter))
            print('You have: {} chances'.format(max_errors - count_errors))

        if not ('_' in empty_word):
            # Finish the game with win.
            find_word = True
            print('You win!')

        if count_errors == max_errors:
            # Finish the game with lose.
            hanged = True
            print('You lose!')

    print('End Game')


if __name__ == '__main__':

    main()

