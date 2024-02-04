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

    @patch(
        'client.get_json',
        return_value=[{"name": "repo1"}, {"name": "repo2"}]
    )
    def test_public_repos(self, mock_get):
        """
        test_public_repos method
        """
        with patch.object(
            GithubOrgClient, '_public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            url = "https://api.github.com/orgs/test"
            mock_public_repos_url.return_value = url
            github_org_client = GithubOrgClient("test")
            repos = github_org_client.public_repos()
            self.assertEqual(repos, ["repo1", "repo2"])
            mock_get.assert_called_once()
            mock_public_repos_url.assert_called_once()
