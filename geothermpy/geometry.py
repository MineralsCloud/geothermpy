#!/usr/bin/env python

from collections import namedtuple

__all__ = [
    'Point',
    'Rectangle',
    'rectangle_to_points'
]

Point = namedtuple('Point', ['x', 'y'])
Rectangle = namedtuple('Rectangle', ['lx', 'ly', 'rx', 'ry'])


def rectangle_to_points(rec: Rectangle):
    lx, rx, ly, ry = rec.lx, rec.ly, rec.rx, rec.ry
    return Point(lx, ly), Point(lx, ry), Point(rx, ly), Point(rx, ry)
