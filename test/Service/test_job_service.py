from TravisFailFinder import JobService


class TestTravisFailFinder:

    def test_get_repo_id(self):
        job_service = JobService.create()
        assert job_service.get_repo_id('dbould%2Ftravis-fail-finder') == 17456283

    def test_get_branch_id(self):
        job_service = JobService.create()
        assert job_service.get_branch_id('17456283', 'failing_branch') == 337061161

    def test_get_job_id(self):
        job_service = JobService().create()
        assert job_service.get_job_id('337061161') == 337061162

    def test_get_log(self):
        job_service = JobService().create()
        log = job_service.get_log('337061162')
        assert log.find('exited with 1') > 1
