#!/usr/bin/env python

import pandas as pd

__all__ = [
    'load_geothermal_gradient'
]


def load_geothermal_gradient(file: str):
    return pd.read_csv(file).set_index('T(K)\P(GPa)')
