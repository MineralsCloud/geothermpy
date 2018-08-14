#!/usr/bin/env python

import typing
from collections import namedtuple

__all__ = [
    'Point',
    'Rectangle',
    'rectangle_to_points'
]

Point = namedtuple('Point', ['x', 'y'])
Rectangle = namedtuple('Rectangle', ['lx', 'ly', 'rx', 'ry'])
SurfacePoint = namedtuple('SurfacePoint', ['x', 'y', 'z'])


def rectangle_to_points(rec: Rectangle) -> typing.Tuple[Point, ...]:
    lx, rx, ly, ry = rec.lx, rec.ly, rec.rx, rec.ry
    return Point(lx, ly), Point(lx, ry), Point(rx, ly), Point(rx, ry)


def within_rectangle(rec: Rectangle, t: Point) -> bool:
    lx, rx, ly, ry = rec.lx, rec.ly, rec.rx, rec.ry
    x, y = t.x, t.y
    return lx <= x <= rx and ly <= y <= ry


def point_to_surface_point(p: Point, z: float) -> SurfacePoint:
    return SurfacePoint(p.x, p.y, z)
