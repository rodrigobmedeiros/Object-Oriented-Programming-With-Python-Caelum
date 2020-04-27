# Exercises - Section 5.8
# Solution of the exercises.
# Developed by: Rodrigo bernardo
# Date: 21/04/2020


def test_args_kwargs_1(arg1, arg2, arg3):
    # Exercise 1 - Test the use of args and kwargs

    print('arg1: ', arg1)
    print('arg2: ', arg2)
    print('arg3: ', arg3)


def test_args_kwargs_2(*args):

    # Exercise 2
    print('arg1: ', args[0])
    print('arg2: ', args[1])
    print('arg3: ', args[2])


def test_args_kwargs_3(**kwargs):

    # Exercise 3
    print('arg1: ', kwargs['arg1'])
    print('arg2: ', kwargs['arg2'])
    print('arg3: ', kwargs['arg3'])


test_args_kwargs_3(arg3=1, arg2=2, arg1=3, arg4=4)

