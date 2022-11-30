"""Improved slow down decorator."""


import sys
import functools
import time


def slow_down(_func=None, *, rate=1):
    """Wait given amount of seconds before calling the function"""
    def decorator_slow_down(func):
        @functools.wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapper_slow_down

    if _func is None:
        return decorator_slow_down
    return decorator_slow_down(_func)


@slow_down(rate=2)
def accelerate(target, speed=0):
    if speed == target:
        print("Done!")
        return
    print(speed)
    accelerate(target, speed + 1)


def main():
    accelerate(3)
    print("Call slow down.")
    slow_down()
    print("Well done!")


if __name__ == "__main__":
    sys.exit(main())
