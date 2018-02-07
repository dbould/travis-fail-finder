from TravisFailFinder import ConfigService


class TestConfigService:

    def test_get_config_repo(self):
        config_service = ConfigService()
        config = config_service.get_config()

        expected = 0

        if 'repository' in config:
            expected = 1

        assert expected == 1

    def test_get_config_login(self):
        config_service = ConfigService()
        config = config_service.get_config()

        expected = 0

        if 'repository_login' in config:
            expected = 1

        assert expected == 1

    def test_get_config_token(self):
        config_service = ConfigService()
        config = config_service.get_config()

        expected = 0

        if 'auth_token' in config:
            expected = 1

        assert expected == 1

    def test_get_config_url(self):
        config_service = ConfigService()
        config = config_service.get_config()

        expected = 0

        if 'base_url' in config:
            expected = 1

        assert expected == 1
