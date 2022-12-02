"""Classes as decorators.
Method __call__() is defined to make class instance be callable.
Hint: 
>>>decorated_func = CountCalls(func)
>>>decorated_func(*args, **kwargs)
"""


import sys
import functools


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def hello():
    print("Hello!")


@CountCalls
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
