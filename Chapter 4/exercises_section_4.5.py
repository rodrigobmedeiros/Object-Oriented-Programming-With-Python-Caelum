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

    grades = list(map(float, input('Enter 4 grades separated with spaces: ').split()))

    print(grades)

    mean = sum(grades)/len(grades)

    print('The mean between grades is {}'.format(round(mean, 2)))

def exercise_4():

    user_info = {}

    user_info['name'], user_info['age'], user_info['city'] = input('Enter your name, city and age separated with'
                                                                   'spaces: ').split()

    for key, value in user_info.items():

        print('{}: {}'.format(key,value))

def

exercise_4()


