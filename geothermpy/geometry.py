#!/usr/bin/env python

import typing
from collections import namedtuple

__all__ = [
    'Point',
    'Rectangle',
    'SurfacePoint',
    'rectangle_to_points',
    'within_rectangle',
]

Point = namedtuple('Point', ['x', 'y'])
SurfacePoint = namedtuple('SurfacePoint', ['x', 'y', 'z'])


class Rectangle:
    """
    A rectangle region on a two-dimensional plane.

    :param lx: The left x-coordinate of the rectangle.
    :param rx: The right x-coordinate of the rectangle.
    :param ly: The lower y-coordinate of the rectangle.
    :param uy: The upper y-coordinate of the rectangle.
    """

    def __init__(self, lx, rx, ly, uy):
        self.lx = min(lx, rx)
        self.rx = max(lx, rx)
        self.ly = min(ly, uy)
        self.uy = max(ly, uy)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.lx}, {self.rx}, {self.ly}, {self.uy})"


def rectangle_to_points(rec: Rectangle):
    """
    Given a ``Rectangle`` class, convert it to four ``Point``s, with order: lower-left, upper-left, lower-right, and
    upper-right.

    :param rec: A ``Rectangle`` class.
    :return: A tuple of four ``Point``s.
    """
    lx, rx, ly, uy = rec.lx, rec.rx, rec.ly, rec.uy
    return Point(lx, ly), Point(lx, uy), Point(rx, ly), Point(rx, uy)


def within_rectangle(rec: Rectangle, p: Point) -> bool:
    """
    Check whether a point *p* is within a rectangle region.

    .. doctest::

       >>> within_rectangle(Rectangle(1, 10, 5, 20), Point(6, 4))
       False
       >>> within_rectangle(Rectangle(1, 10, 5, 20), Point(6, 15))
       True
       >>> within_rectangle(Rectangle(1, 10, 5, 20), Point(5, 5))
       True
       >>> within_rectangle(Rectangle(1, 10, 5, 20), Point(1, 15))
       True
       >>> within_rectangle(Rectangle(1, 10, 5, 20), Point(1, 5))
       True

    :param rec: A ``Rectangle`` class.
    :param p: A two-dimensional ``Point``.
    :return: Whether the point *p* is within a rectangle region, on boundary is regarded as ``True``.
    """
    lx, rx, dy, uy = rec.lx, rec.rx, rec.ly, rec.uy
    x, y = p.x, p.y
    return lx <= x <= rx and dy <= y <= uy


if __name__ == '__main__':
    import doctest

    doctest.testmod()
