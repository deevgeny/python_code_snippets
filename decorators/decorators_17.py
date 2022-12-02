"""LRU (Least Recently Used) cache by functools."""


import sys
import functools


@functools.lru_cache(maxsize=4)
def fib(num):
    print(f"Calculating fib({num})")
    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)


def main():
    print(fib(10))
    print()
    print(fib(8))
    print()
    print(fib(3))
    print()
    print(fib.cache_info())


if __name__ == "__main__":
    sys.exit(main())
