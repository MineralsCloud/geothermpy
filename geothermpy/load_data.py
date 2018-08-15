#!/usr/bin/env python

import pandas as pd

__all__ = [
    'load_csv',
    'load_geothermal_gradient'
]


def load_csv(d: dict) -> dict:
    for k, v in d.items():
        m = pd.read_csv(v)
        d.update({k: m.set_index('Unnamed: 0')})
    return d


def load_geothermal_gradient(file: str):
    return pd.read_csv(file).set_index('T(K)\P(GPa)')
