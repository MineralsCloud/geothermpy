#!/usr/bin/env python

from numba import float64, vectorize
from scipy.constants import physical_constants, angstrom

BOHR = physical_constants['Bohr radius'][0]
EH_EV = physical_constants['Hartree energy in eV'][0]
RY_EV = physical_constants['Rydberg constant times hc in eV'][0]
EH_J = physical_constants['hartree-joule relationship'][0]
EH_HZ = physical_constants['hartree-hertz relationship'][0]
EH_K = physical_constants['hartree-kelvin relationship'][0]
EH_M_INVERSE = physical_constants['hartree-inverse meter relationship'][0]
EV_M_INVERSE = physical_constants['electron volt-inverse meter relationship'][0]
EV_K = physical_constants['electron volt-kelvin relationship'][0]
RY_J = physical_constants['Rydberg constant times hc in J'][0]


@vectorize([float64(float64)], nopython=True, cache=True)
def b3_to_a3(value):
    """
    Convert the *value* in unit cubic bohr radius to what in cubic angstrom.

    :param value: The value to be converted.
    :return: The converted value.
    """
    return value * (BOHR / angstrom) ** 3
