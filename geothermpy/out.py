#!/usr/bin/env python

import pandas as pd
import geothermpy.bind as bind
import numpy as np

__all__ = [
    'TraceWriter'
]


class TraceWriter:
    def __init__(self, trace):
        self._trace = trace

    @property
    def trace(self):
        return self._trace

    @property
    def derivative(self):
        return bind.generate_derivative_from_trace(self._trace)

    def to_csv(self, include_derivative=True, **kwargs):
        xs, ys = np.array([p.x for p in self._trace]), np.array([p.y for p in self._trace])
        if include_derivative:
            df = pd.DataFrame(np.vstack((xs, ys, self.derivative)).T, columns=['P', 'T', 'G'])
        else:
            df = pd.DataFrame(np.vstack((xs, ys)).T, columns=['P', 'T'])
        df.to_csv(**kwargs)
