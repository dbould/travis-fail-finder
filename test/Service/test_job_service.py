import sys

import os

from TravisFailFinder import JobService
import unittest
from unittest import mock


class TestTravisFailFinder:

    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            text = ''

            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code
                self.text = json_data

            def json(self):
                return self.json_data

        if args[0] == 'https://api.travis-ci.org/repo/dbould%2Ftravis-fail-finder':
            with open(os.getcwd() + '/test/Mocks/repo_response.json', 'r') as content_file:
                return MockResponse(content_file.read(), 200)
        if args[0] == 'https://api.travis-ci.org/repo/17456283/branches':
            with open(os.getcwd() + '/test/Mocks/branch_response.json', 'r') as content_file:
                return MockResponse(content_file.read(), 200)
        elif args[0] == 'http://someotherurl.com/anothertest.json':
            return MockResponse({"key2": "value2"}, 200)

        return MockResponse(None, 404)

    # We patch 'requests.get' with our own method. The mock object is passed in to our test case method.
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_repo_id(self, mock_get):
        # Assert requests.get calls
        mgc = JobService().create()
        json_data = mgc.get_repo_id('dbould%2Ftravis-fail-finder')
        assert json_data == 17456283

    if __name__ == '__main__':
        unittest.main()

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_branch_id(self, mock_get):
        job_service = JobService.create()
        assert job_service.get_branch_id('17456283', 'failing_branch') == 337061161

    def test_get_job_id(self):
        job_service = JobService().create()
        assert job_service.get_job_id('337061161') == 337061162

    def test_get_log(self):
        job_service = JobService().create()
        log = job_service.get_log('337061162')
        assert log.find('exited with 1') > 1
