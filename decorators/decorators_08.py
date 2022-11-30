"""Nested decorators."""


import sys
import functools


def do_twice(func):
    functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


def pop_up(func):
    functools.wraps(func)
    def wrapper_pop_up(*args, **kwargs):
        print("Pop up :-)")
        func(*args, **kwargs)
    return wrapper_pop_up


def main():
    @do_twice
    @pop_up
    def hello(name):
        print(f"Hello {name}!")

    # Hint: hello = do_twice(pop_up(hello("user")))
    hello("user")
    print()

    @pop_up
    @do_twice
    def hello(name):
        print(f"Hello {name}!")

    # Hint: hello = pop_up(do_twice(hello("user")))
    hello("user")


if __name__ == "__main__":
    sys.exit(main())
