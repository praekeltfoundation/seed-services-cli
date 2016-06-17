""" Tests for seed_services_cli.main. """

from unittest import TestCase

from click.testing import CliRunner

from seed_services_cli.main import cli


class TestCli(TestCase):
    def test_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue("Seed Services command line utility." in result.output)
        self.assertTrue(
            "identity-search  Find an identity"
            in result.output)
        self.assertTrue(
            "sbm-schedules    List all schedules"
            in result.output)
        self.assertTrue(
            "sbm-messagesets  List all messagesets"
            in result.output)

    def test_version(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['--version'])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue("seed-services-cli, version " in result.output)