import json
import os


class ConfigService:

    def get_config(self):
        with open(os.getcwd() + '/config/setup.json', 'r') as content_file:
            config = content_file.read()

            return json.loads(config)
