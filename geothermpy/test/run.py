#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd

from geothermpy import bind, Point, load_geothermal_gradient

if __name__ == '__main__':
    gg = load_geothermal_gradient('adiabat 2.csv')
    trace = bind.bind(gg, Point(24, 1876.80005), h=0.01, n=100000)
    xs = list(map(lambda x: x.x, trace))
    ys = list(map(lambda x: x.y, trace))

    fig, ax = plt.subplots()
    ax.plot(xs, ys, label="my result")

    ref = pd.read_csv('data 2.csv')
    ax.plot(ref.loc[:, 'P(GPa)'], ref.loc[:, 'T(K)'], label="renata result")

    ax.set_xlabel(r"$P$ (GPa)")
    ax.set_ylabel(r"$T$ (K)")
    ax.legend(loc="best")
    ax.set_title(r"adiabatic $T(P)$")
    fig.savefig('run.pdf')
    plt.show()
