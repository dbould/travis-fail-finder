import requests
import json


class JobService:

    def get_repo_id(self, repo_slug):

        headers = {
            'Authorization': 'token fZ1gERYqeLtGNd0BesVmEg',
            'Travis-API-Version': '3',
        }

        request = requests.get('https://api.travis-ci.org/repo/' + repo_slug, headers=headers)
        repo = json.loads(request.text)

        return repo['id']

    def get_branch_id(self, repo_id, branch_name):

        headers = {
            'Authorization': 'token fZ1gERYqeLtGNd0BesVmEg',
            'Travis-API-Version': '3',
        }

        request = requests.get('https://api.travis-ci.org/repo/' + repo_id + '/branches', headers=headers)
        branches = json.loads(request.text)

        branch_id = 0

        for branch in branches['branches']:
            if branch['name'] == branch_name:
                branch_id = branch['last_build']['id']

        return branch_id
