# -*- coding: utf-8 -*-
"""Tests for the `template` module."""

from .base import BaseTestCase

from statikos.template import create_template
from statikos.utils import read_json_file


class TemplateTestCase(BaseTestCase):
    def setUp(self):
        super(TemplateTestCase, self).setUp()

    def test_create_template(self):
        parameters = {'stack_name': 'stack-name', 'domain_name': 'domain-name'}
        expected = read_json_file('tests/resources/test_cloudformation.json')
        actual = create_template(parameters=parameters)
        self.assertDictEqual(expected, actual.to_dict())
