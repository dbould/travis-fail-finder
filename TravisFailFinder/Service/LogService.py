class LogService:
    def get_error_feedback(self, log):
        failures = log.find('exited with')

        return failures
