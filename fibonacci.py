"""
Calculates Fibonacci sequence
"""

from fib import fib


def main():
    """
    Program main entry point
    :return: None
    """
    integer_input = 4
    string_input = "5"
    float_input = 6.5

    fibonacci_sequence = list(fib(integer_input))
    print(fibonacci_sequence)

    fibonacci_sequence = list(fib(string_input))  # error
    print(fibonacci_sequence)

    fibonacci_sequence = list(fib(float_input))  # error
    print(fibonacci_sequence)

    fibonacci_sequence = list(fib(integer_input, float_input))  # error
    print(fibonacci_sequence)


main()
