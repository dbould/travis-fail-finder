from TravisFailFinder.Service.JobService import JobService


class JobServiceFactory:

    @staticmethod
    def create():
        auth_token = 'fZ1gERYqeLtGNd0BesVmEg'

        return JobService(auth_token)
