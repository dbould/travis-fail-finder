from TravisFailFinder.Factory.JobServiceFactory import JobServiceFactory
from TravisFailFinder.Service.JobService import JobService


class TestJobServiceFactory:
    def test_instance_is_created(self):
        job_service = JobServiceFactory().create()
        assert isinstance(job_service, JobService) == 1
