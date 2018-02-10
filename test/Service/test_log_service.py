import json
import os
from TravisFailFinder import LogService


class TestLogServiceFactory:
    def test_get_error_feedback(self):
        with open(os.getcwd() + '/test/MockResponses/log_response.json', 'r') as content_file:
            log = content_file.read()
            log = json.loads(log)

        log_service = LogService()
        filtered_log = log_service.get_error_feedback(log['content'])
        assert filtered_log.find('exited with 1') == 500
