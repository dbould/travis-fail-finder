import os

from TravisFailFinder import JobService
import unittest
from unittest import mock
from test.MockApiResponse import MockApiResponse


class TestTravisFailFinder:

    def mocked_requests_get(*args, **kwargs):
        if args[0] == 'https://api.travis-ci.org/repo/dbould%2Ftravis-fail-finder':
            with open(os.getcwd() + '/test/MockResponses/repo_response.json', 'r') as content_file:
                return MockApiResponse(content_file.read(), 200)
        if args[0] == 'https://api.travis-ci.org/repo/17456283/branches':
            with open(os.getcwd() + '/test/MockResponses/branch_response.json', 'r') as content_file:
                return MockApiResponse(content_file.read(), 200)
        if args[0] == 'https://api.travis-ci.org/build/337061161/jobs':
            with open(os.getcwd() + '/test/MockResponses/jobs_response.json', 'r') as content_file:
                return MockApiResponse(content_file.read(), 200)
        if args[0] == 'https://api.travis-ci.org/job/337061162/log':
            with open(os.getcwd() + '/test/MockResponses/log_response.json', 'r') as content_file:
                return MockApiResponse(content_file.read(), 200)

        return MockApiResponse(None, 404)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_repo_id(self, mock_get):
        mgc = JobService().create()
        json_data = mgc.get_repo_id('dbould%2Ftravis-fail-finder')
        assert json_data == 17456283

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_branch_id(self, mock_get):
        job_service = JobService.create()
        assert job_service.get_branch_id('17456283', 'failing_branch') == 337061161

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_job_id(self, mock_get):
        job_service = JobService().create()
        assert job_service.get_job_id('337061161') == 337061162

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_log(self, mock_get):
        job_service = JobService().create()
        log = job_service.get_log('337061162')
        assert log.find('exited with 1') > 1
