"""With and without arguments version.
https://peps.python.org/pep-3102/
"""


import sys
import functools


def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    return decorator_repeat(_func)


@repeat
def say_hello():
    print("Hello!")


@repeat(num_times=3)
def hello(name):
    print(f"Hello {name}!")


def main():
    say_hello()
    hello("user")


if __name__ == "__main__":
    sys.exit(main())
