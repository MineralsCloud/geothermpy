#!/usr/bin/env python

import bisect

import pandas as pd

from geothermpy import Point, runge_kutta_iter, bilinear_interpolate, SurfacePoint


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


def bind(geothermal_gradient: pd.DataFrame, p0: Point, h=0.01, n=1000):
    ts = geothermal_gradient.index.astype('float')
    ps = geothermal_gradient.columns.astype('float')
    trace = [p0]
    for k in range(n):
        i, j = find_le(ps, trace[k].x), find_le(ts, trace[k].y)
        f = bilinear_interpolate(
            SurfacePoint(ps[i], ts[j], geothermal_gradient.iloc[j, i]),
            SurfacePoint(ps[i], ts[j + 1], geothermal_gradient.iloc[j + 1, i]),
            SurfacePoint(ps[i + 1], ts[j], geothermal_gradient.iloc[j, i + 1]),
            SurfacePoint(ps[i + 1], ts[j + 1], geothermal_gradient.iloc[j + 1, i + 1])
        )
        p_next = runge_kutta_iter(trace[k], f, h)
        trace.append(p_next)
    return trace


if __name__ == '__main__':
    import doctest

    doctest.testmod()
