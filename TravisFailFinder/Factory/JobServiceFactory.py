from TravisFailFinder.Service.JobService import JobService


class JobServiceFactory:

    @staticmethod
    def create():

        return JobService()
