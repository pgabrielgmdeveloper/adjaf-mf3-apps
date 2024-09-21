import requests
import django.contrib.admin

class Requests():
    def __init__(self, base) -> None:
        self._req = requests
        self._base = base

    def get(self, prefix: str ,headers = {}, params = {}):
        response = requests.get(url=f'{self._base}/{prefix}',headers=headers, params=params)
        if response.ok:
            return response.json() if response.json() else {"success": True}
        return None
    
    def post(self, prefix: str, body={}, headers = {}, params = {}):
        response = requests.post(url=f'{self._base}/{prefix}',headers=headers, params=params, json=body)
        if response.ok:
            return response.json() if response.json() else {"success": True}
        return None