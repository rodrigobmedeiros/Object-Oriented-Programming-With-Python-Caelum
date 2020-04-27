# Exercises - Section 5.5
# Solution of the exercises.
# Developed by: Rodrigo bernardo
# Date: 21/04/2020


def mean_velocity(distance, time):
    # Exercise 1
    velocity = divide_numbers(distance, time)
    return velocity


def sum_numbers(num1, num2):
    # Exercise 6
    return num1 + num2


def subtraction_numbers(num1, num2):
    # Exercise 7
    return num1 - num2


def divide_numbers(num1, num2):
    # Exercise 11
    return num1 / num2


def calculator(num1, num2):
    # Exercise 8
    multiply = num1 * num2
    divide = num1 / num2

    return sum_numbers(num1, num2), subtraction_numbers(num1, num2), multiply, divide


sum_, subtraction_, multiply_, divide_ = calculator(4, 2)

print(sum_)
print(subtraction_)
print(multiply_)
print(divide_)

mean_velocity(distance=100, time=20)
mean_velocity(distance=150, time=22)

