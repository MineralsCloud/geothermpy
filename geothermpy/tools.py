#!/usr/bin/env python

from bisect import bisect_right

__all__ = [
    'find_le',
]


def find_le(arr, x):
    """
    Find the rightmost index whose value is less than or equal to *x*. The algorithm is referenced from
    `Python's official documentation <https://docs.python.org/3.7/library/bisect.html#bisect.bisect_right>`_.

    .. doctest::

       >>> find_le([1, 2, 3, 4, 5], 3.1)
       2
       >>> find_le([1, 2, 3, 3.2, 5], 3)
       2

    :param arr: An array whose elements are monotonic increasing.
    :param x: A value could be used to compare with the elements in *arr*.
    :return: The rightmost index whose value is less than or equal to *x*.
    """
    i = bisect_right(arr, x)
    if i:
        return i - 1
    raise ValueError


if __name__ == '__main__':
    import doctest

    doctest.testmod()
