# coding=utf-8

import unittest

import os
from click.testing import CliRunner
from booknot.cli import cli
from booknot_tests.fixtures import clone_fixture


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_init_should_create_dot_booknote_directory(self):
        with clone_fixture('empty_directory') as directory:
            # Assign
            runner = CliRunner()

            # Acts
            os.chdir(directory)
            result = runner.invoke(cli, ['init'])

            # Assert
            self.assertTrue(os.path.isdir(os.path.join(directory, '.booknot')))
