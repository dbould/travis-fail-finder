from TravisFailFinder.Service.ConfigService import ConfigService
from TravisFailFinder.Service.JobService import JobService


class JobServiceFactory:

    @staticmethod
    def create():
        config_service = ConfigService()
        config = config_service.get_config()

        auth_token = config['auth_token']
        base_url = config['base_url']

        return JobService(auth_token, base_url)
