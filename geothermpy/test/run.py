#!/usr/bin/env python

from geothermpy import load_csv, bind, Point, GeothermalGradient, plot, load_geothermal_gradient

if __name__ == '__main__':
    d = load_csv({
        'alpha': '5000_alpha_tp.csv',
        'cp': '5000_cp_tp.csv',
        'v': '5000_v_tp.csv'
    })

    alpha = d['alpha']
    cp = d['cp']
    v = d['v']
    ts = v.iloc[:, 0]

    # gg = GeothermalGradient(alpha, v, cp)
    gg = load_geothermal_gradient('adiabat.csv')
    trace = bind.bind(gg, Point(1000, 20))
    plot.plot_trace(trace)
