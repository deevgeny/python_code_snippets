"""Intro to decorators."""


import sys


def simple_decorator(func):
    def wrapper():
        print("Do something before the function is called.")
        func()
        print("Do something after the function is called.")
    return wrapper


def hello():
    print("Hello!")


hello = simple_decorator(hello)


@simple_decorator
def say_goodbye():
    print("Goodbye!")


def main():
    hello()
    print()
    say_goodbye()


if __name__ == "__main__":
    sys.exit(main())
