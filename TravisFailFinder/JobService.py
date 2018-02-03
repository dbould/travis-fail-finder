import requests
import json


class JobService:

    def get_repo_id(self, repo_name):
        repo_id = 0

        headers = {
            'Authorization': 'token fZ1gERYqeLtGNd0BesVmEg',
            'Travis-API-Version': '3',
        }

        request = requests.get('https://api.travis-ci.org/repos', headers=headers)
        repos = json.loads(request.text)

        for repo in repos['repositories']:
            if repo['name'] == repo_name:
                repo_id = repo['id']
                break

        return repo_id
