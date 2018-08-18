#!/usr/bin/env python

from typing import Callable

import pandas as pd

from geothermpy import Point, SurfacePoint, bilinear_interpolate, runge_kutta_iter, find_lower_bound


def inject_find_lower_bound(ps, ts, geothermal_gradient) -> Callable:
    def g(x, y):
        i, j = find_lower_bound(ps, ts)(x, y)
        k, l = i + 1, j + 1
        if k == len(ps) or l == len(ts):
            raise IndexError("The index has reached the last of pressures or temperatures!")
        interpolated_function: Callable = bilinear_interpolate(
            SurfacePoint(ps[i], ts[j], geothermal_gradient[j, i]),
            SurfacePoint(ps[i], ts[l], geothermal_gradient[l, i]),
            SurfacePoint(ps[k], ts[j], geothermal_gradient[j, k]),
            SurfacePoint(ps[k], ts[l], geothermal_gradient[l, k])
        )
        return interpolated_function(x, y)

    return g


def bind(geothermal_gradient: pd.DataFrame, p0: Point, h=0.01, n=1000):
    ts = geothermal_gradient.index.astype('float').values
    ps = geothermal_gradient.columns.astype('float').values
    trace = [p0]
    for m in range(n):
        g = inject_find_lower_bound(ps, ts, geothermal_gradient.values)
        try:
            p_next = runge_kutta_iter(trace[m], g, h)
        except IndexError:
            return trace
        trace.append(p_next)
    return trace
