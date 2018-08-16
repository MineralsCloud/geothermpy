#!/usr/bin/env python

import numpy as np
import bisect

from geothermpy import Point, runge_kutta_iter, bilinear_interpolate, SurfacePoint
import pandas as pd


def find_le(arr, x):
    """
    Find rightmost value less than or equal to *x*.

    :param arr:
    :param x:
    :return:
    """
    i = bisect.bisect_right(arr, x)
    if i:
        return i - 1
    raise ValueError("The argument *arr* is not sorted, the algorithm might not work!")


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
        x, y = find_le(ps, trace[k].x), find_le(ts, trace[k].y)
        if x == len(ps) - 1:
            x = len(ps) - 2
        z = x + 2
        if y == len(ts) - 1:
            y = len(ts) - 2
        w = y + 2
        f = bilinear_interpolate(
            SurfacePoint(ps[x], ts[y], geothermal_gradient.iloc[y, x]),
            SurfacePoint(ps[x], ts[w], geothermal_gradient.iloc[w, x]),
            SurfacePoint(ps[z], ts[y], geothermal_gradient.iloc[y, z]),
            SurfacePoint(ps[z], ts[w], geothermal_gradient.iloc[w, z])
        )
        p_next = runge_kutta_iter(trace[k], f, h)
        trace.append(p_next)
    return trace


if __name__ == '__main__':
    import doctest

    doctest.testmod()
