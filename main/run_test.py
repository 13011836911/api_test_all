from base.run_method import RunMethod
from data.get_data import GetData
import json
import sys
from base.common_util import CommonUtil
import requests
from base.sendEmail import SendEmail
from json_config.depend_data import DependDentData
from base.operation_json import OperationJson
from base.operation_header import OperationHeader
from base.logger import logger

sys.path.append("D:\projectPython\DjangoProject")
class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.common = CommonUtil()
        self.mail = SendEmail()
        self.opera_json = OperationJson('../json_config/cookie.json')

    def go_on_run(self):
        logger.info("*************** 开始执行用例 ***************")
        res = None
        pass_count = []
        fail_count = []
        request_data = {}
        rows_count = self.data.get_case_lines()
        try:
            for i in range(1, rows_count):
                is_run = self.data.get_is_run(i)
                if is_run:
                    url = self.data.get_url(i)
                    method = self.data.get_request_method(i)
                    data = json.dumps(self.data.get_data_for_json(i))
                    expect = self.data.get_expect_data(i)
                    header = self.data.is_cookie(i)
                    depend_case = self.data.is_depend(i)
                    if depend_case != None:
                        self.depend_data = DependDentData(depend_case)
                        # 相应数据
                        depend_response_data = self.depend_data.get_data_for_key(i)
                        # 获取依赖的key
                        depend_key = self.data.get_depend_field(i)
                        request_data[depend_key] = depend_response_data
                    if header == 'write':
                        res = self.run_method.run_main(method, url, data)
                        opera_header = OperationHeader()
                        opera_header.write_cookie()
                    if header != 'write':
                        cookie = self.opera_json.get_data('JSESSIONID')
                        cookies = {
                            "JSESSIONID": cookie
                        }
                        cookies = json.dumps(cookies)
                        res = self.run_method.run_main(method=method, url=url, data=data, cookies=cookies)
                    if self.common.is_contain(expect, res):
                        self.data.write_result(i, 'pass')
                        pass_count.append(i)
                    else:
                        self.data.write_result(i, 'fail')
                        fail_count.append(i)
            self.mail.send_main(pass_count, fail_count)
        except requests.exceptions.ConnectionError:
            print('连接错误')
        logger.info("*************** 结束执行用例 ***************")
        return res


if __name__ == "__main__":
    run = RunTest()
    run.go_on_run()