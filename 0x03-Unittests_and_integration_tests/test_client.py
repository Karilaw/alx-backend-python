#!/usr/bin/env python3
"""
test_client module
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
import client


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient Class
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock_get):
        """
        test_org method
        """
        github_org_client = client.GithubOrgClient(org_name)
        self.assertEqual(github_org_client.org, {"payload": True})
        mock_get.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        test_public_repos_url method
        """
        payload = {"repos_url": "World"}
        mock_org.return_value = payload

        github_org_client = GithubOrgClient("test")
        expected = payload["repos_url"]
        self.assertEqual(github_org_client._public_repos_url, expected)
