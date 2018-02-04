from TravisFailFinder.Service.JobService import JobService


class JobServiceFactory:

    @staticmethod
    def create():

        auth_token = 'fZ1gERYqeLtGNd0BesVmEg'
        base_url = 'https://api.travis-ci.org/'

        return JobService(auth_token, base_url)
