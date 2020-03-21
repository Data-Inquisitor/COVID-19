#!/usr/bin/env python

"""Tests for `covid_19` package."""


import unittest
from click.testing import CliRunner

from covid_19 import covid_19
from covid_19 import cli


class TestCovid_19(unittest.TestCase):
    """Tests for `covid_19` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'covid_19.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
