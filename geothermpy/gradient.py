#!/usr/bin/env python

import numpy as np
import pandas as pd

__all__ = [
    'GeothermalGradient'
]


class GeothermalGradient:
    def __init__(self, alpha, volume, cp):
        self.alpha = alpha.values
        self.volume = volume.values
        self.cp = cp.values
        self.temperatures = alpha.iloc[:, 0]
        self.pressures = np.array(alpha.columns[1:], dtype=float)
        self._gradient = None

    def calculate_gradient(self):
        df = pd.DataFrame(((self.alpha * self.volume / self.cp).T * self.temperatures).T, columns=self.pressures)
        self._gradient = df.insert(0, 'T (K)', self.temperatures)

    @property
    def gradient(self):
        return self._gradient
