"""Register decorator."""


import sys
import random


FUNCTIONS = dict()


def register(func):
    """Register a function as a plug-in"""
    FUNCTIONS[func.__name__] = func


@register
def hello(name):
    return f"Hello {name}!"


@register
def hi(name):
    return f"Hi {name}!"


def random_greet(name):
    func_name, func = random.choice(list(FUNCTIONS.items()))
    print(f"Using {func_name!r}")
    print(func(name))


def main():
    random_greet("user")
    print()
    random_greet("user")
    print()
    random_greet("user")


if __name__ == "__main__":
    sys.exit(main())
