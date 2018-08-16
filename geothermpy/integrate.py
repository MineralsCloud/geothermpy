#!/usr/bin/env python

from geothermpy import Point

__all__ = [
    'runge_kutta_iter'
]


def runge_kutta_iter(p: Point, f, h=0.01) -> Point:
    """
    Integrate an initial value problem

    .. math::

       \begin{align}
           y(x_0) &= y_0, \\
           \\frac{ dy }{ dx } &= f(x, y),
       \end{align}

    where :math:`y` is an unknown function (scalar or vector) of variable :math:`x`.

    :param p: A point that specifies the initial value, i.e., :math:`(x_0, y_0)`.
    :param f: A bivariate function of :math:`x` and :math:`y`, which specifies the ODE.
    :param h: The integration time step, by default is ``0.01``.
    :return: A point :math:`(x, y)` of the next time step.
    """
    x, y = p.x, p.y
    k1 = h * f(x, y)
    k2 = h * f(x + h / 2, y + k1 / 2)
    k3 = h * f(x + h / 2, y + k2 / 2)
    k4 = h * f(x + h, y + k3)
    return Point(x + h, y + (k1 + 2 * k2 + 2 * k3 + k4) / 6)
