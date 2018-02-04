import requests
import json


class JobService:

    auth_token = ''

    def __init__(self, auth_token):
        self.auth_token = auth_token

    def get_headers(self):
        return {
            'Authorization': 'token ' + self.auth_token,
            'Travis-API-Version': '3',
        }

    def get_repo_id(self, repo_slug):
        request = requests.get('https://api.travis-ci.org/repo/' + repo_slug, headers=self.get_headers())
        repo = json.loads(request.text)

        return repo['id']

    def get_branch_id(self, repo_id, branch_name):
        request = requests.get('https://api.travis-ci.org/repo/' + repo_id + '/branches', headers=self.get_headers())
        branches = json.loads(request.text)

        branch_id = 0

        for branch in branches['branches']:
            if branch['name'] == branch_name:
                branch_id = branch['last_build']['id']

        return branch_id

    def get_job_id(self, branch_id):
        request = requests.get('https://api.travis-ci.org/build/' + branch_id + '/jobs', headers=self.get_headers())
        jobs = json.loads(request.text)

        for job in jobs['jobs']:
            job_id = job['id']

        return job_id

    def get_log(self, job_id):
        request = requests.get('https://api.travis-ci.org/job/' + job_id + '/log', headers=self.get_headers())
        log = json.loads(request.text)

        return log['content']