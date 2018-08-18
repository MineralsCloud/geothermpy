#!/usr/bin/env python

from typing import Callable

import pandas as pd

from geothermpy import Point, SurfacePoint, bilinear_interpolate, runge_kutta_iter, find_le


def find_lower_bounds(xs, ys) -> Callable:
    """
    A two-dimensional version of ``find_le`` function.

    :param xs: An array whose elements are monotonic increasing in the x direction.
    :param ys: An array whose elements are monotonic increasing in the y direction.
    :return: A closure that could return the lower bounds of an ``(x, y)`` coordinate pair, restricted in *xs* and *ys*,
        respectively.
    """

    def f(x, y):
        """
        A function that accept an ``(x, y)`` coordinate pair, and return the rightmost indices whose values
        are less than or equal to *x* and *y*, respectively.

        :param x: The coordinate in the x direction that needs to be found the lower bound.
        :param y: The coordinate in the y direction that needs to be found the lower bound.
        :return: A tuple of indices which specifies the lowers bounds of *x* and *y*, respectively.
        """
        return find_le(xs, x), find_le(ys, y)

    return f


def inject_find_lower_bound(ps, ts, geothermal_gradient) -> Callable:
    def g(x, y):
        m, n = find_lower_bounds(ps, ts)(x, y)
        o, p = m + 1, n + 1
        interpolated_function: Callable = bilinear_interpolate(
            SurfacePoint(ps[m], ts[n], geothermal_gradient[n, m]),
            SurfacePoint(ps[m], ts[p], geothermal_gradient[p, m]),
            SurfacePoint(ps[o], ts[n], geothermal_gradient[n, o]),
            SurfacePoint(ps[o], ts[p], geothermal_gradient[p, o])
        )
        return interpolated_function(x, y)

    return g


def bind(geothermal_gradient: pd.DataFrame, p0: Point, h=0.01, n=1000):
    ts = geothermal_gradient.index.astype('float').values
    ps = geothermal_gradient.columns.astype('float').values
    trace = [p0]
    for i in range(n):
        g = inject_find_lower_bound(ps, ts, geothermal_gradient.values)
        try:
            p_next = runge_kutta_iter(trace[i], g, h)
        except IndexError:
            return trace
        trace.append(p_next)
    return trace
