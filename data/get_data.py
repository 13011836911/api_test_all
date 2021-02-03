#coding:utf-8
from base.operation_excel import OperationExcel
from data import data_config
from base.operation_json import OperationJson

class GetData:

    def __init__(self):
        self.opera_excel = OperationExcel()

    def get_case_lines(self):
        return int(self.opera_excel.get_lines())

    def get_is_run(self, row):
        flag = None
        col = int(data_config.get_run())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    #是否携带cookie
    def is_cookie(self, row):
        col = int(data_config.get_cookie())
        cookie = self.opera_excel.get_cell_value(row, col)
        if cookie != '':
            # return data_config.get_header_value()
            return cookie
        else:
            return None

    #请求方式
    def get_request_method(self,row):
        col = int(data_config.get_run_way())
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    #获取url
    def get_url(self, row):
        col = int(data_config.get_url())
        request_url = self.opera_excel.get_cell_value(row, col)
        return request_url

    #获取请求数据
    def get_request_data(self, row):
        col = int(data_config.get_data())
        request_data = self.opera_excel.get_cell_value(row, col)
        if request_data == '':
            return None
        return request_data

    #通过关键字获取json文件中的请求数据
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    #获取预期结果
    def get_expect_data(self, row):
        col = int(data_config.get_expect())
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect

    #写入case执行结果
    def write_result(self, row, value):
        col = int(data_config.get_result())
        self.opera_excel.write_value(row, col, value)

    # 获取依赖数据的key
    def get_depend_key(self, row):
        col = int(data_config.get_data_depend())
        depend_key = self.opera_excel.get_cell_value(row, col)
        if depend_key == "":
            return None
        else:
            return depend_key

    #判断是否有case依赖
    def is_depend(self, row):
        col = int(data_config.get_case_depend())
        depend_case_id = self.opera_excel.get_cell_value(row, col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    #获取数据依赖字段
    def get_depend_field(self, row):
        col = int(data_config.get_field_depend())
        data = self.opera_excel.get_cell_value(row, col)
        if data == "":
            return None
        else:
            return data





