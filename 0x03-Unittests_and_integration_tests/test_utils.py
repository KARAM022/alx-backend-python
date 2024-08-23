#!/usr/bin/env python3
""" Unittests and integration tests """

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized

from .utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap """

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """ Test access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), result)