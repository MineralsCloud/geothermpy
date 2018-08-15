#!/usr/bin/env python

import numpy as np

__all__ = [
    'GeothermalGradient'
]


class GeothermalGradient:
    def __init__(self, alpha, volumes, cp):
        self.alpha = alpha
        self.volumes = volumes
        self.cp = cp
        self.temperatures = alpha.iloc[:, 0]
        self.pressures = np.array(alpha.columns[1:], dtype=float)

    @property
    def gradient(self):
        return ((self.alpha * self.volumes / self.cp).T * self.temperatures).T
