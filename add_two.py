"""
Simple module
"""

def add_two(num):
    """
    Add two to the argument.

    :param num: first addendum
    :return: num + 2
    """
    return num + 2


def main():
    """
    Main program entry point
    """

    this_is_an_integer = add_two(3)
    this_is_a_float = add_two(0.4)

    print(f"3 + 2 = {this_is_an_integer}")
    print(f"0.4 + 2 = {this_is_a_float}")


main()
