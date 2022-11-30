"""Slow down decorator."""


import sys
import functools
import time


def slow_down(func):
    """Wait 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down


@slow_down
def accelerate(target, speed=0):
    if speed == target:
        print("Done!")
        return
    print(speed)
    accelerate(target, speed + 1)


def main():
    accelerate(10)


if __name__ == "__main__":
    sys.exit(main())
