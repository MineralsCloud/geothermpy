#!/usr/bin/env python

from typing import Callable

import numpy as np
import pandas as pd

from geothermpy import Point, SurfacePoint, bilinear_interpolate, runge_kutta_iter, find_le

__all__ = [
    'find_lower_bounds',
    'inject_find_lower_bound',
    'generate_trace'
]


def find_lower_bounds(xs, ys) -> Callable:
    """
    A two-dimensional version of ``find_le`` function.

    :param xs: An array whose elements are monotonic increasing in the x-direction.
    :param ys: An array whose elements are monotonic increasing in the y-direction.
    :return: A closure that could return the lower bounds of an ``(x, y)`` coordinate pair, restricted in *xs* and *ys*,
        respectively.
    """

    def f(x, y):
        """
        A function that accept an ``(x, y)`` coordinate pair, and return the rightmost indices whose values
        are less than or equal to *x* and *y*, respectively.

        :param x: The coordinate in the x-direction that needs to be found the lower bound.
        :param y: The coordinate in the y-direction that needs to be found the lower bound.
        :return: A tuple of indices which specifies the lowers bounds of *x* and *y*, respectively.
        """
        return find_le(xs, x), find_le(ys, y)

    return f


def inject_find_lower_bound(ps, ts, geothermal_gradient) -> Callable:
    """
    Inject a bound check into the bilinear interpolation algorithm. Will be used in the integration algorithm.

    :param ps: Check whether the x-coordinate is within the pressure range.
    :param ts: Check whether the x-coordinate is within the pressure range.
    :param geothermal_gradient: Must be a Numpy array that specifying the geothermal gradient
        :math:`\\frac{ dT }{ dP }(P, T)`. The temperatures should be in an increasing order from top to bottom,
        and the pressures should be in an increasing order from left to right.
    :return: A function that can evaluate the geothermal gradient on any point :math:`(x, y)` within
        the smallest rectangle region enclosing it.
    """

    def g(x, y):
        m, n = find_lower_bounds(ps, ts)(x, y)
        o, p = m + 1, n + 1
        interpolated_function: Callable = bilinear_interpolate(
            SurfacePoint(ps[m], ts[n], geothermal_gradient[n, m]),  # Note the order of indices!
            SurfacePoint(ps[m], ts[p], geothermal_gradient[p, m]),  # Note the order of indices!
            SurfacePoint(ps[o], ts[n], geothermal_gradient[n, o]),  # Note the order of indices!
            SurfacePoint(ps[o], ts[p], geothermal_gradient[p, o])  # Note the order of indices!
        )
        return interpolated_function(x, y)  # Evaluate the geothermal gradient on point (x, y).

    return g


def generate_trace(geothermal_gradient, p0: Point, h=0.01, n=1000):
    """
    Solve the initial value problem by an integration method. Return a trace of points on each integration step.

    :param geothermal_gradient: A Pandas ``DataFrame`` specifying the geothermal gradient
        :math:`\\frac{ dT }{ dP }(P, T)`, with ``columns`` attribute to be pressures and ``index`` attribute to be
        temperatures. The temperatures should be in an increasing order from top to bottom,
        and the pressures should be in an increasing order from left to right.
    :param p0: A ``Point`` specifying the initial value of the ODE, note that the final result is sensitive to the
        initial value so it has to be carefully chosen.
    :param h: The interval between each pressure step. The default value is ``0.01``.
    :param n: Generate *n* steps using the integration method, if there is no index out of bounds (of the
        pressures) during the integration. If that happens, the accumulated trace up to that step is returned.
        Note that the total number of steps *n* includes the initial value, so the number of generated
        steps is :math:`n-1`.
    :return: A numpy array contains at most *n* ``Point``s, depending on whether there is an index out of bounds.
    """
    if not isinstance(geothermal_gradient, pd.DataFrame):
        raise TypeError("The argument *geothermal_gradient* should be a Pandas DataFrame!")

    ts = geothermal_gradient.index.astype('float').values
    ps = geothermal_gradient.columns.astype('float').values
    trace = np.empty(n, dtype=Point)
    trace[0] = p0
    f = inject_find_lower_bound(ps, ts, geothermal_gradient.values)
    for i in range(n - 1):
        try:
            trace[i + 1] = runge_kutta_iter(trace[i], f, h)
        except IndexError:
            return trace[:i + 1]
    return trace
