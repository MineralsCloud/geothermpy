#!/usr/bin/env python

from geothermpy import load_csv, bind, Point, GeothermalGradient

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

    dg = GeothermalGradient(alpha, v, cp).calculate_gradient()

    bind.bind(dg, Point(51, 300))
