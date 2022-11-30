"""How to preserve decorated function name and docstring."""


import sys
import functools


def do_not_preserve(func):
    def wrapper_do_not_preserve(*args, **kwargs):
        """Wrapper function."""
        return func(*args, **kwargs)
    return wrapper_do_not_preserve


def preserve(func):
    @functools.wraps(func)
    def wrapper_preserve(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper_preserve


def main():
    @do_not_preserve
    def who_am_i():
        """Who am I function."""
        return "\nWho am I?"

    print(who_am_i())
    print("Func name:", who_am_i.__name__)
    print("Func docstring:", who_am_i.__doc__)

    @preserve
    def who_am_i():
        """Who am I function."""
        return "\nWho am I?"

    print(who_am_i())
    print("Func name:", who_am_i.__name__)
    print("Func docstring:", who_am_i.__doc__)


if __name__ == "__main__":
    sys.exit(main())
