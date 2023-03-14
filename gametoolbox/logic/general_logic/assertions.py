"""
A collection of functions to be used as shorthand to keep assert statements DRY.
These functions MUST return a boolean value.
"""


def even(x: int):
    return x % 2 == 0


def odd(x: int):
    return not even(x)


def main():
    pass


if __name__ == "__main__":
    main()
