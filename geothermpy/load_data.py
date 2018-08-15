#!/usr/bin/env python

import pandas

__all__ = [
    'load_csv'
]


def load_csv(d: dict) -> dict:
    for k, v in d.items():
        m = pandas.read_csv(v)
        d.update({k: m.set_index('Unnamed: 0')})
    return d
