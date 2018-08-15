#!/usr/bin/env python

import matplotlib.pyplot as plt

__all__ = [
    'plot_trace'
]


def plot_trace(points):
    xs = list(map(lambda x: x.x, points))
    ys = list(map(lambda x: x.y, points))
    plt.plot(xs, ys)
    plt.show()
