#!/usr/bin/env python

import numpy as np

from geothermpy import Point, runge_kutta_iter, bilinear_interpolate, SurfacePoint
import pandas as pd


def find_nearest(arr, v) -> int:
    """
    Return the nearest index of *v* in an array *arr*.
    In case of multiple occurrences of the nearest values,
    the index corresponding to the first occurrence is returned.

    .. doctest::
       >>> find_nearest(np.linspace(1, 10), 2.9)
       10
       >>> np.linspace(1, 10)[10]
       2.836734693877551

    :param arr: The array to scan through.
    :param v: Find the nearest value to *v* in the array *arr*.
    :return: A integer specifying the index of the nearest value.
    """
    return abs(arr - v).argmin()


def boundary_check(p: Point, adiabat: np.array):
    c, k = adiabat.shape
    temperature, pressure = p.x, p.y
    x, y, z, w = [1] * 4

    for i in range(c):
        if adiabat[i, 0] <= temperature:
            x = i
    for j in range(k):
        if adiabat[0, j] <= pressure:
            y = j

    if p.x == pressure and p.y == temperature:
        return adiabat[x, y]

    if x == c - 1 and y < k - 1:
        z = x - 1
        w = y + 1
    elif x < c - 1 and y == k - 1:
        z = x + 1
        w = y - 1
    elif x == c - 1 and y < k - 1:
        z = x - 1
        w = y - 1
    elif x < c - 1 and y < k - 1:
        z = x + 1
        w = y + 1

    return x - 1, y - 1, z - 1, w - 1


def bind(geothermal_gradient: pd.DataFrame, p0: Point, h=0.01, n=1000):
    ts = geothermal_gradient.index.astype('float')
    ps = geothermal_gradient.columns.astype('float')
    trace = [p0]
    for k in range(n):
        x, y = find_nearest(ps, trace[k].y), find_nearest(ts, trace[k].x)
        z = x + 1
        w = y + 1
        f = bilinear_interpolate(
            SurfacePoint(ps[x], ts[y], geothermal_gradient.iloc[y, x]),
            SurfacePoint(ps[x], ts[w], geothermal_gradient.iloc[w, x]),
            SurfacePoint(ps[z], ts[y], geothermal_gradient.iloc[y, z]),
            SurfacePoint(ps[z], ts[w], geothermal_gradient.iloc[w, z])
        )
        p_next = runge_kutta_iter(trace[k], f, h)
        print(p_next)
        trace.append(p_next)
    return trace


if __name__ == '__main__':
    import doctest

    doctest.testmod()
