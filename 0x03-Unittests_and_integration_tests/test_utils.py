#!/usr/bin/env python3
""" Unittests and integration tests """

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import access_nested_map
from utils import get_json


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
        
    
    @parameterized.expand([
        ({}, ('a',), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, result):
        """ Test access_nested_map exception """
        with self.assertRaises(result):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ TestGetJson """
    
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test get_json """
        mock = Mock()
        mock.json.return_value = test_payload
        with patch('requests.get', return_value=mock):
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """ TestMemoize """
    pass