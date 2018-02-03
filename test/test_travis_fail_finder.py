from TravisFailFinder import JobService

class TestTravisFailFinder:

    def test_get_repo_id(self):
        job_service = JobService()
        assert job_service.get_repo_id('travis-fail-finder') == 17456283
