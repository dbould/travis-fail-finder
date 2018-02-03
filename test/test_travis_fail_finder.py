from TravisFailFinder import JobService

class TestTravisFailFinder:

    def test_get_repo_id(self):
        job_service = JobService()
        assert job_service.get_repo_id('davework') == 16045679
