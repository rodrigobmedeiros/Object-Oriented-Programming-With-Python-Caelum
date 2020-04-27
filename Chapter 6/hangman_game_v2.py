# Hangman Game - v2.0
# Game to find a secret word by guessing each letter
# Developed by: Rodrigo bernardo
# Date: 21/04/2020

# Updating v2.0
# The word is read from a text file.

import random as rd


def print_start_game():

    print('**************************************')
    print('*           Hangman Game             *')
    print('**************************************')


def define_secret_word():

    word_file = open('words.txt', 'r')
    lines = word_file.readlines()
    word_file.close()

    secret_word = lines[rd.randint(0, len(lines) - 1)].rstrip('\n')

    return secret_word


def print_win_message():

    print('You win!')


def print_loser_message():

    print('You lose!')


def print_hangman(errors):

    if errors == 1:

        print("---------------------")
        print("|            |       ")
        print("|           ---      ")
        print("|          |   |     ")
        print("|           ---      ")
        print("|                    ")
        print("|                    ")
        print("|                    ")
        print("|                    ")
        print("|                    ")
        print("|                    ")
        print("-----                ")
        print("     |               ")
        print("     ----------------")

    elif errors == 2:

        print("---------------------")
        print("|            |       ")
        print("|           ---      ")
        print("|          |   |     ")
        print("|           ---      ")
        print("|            |       ")
        print("|            |       ")
        print("|            |       ")
        print("|            |       ")
        print("|                    ")
        print("|                    ")
        print("-----                ")
        print("     |               ")
        print("     ----------------")

    elif errors == 3:

        print("---------------------")
        print("|            |       ")
        print("|           ---      ")
        print("|          |   |     ")
        print("|           ---      ")
        print("|            | /     ")
        print("|            |/      ")
        print("|            |       ")
        print("|            |       ")
        print("|                    ")
        print("|                    ")
        print("-----                ")
        print("     |               ")
        print("     ----------------")

    elif errors == 4:

        print("---------------------")
        print("|            |       ")
        print("|           ---      ")
        print("|          |   |     ")
        print("|           ---      ")
        print("|          \ | /     ")
        print("|           \|/      ")
        print("|            |       ")
        print("|            |       ")
        print("|                    ")
        print("|                    ")
        print("-----                ")
        print("     |               ")
        print("     ----------------")

    elif errors == 5:

        print("---------------------")
        print("|            |       ")
        print("|           ---      ")
        print("|          |   |     ")
        print("|           ---      ")
        print("|          \ | /     ")
        print("|           \|/      ")
        print("|            |       ")
        print("|            |       ")
        print("|           /        ")
        print("|          /         ")
        print("-----                ")
        print("     |               ")
        print("     ----------------")

    elif errors == 6:

        print("---------------------")
        print("|            |       ")
        print("|           ---      ")
        print("|          |   |     ")
        print("|           ---      ")
        print("|          \ | /     ")
        print("|           \|/      ")
        print("|            |       ")
        print("|            |       ")
        print("|           / \      ")
        print("|          /   \     ")
        print("-----                ")
        print("     |               ")
        print("     ----------------")


def update_word_with_guess(letter, secret_word, empty_word):

    index = 0
    print('Nice! We found {} in the secret word'.format(letter))

    # Replace _ for the letter at right position
    for char in secret_word:

        if letter == char:
            empty_word[index] = char

        index += 1
    # Print the status of the word
    print(empty_word)


def main():

    print_start_game()

    secret_word = define_secret_word()

    empty_word = list(map(lambda x: x.replace(x, "_"), secret_word))

    # Define variables to control if the game continue or not.
    find_word = False
    hanged = False
    count_errors = 0
    max_errors = 6

    print('Word to find: ')
    print(empty_word)

    # Loop to ask user for a letter
    while (not find_word) and (not hanged):

        letter = input('Guess a letter\n '
                       '>> ').lower()

        if letter in secret_word:

            update_word_with_guess(letter, secret_word, empty_word)

        else:

            count_errors += 1
            print('There is no {} in the secret word'.format(letter))
            print('You have: {} chances'.format(max_errors - count_errors))
            print_hangman(count_errors)

        find_word = '_' not in empty_word
        hanged = count_errors == max_errors

        if find_word:
            # Finish the game with win.
            print_win_message()

        if hanged:
            # Finish the game with lose.
            print_loser_message()

    print('End Game')


if __name__ == '__main__':

    main()

