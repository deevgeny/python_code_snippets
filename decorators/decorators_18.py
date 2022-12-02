"""Add attribute to a function."""


import sys
import math


def add_attribute(attr):
    """Add attribute to a function"""
    def decorator_add_attribute(func):
        func.attr = attr
        return func
    return decorator_add_attribute


@add_attribute("cm3")
def cylinder_volume(r, h):
    """Calculate cylinder volume."""
    return math.pi * r ** 2 * h


def main():
    print(cylinder_volume(5, 10))
    print(cylinder_volume.attr)
    print(cylinder_volume.__doc__)


if __name__ == "__main__":
    sys.exit(main())
