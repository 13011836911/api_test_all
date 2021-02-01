import requests
import json

class RunMethod:
    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header).json()
        else:
            res = requests.post(url=url, data=data).json()
        return res

    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header).json()
        else:
            res = requests.get(url=url)
            if isinstance(res, str):
                res = json.dumps(res.json(), indent=2, sort_keys=True)
            else:
                res = res.content.decode("utf-8")
        return res


    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'POST':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, header)
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)