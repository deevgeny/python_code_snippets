"""Simple decorators examples."""


import sys


def simple_decorator(func):
    def wrapper():
        print("Do something before the function is called.")
        func()
        print("Do something after the function is called.")
    return wrapper


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


def hello():
    print("Hello!")


hello = simple_decorator(hello)


def main():
    hello()
    print()


    @simple_decorator
    def say_goodbye():
        print("Goodbye!")


    say_goodbye()


if __name__ == "__main__":
    sys.exit(main())
