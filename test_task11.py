#!/usr/bin/env python3

from unittest import TestCase
import task11


class Test_task11(TestCase):
    def setUp(self):
        """Init"""

    def test_viskos(self):
        """Test for is _prime"""
        self.assertFalse(task11.viskos(2019))
        self.assertTrue(task11.viskos(2020))
        self.assertTrue(task11.viskos(800))
    def tearDown(self):
        """Finish"""
