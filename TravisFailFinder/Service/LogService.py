class LogService:
    def get_error_feedback(self, log):
        failures = log.find('exited with')
        start = failures - 500
        end = failures + 500

        return log[start:end]
