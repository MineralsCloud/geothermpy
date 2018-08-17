#!/usr/bin/env python

from bisect import bisect_right

import pandas as pd

from geothermpy import Point, runge_kutta_iter, bilinear_interpolate, SurfacePoint


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


def bind(geothermal_gradient: pd.DataFrame, p0: Point, h=0.01, n=1000):
    ts = geothermal_gradient.index.astype('float')
    ps = geothermal_gradient.columns.astype('float')
    trace = [p0]
    for m in range(n):
        i, j = find_le(ps, trace[m].x), find_le(ts, trace[m].y)
        k, l = find_gt(ps, trace[m].x), find_gt(ts, trace[m].y)
        f = bilinear_interpolate(
            SurfacePoint(ps[i], ts[j], geothermal_gradient.iloc[j, i]),
            SurfacePoint(ps[i], ts[l], geothermal_gradient.iloc[l, i]),
            SurfacePoint(ps[k], ts[j], geothermal_gradient.iloc[j, k]),
            SurfacePoint(ps[k], ts[l], geothermal_gradient.iloc[l, k])
        )
        p_next = runge_kutta_iter(trace[m], f, h)
        trace.append(p_next)
    return trace


if __name__ == '__main__':
    import doctest

    doctest.testmod()
