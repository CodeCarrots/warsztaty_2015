from .colorama import init
from .termcolor import colored
init()


def check(func, data):
    for input_value, expected_value in data:

        # Run function that was passed as argument
        value = func(input_value)

        result, modifier, color = 'OK',  '', 'green'

        # Compare value produced by function and expected value
        if value != expected_value:
            result, modifier, color = 'ERROR', 'NOT', 'red'

        print(colored("{0}: `func({1})` -> `{2}`".format(result, input_value, value), color))

        if result == 'ERROR':
            print("`{0}` is {1} equal to `{2}`".format(value, modifier, expected_value))