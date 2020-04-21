# Guessing Game
# Game to find a secret number asking the user for a guess
# Developed by: Rodrigo bernardo
# Date: 21/04/2020

def main():

    print('**************************************')
    print('*            Guessing Game           *')
    print('**************************************')

    # Define a secret number
    secret_number = 42

    # Ask user for a integer number and convert from string to int
    print('\n')

    # Define the number of tries and a round to start
    number_of_tries = 3
    n_round = 1

    while n_round <= number_of_tries:

        print('round {} of {}'.format(n_round, number_of_tries))

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


if __name__ == '__main__':

    main()


