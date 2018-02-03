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
