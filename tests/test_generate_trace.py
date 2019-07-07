#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from geothermpy import bind, Point, load_geothermal_gradient

if __name__ == '__main__':
    gg = load_geothermal_gradient('data/example.csv')
    trace = bind.generate_trace(gg, Point(24, 1876.80005), h=0.01, n=100000)
    xs, ys = np.array([p.x for p in trace]), np.array([p.y for p in trace])

    fig, ax = plt.subplots()
    ax.plot(xs, ys, label="Python version result")

    ref = pd.read_csv('data/out.csv')
    ax.plot(ref.loc[:, 'P(GPa)'], ref.loc[:, 'T(K)'], label="Fortran version result")

    ax.set_xlabel(r"$P$ (GPa)")
    ax.set_ylabel(r"$T$ (K)")
    ax.legend(loc="best")
    ax.set_title(r"adiabatic $T(P)$")
    plt.show()
