#!/usr/bin/env python

from geothermpy import Point, Rectangle, SurfacePoint, within_rectangle

__all__ = [
    'linear_interpolate',
    'bilinear_interpolate'
]


def linear_interpolate(a, b, f, g):
    return lambda x: ((b - x) * f + (x - a) * g) / (b - a)


def bilinear_interpolate(q11: SurfacePoint, q12: SurfacePoint, q21: SurfacePoint, q22: SurfacePoint):
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
