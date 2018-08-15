#!/usr/bin/env python

import typing
from collections import namedtuple

__all__ = [
    'Point',
    'Rectangle',
    'SurfacePoint',
    'rectangle_to_points',
    'within_rectangle',
    'point_to_surface_point'
]

Point = namedtuple('Point', ['x', 'y'])
SurfacePoint = namedtuple('SurfacePoint', ['x', 'y', 'z'])


class Rectangle:
    def __init__(self, lx, rx, dy, uy):
        self.lx = min(lx, rx)
        self.rx = max(lx, rx)
        self.dy = min(dy, uy)
        self.uy = max(dy, uy)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.lx}, {self.rx}, {self.dy}, {self.uy})"


def rectangle_to_points(rec: Rectangle) -> typing.Tuple[Point, ...]:
    lx, rx, dy, uy = rec.lx, rec.rx, rec.dy, rec.uy
    return Point(lx, dy), Point(lx, uy), Point(rx, dy), Point(rx, uy)


def within_rectangle(rec: Rectangle, t: Point) -> bool:
    lx, rx, dy, uy = rec.lx, rec.rx, rec.dy, rec.uy
    x, y = t.x, t.y
    return lx <= x <= rx and dy <= y <= uy


def point_to_surface_point(p: Point, z: float) -> SurfacePoint:
    return SurfacePoint(p.x, p.y, z)
