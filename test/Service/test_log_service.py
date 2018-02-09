import json
import os
from TravisFailFinder import LogService


class TestLogService:
    def test_get_error_feedback(self):
        with open(os.getcwd() + '/test/MockResponses/log_response.json', 'r') as content_file:
            log = content_file.read()
            log = json.loads(log)

        log_service = LogService()
        assert log_service.get_error_feedback(log['content']) == 50775
