#!/usr/bin/env python

import numpy as np
import pandas as pd

__all__ = [
    'GeothermalGradient'
]


class GeothermalGradient:
    def __init__(self, alpha, volume, cp):
        self.alpha = alpha
        self.volume = volume
        self.cp = cp
        self.temperatures = alpha.iloc[:, 0]
        self.pressures = np.array(alpha.columns[1:], dtype=float)

    def calculate_gradient(self):
        return ((self.alpha * self.volume / self.cp).T * self.temperatures).T

    @property
    def gradient(self):
        return self.calculate_gradient()
