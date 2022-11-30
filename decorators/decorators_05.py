"""Debug decorator."""


import sys
import functools


def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_list = [repr(a) for a in args]
        kwargs_list = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_list + kwargs_list)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug


@debug
def check_me(name, title=None):
    if title is None:
        return f"Hello {name}!"
    return f"Hello {title} {name}!"


def main():
    print(check_me("user"))
    print()
    print(check_me("user", "Mr."))
    print()
    print(check_me("user", title="Master"))


if __name__ == "__main__":
    sys.exit(main())
