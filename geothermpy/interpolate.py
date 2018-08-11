#!/usr/bin/env python

from geothermpy import Point, rectangle_to_points

__all__ = [
    'linear_interpolate',
    'bilinear_interpolate'
]


def linear_interpolate(p1: Point, p2: Point):
    x1, x2, y1, y2 = p1.x, p2.x, p1.y, p2.y
    return lambda x: ((x2 - x) * y1 + (x - x1) * y2) / (x2 - x1)


def bilinear_interpolate(rec):
    def f(x, y):
        a, b, c, d = rectangle_to_points(rec)
        y1, y2 = a.y, b.y
        f1 = linear_interpolate(a, c)
        f2 = linear_interpolate(b, d)
        return ((y2 - y) * f1(x) + (y - y1) * f2(x)) / (y2 - y1)
    return f
