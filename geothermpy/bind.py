#!/usr/bin/env python

import pandas as pd
from typing import Callable

from geothermpy import Point, SurfacePoint, bilinear_interpolate, runge_kutta_iter, find_lower_bound


def inject_find_lower_bound(ps, ts, geothermal_gradient) -> Callable:
    def g(x, y):
        i, j = find_lower_bound(ps, ts)(x, y)
        interpolated: Callable = bilinear_interpolate(
            SurfacePoint(ps[i], ts[j], geothermal_gradient.iloc[j, i]),
            SurfacePoint(ps[i], ts[j + 1], geothermal_gradient.iloc[j + 1, i]),
            SurfacePoint(ps[i + 1], ts[j], geothermal_gradient.iloc[j, i + 1]),
            SurfacePoint(ps[i + 1], ts[j + 1], geothermal_gradient.iloc[j + 1, i + 1])
        )
        return interpolated(x, y)

    return g


def bind(geothermal_gradient: pd.DataFrame, p0: Point, h=0.01, n=1000):
    ts = geothermal_gradient.index.astype('float')
    ps = geothermal_gradient.columns.astype('float')
    trace = [p0]
    for m in range(n):
        g = inject_find_lower_bound(ps, ts, geothermal_gradient)
        p_next = runge_kutta_iter(trace[m], g, h)
        trace.append(p_next)
    return trace
