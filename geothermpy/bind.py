#!/usr/bin/env python

import numpy as np

from geothermpy import Point, runge_kutta_iter, point_to_surface_point, bilinear_interpolate, GeothermalGradient


def find_nearest(arr: np.array, x):
    return np.argmin(abs(arr - x))


def bind(gg: GeothermalGradient, p0: Point, h=0.01, n=1000):
    ts = gg.temperatures
    ps = gg.pressures
    geothermal_gradient = gg.gradient.values
    trace = [p0]
    for k in range(n):
        i, j = find_nearest(ts, trace[k].x), find_nearest(ps, trace[k].y)
        f = bilinear_interpolate(
            point_to_surface_point(Point(ts[i], ps[j]), geothermal_gradient[i, j]),
            point_to_surface_point(Point(ts[i], ps[j + 3]), geothermal_gradient[i, j + 3]),
            point_to_surface_point(Point(ts[i + 3], ps[j]), geothermal_gradient[i + 3, j]),
            point_to_surface_point(Point(ts[i + 3], ps[j + 3]), geothermal_gradient[i + 3, j + 3])
        )
        p_next = runge_kutta_iter(trace[k], f, h)
        trace.append(p_next)
    return trace
