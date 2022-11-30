"""Stateful decorator."""


import sys
import functools


def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls


@count_calls
def hello():
    print("Hello!")


@count_calls
def bye():
    print("Bye!")


def main():
    hello()
    hello()
    print(hello.num_calls)
    print()
    bye()
    print(bye.num_calls)


if __name__ == "__main__":
    sys.exit(main())
