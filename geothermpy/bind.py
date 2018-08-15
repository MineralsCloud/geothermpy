#!/usr/bin/env python

import numpy as np

from geothermpy import Point, runge_kutta_iter, bilinear_interpolate, GeothermalGradient, SurfacePoint


def find_nearest(arr: np.array, x):
    return np.argmin(abs(arr - x))


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


def bind2(gg: GeothermalGradient, p0: Point, h=0.01, n=1000):
    ts = gg.temperatures.values
    ps = gg.pressures
    geothermal_gradient = gg.gradient.values
    trace = [p0]
    for k in range(n):
        x, y, z, w = boundary_check(trace[k], geothermal_gradient)
        print(x, y, z, w)
        print(geothermal_gradient.shape)
        f = bilinear_interpolate(
            SurfacePoint(ts[x], ps[y], geothermal_gradient[x, y]),
            SurfacePoint(ts[x], ps[w], geothermal_gradient[x, w]),
            SurfacePoint(ts[z], ps[y], geothermal_gradient[z, y]),
            SurfacePoint(ts[z], ps[w], geothermal_gradient[z, w])
        )
        p_next = runge_kutta_iter(trace[k], f, h)
        trace.append(p_next)
    return trace


def bind(gg, p0: Point, h=0.01, n=1000):
    ts = gg.index
    ps = np.array(gg.columns, dtype=float)
    geothermal_gradient = gg.values
    trace = [p0]
    for k in range(n):
        x, y = find_nearest(ts, p0.x), find_nearest(ps, p0.y)
        z = x + 10
        w = y + 10
        print(ts[x], ps[y])
        f = bilinear_interpolate(
            SurfacePoint(ts[x], ps[y], geothermal_gradient[x, y]),
            SurfacePoint(ts[x], ps[w], geothermal_gradient[x, w]),
            SurfacePoint(ts[z], ps[y], geothermal_gradient[z, y]),
            SurfacePoint(ts[z], ps[w], geothermal_gradient[z, w])
        )
        p_next = runge_kutta_iter(trace[k], f, h)
        trace.append(p_next)
    return trace
