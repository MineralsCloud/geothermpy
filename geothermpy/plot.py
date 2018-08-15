#!/usr/bin/env python

import matplotlib.pyplot as plt

__all__ = [
    'plot_trace'
]


def plot_trace(points):
    xs = list(map(lambda x: x.x, points))
    ys = list(map(lambda x: x.y, points))
    fig, ax = plt.subplots()
    ax.plot(ys, xs)
    ax.set_xlabel(r"$P$ (GPa)")
    ax.set_ylabel(r"$T$ (K)")
    ax.set_title(r"adiabatic $T(P)$")
    return fig, ax
