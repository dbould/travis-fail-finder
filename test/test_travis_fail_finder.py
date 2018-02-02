from TravisFailFinder import JobService


class TestTravisFailFinder:

    def test_hello_world(self):
        fail_finder = JobService()
        assert fail_finder.test() == "Hello World!"
