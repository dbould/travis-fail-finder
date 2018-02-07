from TravisFailFinder import ConfigService


class TestConfigService:

    def test_get_config(self):
        config_service = ConfigService()
        config = config_service.get_config()

        expected = 0

        if 'repository_login' in config:
            expected = 1

        assert expected == 1
