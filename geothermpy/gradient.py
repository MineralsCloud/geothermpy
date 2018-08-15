#!/usr/bin/env python

import numpy as np

import geothermpy.unit

__all__ = [
    'GeothermalGradient'
]


class GeothermalGradient:
    def __init__(self, alpha, volumes, cp):
        self.alpha = alpha * 10 ** 5
        self.volumes = geothermpy.unit.b3_to_a3(volumes)
        self.cp = cp
        self.temperatures = alpha.iloc[:, 0]
        self.pressures = np.array(alpha.columns[1:], dtype=float)

    @property
    def gradient(self):
        return ((self.alpha * self.volumes / self.cp).T * self.temperatures).T
