#!/usr/bin/env python

import unittest

import geothermpy.bind as bind
from geothermpy import Point
from geothermpy.load_data import load_geothermal_gradient
from geothermpy.out import TraceWriter


class OutTester(unittest.TestCase):
    def setUp(self):
        self.data = load_geothermal_gradient('data/example.csv')
        self.trace = bind.generate_trace(self.data, Point(24, 1876.80005), h=0.01, n=1000)
        self.trace_writer = TraceWriter(self.trace)

    def test_to_csv(self):
        self.trace_writer.to_csv(path_or_buf='data/trace2cols.csv', include_derivative=False, index=False)
        self.trace_writer.to_csv(path_or_buf='data/trace3cols.csv', include_derivative=True, index=False)


if __name__ == "__main__":
    unittest.main()
