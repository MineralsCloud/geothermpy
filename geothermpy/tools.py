#!/usr/bin/env python

from bisect import bisect_right

__all__ = [
    'find_le',
    'find_lower_bound',
]


def find_le(arr, x):
    """
    Find the rightmost index whose value is less than or equal to *x*.

    :param arr:
    :param x:
    :return:
    """
    i = bisect_right(arr, x)
    if i:
        return i - 1
    raise ValueError("The argument *arr* is not sorted, the algorithm might not work!")


def find_lower_bound(ps, ts):
    def f(x, y):
        return find_le(ps, x), find_le(ts, y)

    return f


if __name__ == '__main__':
    import doctest

    doctest.testmod()
