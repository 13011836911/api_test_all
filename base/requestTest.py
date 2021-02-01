import requests
import json

class RunMain:
    def __init__(self):
        pass

    def sendPOST(self, url, data, header, cookie):
        res = None
        if header == None and cookie == None:
            res = requests.post(url=url, data=data).json()
        elif header == None and cookie != None:
            res = requests.post(url=url, data=data, cookies=cookie).json()
        elif cookie == None and header != None:
            res = requests.post(url=url, data=data, headers=header).json()
        else:
            res = requests.post(url=url, data=data, headers=header, cookies=cookie).json()
        return json.dumps(res, indent=2, sort_keys=True)

    def sendGET(self, url, header, cookie):
        res = None
        if header == None and cookie == None:
            res = requests.get(url=url).json()
        elif header == None:
            res = requests.get(url=url, cookies=cookie).json()
        elif cookie == None:
            res = requests.get(url=url, headers=header).json()
        else:
            res = requests.post(url=url, headers=header, cookies=cookie).json()
        return json.dumps(res, indent=2, sort_keys=True)

    def run_main(self, url, method, data = None, header = None, cookie = None):
        res = None
        if method == 'GET':
            res = self.sendGET(url, header, cookie)
        elif method == 'POST':
            res = self.sendPOST(url, data, header, cookie)
        return res

if __name__ == '__main__':
    pass