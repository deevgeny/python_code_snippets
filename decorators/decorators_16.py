"""Cache all return values of a function."""


import sys
import functools


def cache(func):
    """Keep a cache of all previous function calls."""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache


def count_calls(func):
    """Count function calls."""
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls


@cache
@count_calls
def fib(num):
    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)


def main():
    print(fib(8))
    print()
    print(fib(5))


if __name__ == "__main__":
    sys.exit(main())
