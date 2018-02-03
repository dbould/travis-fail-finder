from TravisFailFinder import JobService


class TestTravisFailFinder:

    def test_get_repo_id(self):
        job_service = JobService()
        assert job_service.get_repo_id('dbould%2Ftravis-fail-finder') == 17456283

    def test_get_branch_id(self):
        job_service = JobService()
        assert job_service.get_branch_id("17456283", 'master') == 336890330
