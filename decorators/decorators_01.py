"""How to decorate functions with arguments."""


import sys


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def hello(name):
    print(f"Hello {name}!")


def main():
    hello("user")


if __name__ == "__main__":
    sys.exit(main())
