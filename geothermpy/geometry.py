#!/usr/bin/env python

from collections import namedtuple

__all__ = [
    'Point',
    'Rectangle',
    'SurfacePoint',
    'rectangle_to_points',
    'within_rectangle',
]

Point = namedtuple('Point', ['x', 'y'])
SurfacePoint = namedtuple('SurfacePoint', ['x', 'y', 'z'])


class Rectangle:
    def __init__(self, lx, rx, ly, uy):
        self.lx = min(lx, rx)
        self.rx = max(lx, rx)
        self.ly = min(ly, uy)
        self.uy = max(ly, uy)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.lx}, {self.rx}, {self.ly}, {self.uy})"


def rectangle_to_points(rec: Rectangle):
    lx, rx, dy, uy = rec.lx, rec.rx, rec.ly, rec.uy
    return Point(lx, dy), Point(lx, uy), Point(rx, dy), Point(rx, uy)


def within_rectangle(rec: Rectangle, t: Point) -> bool:
    lx, rx, dy, uy = rec.lx, rec.rx, rec.ly, rec.uy
    x, y = t.x, t.y
    return lx <= x <= rx and dy <= y <= uy
