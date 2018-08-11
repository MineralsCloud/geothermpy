#!/usr/bin/env python

import numpy as np
from geothermpy import Point, bilinear_interpolate, Rectangle


def boundary_check(p: Point, adiabat: np.ndarry):
    c, k = adiabat.shape
    temperature, pressure = p.x, p.y
    x, y, z, w = [1] * 4

    for i in range(c):
        if adiabat(i, 0) <= temperature:
            x = i
    for j in range(k):
        if adiabat(0, j) <= pressure:
            y = j

    if adiabat(0, y) == pressure and adiabat(x, 0) == temperature:
        return adiabat(x, y)

    if x < c:
        z = x + 1
    elif x == c:
        z = x - 1
    else:
        raise IndexError

    if y < k:
        w = y + 1
    elif y == k:
        w = y - 1
    else:
        raise IndexError

    return x, y, z, w


def interp(p: Point, adiabat: np.ndarry):
    x, y, z, w = boundary_check(p, adiabat)
    return bilinear_interpolate(Rectangle(adiabat(x, 1),))


def runge_kutta(p: Point, h=0.01):
    pass
