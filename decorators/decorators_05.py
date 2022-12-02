"""Timing decorator."""


import sys
import functools
import time


def timer(func):
    """Check runtime of decorated function."""
    functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"Finished {func.__name__!r} in {runtime:.4f} secs")
        return value
    return wrapper_timer


@timer
def waste_time(val):
    for _ in range(val):
        sum([i ** 2 for i in range(val)])


def main():
    waste_time(100)


if __name__ == "__main__":
    sys.exit(main())
