# Exercises - Section 4.5
# Solution of the exercises.
# Developed by: Rodrigo bernardo
# Date: 21/04/2020


def exercise_1():

    numbers = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
    sorted_numbers = sorted(numbers)
    # Print the highest element

    print('highest number: {}'.format(sorted_numbers[-1]))

    # Print the lowest element
    print('lowest number: {}'.format(sorted_numbers[0]))

    # Print even numbers
    print('Even numbers:')
    for num in sorted_numbers:

        if num % 2 == 0:

            print(num, sep=' ')

    # Print the frequence of the first element
    print('The number {} appears {} times'.format(numbers[0], numbers.count(numbers[0])))

    # Print the mean of the elements
    mean = sum(numbers)/len(numbers)
    print('The mean between numbers is {}'.format(round(mean, 2)))

    # Print the negative numbers
    sum_negatives = sum(sorted_numbers[:3])
    print('The sum of negative numbers is {}'.format(sum_negatives))


def exercise_2():

    user_info = input('name surname age separated with spaces: ').split()

    for item in user_info:

        print(item)

def exercise_3():

    



exercise_2()


