from TravisFailFinder import JobService

class TestTravisFailFinder:

    def test_get_repo_id(self):
        job_service = JobService()
        assert job_service.get_repo_id('dbould%2Ftravis-fail-finder') == 17456283
