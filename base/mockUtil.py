import mock
from base.requestTest import RunMain
import requests
import json

if __name__ == "__main__":
    url = 'http://192.168.90.198:81/platform/user/login'
    # list = {
    # "code":200,
    # "message":"success",
    # "data":{
    #     "total":6,
    #     "list":[
    #         {
    #             "id":"null",
    #             "gridId":"adece6c9bf4a44f6878ac4ac033b31bb",
    #             "gridName":"新零售性能测试环境grid(ucloud)",
    #             "province":"北京",
    #             "city":"北京",
    #             "district":"朝阳",
    #             "agentUrl":"http://ucloud-jd1000.ntalker.com/usercenter",
    #             "ratio":1,
    #             "domainName":"null"
    #         },
    #     ],
    #     "pageNum": 1,
    #     "pageSize": 10,
    #     "size": 6,
    #     "startRow": 1,
    #     "endRow": 6,
    #     "pages": 1,
    #     "prePage": 0,
    #     "nextPage": 0,
    #     "isFirstPage": "true",
    #     "isLastPage": "true",
    #     "hasPreviousPage": "false",
    #     "hasNextPage": "false",
    #     "navigatePages": 10,
    #     "navigatepageNums": [],
    #     "navigateFirstPage": 1,
    #     "navigateLastPage": 1,
    #     "firstPage": 1,
    #     "lastPage": 1
    # }
    # }

    data = {
            'loginId':'songshijie',
            'password':'xiaoneng0924'
            }
    jsonDta = json.dumps(data)
    res = requests.post(url = url, data = jsonDta).json()
    # run = RunMain(url, 'POST', data)
    # mockData = mock.Mock(return_value=data)
    # run.run_main = mockData
    # res = run.run_main(url, 'POST', data)
    print(res)
    pass