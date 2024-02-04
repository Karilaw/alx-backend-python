#!/usr/bin/env python3
"""
test_client module
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized_class
import client
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        test_has_license method
        """
        github_org_client = GithubOrgClient("test")
        result = github_org_client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload,
     "expected_repos": expected_repos, "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    TestIntegrationGithubOrgClient Class
    """
    @classmethod
    def setUpClass(cls):
        """
        setUpClass method
        """
        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        tearDownClass method
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        test_public_repos method
        """
        self.get.return_value.json.side_effect = [
            self.org_payload, self.repos_payload,
            self.org_payload, self.repos_payload,
            self.org_payload, self.repos_payload
        ]

        github_org_client = client.GithubOrgClient("test")
        repos = github_org_client.public_repos()
        self.assertEqual(repos, self.expected_repos)
        self.get.assert_called()
