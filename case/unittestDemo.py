import unittest
from base import requestTest
import json
import HTMLTestRunner
import requests
import html

class TestMethod(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.run = requestTest.RunMain()
    #     TestMethod.userId = ''
    #     print("userId:" + TestMethod.userId)

    # def setUp(self):
    #     self.run = requestTest.RunMain()

    def test_01(self):
        self.run = requestTest.RunMain()
        url = 'https://nx-v8-g1-trail.ntalker.com/platform/user/login'
        data = {
                'loginId':'songshijie',
                'password':'xiaoneng0924'
                }
        header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
        jsonData = json.dumps(data)
        res = self.run.run_main(url, 'POST', jsonData, header = header)
        resData = json.loads(res)
        globals()['userId'] = resData.get('data').get('userId')
        globals()['header'] = header
        print(res)


    def test_02(self):
        self.run = requestTest.RunMain()
        url = 'https://www.baidu.com/'
        data = {
            'username': 'songshijie',
            'password': 'xiaoneng0924'
        }
        res = requests.get(url)
        print(res)



if __name__ == '__main__':
#     unittest.main()
    filepath = '../report/htmlreport.html'
    fp = open(filepath,'w')
    suite = unittest.TestSuite()
    suite.addTest('test_01')
    suite.addTest('test_02')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='this is fpreport')
    runner.run(suite)
    # unittest.TextTestRunner(suite).run()