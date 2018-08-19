#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd

from geothermpy import bind, Point, load_geothermal_gradient

if __name__ == '__main__':
    gg = load_geothermal_gradient('data/example.csv')
    trace = bind.generate_trace(gg, Point(24, 1876.80005), h=0.01, n=100000)
    xs = list(map(lambda x: x.x, trace))
    ys = list(map(lambda x: x.y, trace))

    fig, ax = plt.subplots()
    ax.plot(xs, ys, label="Python version result")

    ref = pd.read_csv('out.csv')
    ax.plot(ref.loc[:, 'P(GPa)'], ref.loc[:, 'T(K)'], label="Fortran version result")

    ax.set_xlabel(r"$P$ (GPa)")
    ax.set_ylabel(r"$T$ (K)")
    ax.legend(loc="best")
    ax.set_title(r"adiabatic $T(P)$")
    plt.show()
