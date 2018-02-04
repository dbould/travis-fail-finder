from TravisFailFinder import ConfigService


class TestConfigService:

    def test_get_config(self):
        config_service = ConfigService()
        config = config_service.get_config()
        assert config['repository_login'] == 'dbould'
