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

    gg = GeothermalGradient(alpha, v, cp)
    bind.bind(gg, Point(51, 300))
