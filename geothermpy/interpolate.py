#!/usr/bin/env python

from typing import Callable

from geothermpy import Point, Rectangle, SurfacePoint, within_rectangle

__all__ = [
    'linear_interpolate',
    'bilinear_interpolate'
]


def linear_interpolate(a, b, f, g) -> Callable:
    """
    Return a function of the linear interpolation between any 2 abstract data points `(a, f)` and `(b, g)`.

    :param a: The x coordinate of the first abstract data point.
    :param b: The x coordinate of the second abstract data point. The argument *a* cannot equal to the argument *b*!
    :param f: The y coordinate of the first abstract data point.
    :param g: The y coordinate of the second abstract data point.
    :return: A closure that can evaluate on any ``x`` between the interval :math:`[a, b]`.
    """
    if a != b:
        def h(x):
            return ((b - x) * f + (x - a) * g) / (b - a)

        return h

    raise ValueError("The argument *a* cannot equal to the argument *b*!")


def bilinear_interpolate(q11: SurfacePoint, q12: SurfacePoint, q21: SurfacePoint, q22: SurfacePoint) -> Callable:
    x1, x2, y1, y2 = q11.x, q21.x, q11.y, q22.y
    v11, v12, v21, v22 = q11.z, q12.z, q21.z, q22.z
    rec = Rectangle(x1, x2, y1, y2)

    def f(x, y):
        if not within_rectangle(rec, Point(x, y)):
            raise ValueError(f"The point ({x}, {y}) is out of boundary {rec}!")
        v1 = linear_interpolate(x1, x2, v11, v21)(x)
        v2 = linear_interpolate(x1, x2, v12, v22)(x)
        return linear_interpolate(y1, y2, v1, v2)(y)

    return f
