"""Decorators with arguments."""


import sys
import functools


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper_repeat
    return decorator_repeat


@repeat(num_times=3)
def hello(name):
    print(f"Hello {name}!")


def main():
    hello("user")


if __name__ == "__main__":
    sys.exit(main())
