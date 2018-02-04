import requests
import json


class JobService:

    auth_token = ''
    base_url = ''

    def __init__(self, auth_token, base_url):
        self.auth_token = auth_token
        self.base_url = base_url

    def get_headers(self):
        return {
            'Authorization': 'token ' + self.auth_token,
            'Travis-API-Version': '3',
        }

    def get_repo_id(self, repo_slug):
        repo = self.get_request_response(self.base_url + 'repo/' + repo_slug)

        return repo['id']

    def get_branch_id(self, repo_id, branch_name):
        branches = self.get_request_response(self.base_url + 'repo/' + repo_id + '/branches')

        branch_id = 0

        for branch in branches['branches']:
            if branch['name'] == branch_name:
                branch_id = branch['last_build']['id']

        return branch_id

    def get_job_id(self, branch_id):
        jobs = self.get_request_response(self.base_url + 'build/' + branch_id + '/jobs')

        for job in jobs['jobs']:
            job_id = job['id']

        return job_id

    def get_log(self, job_id):
        log = self.get_request_response(self.base_url + 'job/' + job_id + '/log')

        return log['content']

    def get_request_response(self, url):
        response = requests.get(url, headers=self.get_headers())

        return json.loads(response.text)
