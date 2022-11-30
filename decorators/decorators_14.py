"""Singletons with decorators."""


import sys
import functools


def singleton(cls):
    """Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class Single:
    pass


def main():
    first = Single()
    second = Single()
    print(first is second)


if __name__ == "__main__":
    sys.exit(main())
