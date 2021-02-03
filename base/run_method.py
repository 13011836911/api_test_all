import requests
import json

class RunMethod:
    def post_main(self, url, data, cookies=None):
        res = None
        if cookies != None:
            res = requests.post(url=url, data=data, cookies=cookies).json()
        else:
            res = requests.post(url=url, data=data).json()
        return res

    def get_main(self, url, cookies=None):
        res = None
        if cookies != None:
            res = requests.get(url=url, cookies=json.loads(cookies)).json()
        else:
            res = requests.get(url=url)
            if isinstance(res, str):
                res = json.dumps(res.json(), indent=2, sort_keys=True)
            else:
                res = res.content.decode("utf-8")
        return res


    def run_main(self, method, url, data=None, cookies=None):
        res = None
        if method == 'POST':
            res = self.post_main(url, data, cookies)
        else:
            res = self.get_main(url, cookies)
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)