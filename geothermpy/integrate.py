#!/usr/bin/env python

from geothermpy import Point

__all__ = [
    'runge_kutta_iter'
]


def runge_kutta_iter(p: Point, f, h=0.01) -> Point:
    x, y = p.x, p.y
    k1 = h * f(x, y)
    k2 = h * f(x + h / 2, y + k1 / 2)
    k3 = h * f(x + h / 2, y + k2 / 2)
    k4 = h * f(x + h, y + k3)
    return Point(x + h, y + (k1 + 2 * k2 + 2 * k3 + k4) / 6)
