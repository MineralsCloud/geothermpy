#!/usr/bin/env python

import pandas

__all__ = [
    'load_csv'
]


def load_csv(d: dict) -> dict:
    return {k: pandas.read_csv(v) for k, v in d.items()}
