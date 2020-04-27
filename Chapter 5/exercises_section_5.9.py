# Exercises - Section 5.9
# Solution of the exercises.
# Developed by: Rodrigo bernardo
# Date: 21/04/2020


def hangman_game():

    print('**************************************')
    print('*           Hangman Game             *')
    print('**************************************')

    # Word to find
    secret_word = 'banana'
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


def guessing_game():

    print('**************************************')
    print('*            Guessing Game           *')
    print('**************************************')

    # Define a secret number
    secret_number = 42

    # Ask user in which difficulty level he wants to play
    level = int(input('Choose the difficulty level: 1 (easy) 2 (Intermediate) 3 (hard)\n'
                      '>> '))

    # Dictionary to define the level string and the number of tries of each level
    levels = {1: ['easy', 10], 2: ['intermediate', 3], 3: ['hard', 1]}
    islevel = level in levels.keys()

    while not islevel:
        level = int(input('Choose the difficulty level: 1 (easy) 2 (Intermediate) 3 (hard)\n'
                          '>> '))
        islevel = level in levels

    print('Level: {}'.format(levels[level][0]))

    # Define the number of tries and a round to start
    number_of_tries = levels[level][1]
    n_round = 1

    while n_round <= number_of_tries:

        print('round {} of {}'.format(n_round, number_of_tries))
        # Ask user for a integer number and convert from string to int
        guess = int(input('Enter a integer number: '))

        # Define bool variables to compare user guess with the secret number
        isequal = guess == secret_number
        ishigher = guess > secret_number
        islower = guess < secret_number

        if isequal:

            # If the guess is right the user win and the game is over.
            print('You win!')
            break

        elif ishigher:

            print('Your guess is higher than secret number')

        elif islower:

            print('Your guess is lower than secret number')

        n_round += 1

    print('End game')