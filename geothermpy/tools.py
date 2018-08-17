#!/usr/bin/env python

from bisect import bisect_right

from geothermpy import Point

__all__ = [
    'find_le',
    'find_gt'
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


def check(ps, ts):
    def f(p: Point):
        return find_le(ps, p.x), find_le(ts, p.y)

    return f


def find_gt(arr, x):
    """
    Find the leftmost index whose value is greater than *x*.

    :param arr:
    :param x:
    :return:
    """
    i = bisect_right(arr, x)
    if i != len(arr):
        return i
    raise ValueError("The argument *arr* is not sorted, the algorithm might not work!")


if __name__ == '__main__':
    import doctest

    doctest.testmod()
