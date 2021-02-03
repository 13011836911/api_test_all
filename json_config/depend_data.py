
from base.operation_excel import OperationExcel
from base.run_method import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse

class DependDentData:
    def __init__(self, case_id):
        self.opera_excel = OperationExcel()
        self.case_id = case_id
        self.data = GetData()

    def get_case_lines_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    def run_dependdent(self):
        run_method = RunMethod()
        row = int(self.opera_excel.get_rows_num(self.case_id))
        request_data = self.data.get_data_for_json(row)
        cookie = self.data.is_cookie(row)
        method = self.data.get_request_method(row)
        url = self.data.get_url(row)
        res = run_method.run_main(method, url, request_data, cookie)
        return res

    #根据依赖的key去获取执行依赖测试case的响应，然后返回
    def get_data_for_key(self, row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependdent()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]
