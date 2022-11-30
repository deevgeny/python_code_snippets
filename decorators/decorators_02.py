"""How to return values from decorated function."""


import sys


def call_once(func):
    """Call decorated function and do not return anything."""
    def wrapper_call_once(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper_call_once


@call_once
def return_hello(name):
    print("Prepare hello...")
    return f"Hello {name}!"


def call_once_and_return_function(func):
    """Call decorated function then return it."""
    def wrapper_call_once_and_return_function(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, *kwargs)
    return wrapper_call_once_and_return_function


@call_once_and_return_function
def return_goodbye(name):
    print("Prepare goodbye...")
    return f"Goodbye {name}!"


def call_once_and_return_value(func):
    """Call decorated function and return value."""
    def wrapper_call_once_and_return_value(*args, **kwargs):
        val = func(*args, **kwargs)
        return val
    return wrapper_call_once_and_return_value


@call_once_and_return_value
def return_goodbye_again(name):
    print("Prepare goodbye again...")
    return f"Goodbye again {name}!"


def just_return_function(func):
    """Return decorated function."""
    def wrapper_just_return_function(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper_just_return_function


@just_return_function
def maybe_hello_again(name):
    print("Prepare hello once again...")
    return f"Hello once again {name}!"


def main():
    print("\nCall decorated function.")
    # Call decorated function
    returned_func = return_hello("user")
    # Print decorator output
    print(returned_func)

    print("\nCall decorated function and then return it.")
    # Call decorated function and return it
    returned_function = return_goodbye("user")
    # Call returned function and print its output
    print(returned_function)

    print("\nCall decorated function and return value.")
    # Call decorated function, return value
    returned_value = return_goodbye_again("user")
    # Print returned value
    print(returned_value)

    print("\nReturn decorated function.")
    # Return function
    returned_function = maybe_hello_again("user")
    # Call returned function and print its output
    print(returned_function)


if __name__ == "__main__":
    sys.exit(main())
