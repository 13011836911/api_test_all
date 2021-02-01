#coding:utf-8

class global_var:
    #case_id
    Id = '0'
    name = '1'
    url = '2'
    run = '3'
    run_way = '4'#请求方式
    header = '5'
    case_depend = '6'
    data_depend = '7'
    filed_depend = '8'
    data = '9'
    expect = '10'
    result = '11'

#获取caseId
def get_id():
    return global_var.Id

def get_url():
    return global_var.url

def get_run():
    return global_var.run

def get_run_way():
    return global_var.run_way

def get_header():
    return global_var.header

def get_case_depend():
    return global_var.case_depend

def get_data_depend():
    return global_var.data_depend

def get_field_depend():
    return global_var.filed_depend

def get_data():
    return global_var.data

def get_expect():
    return global_var.expect

def get_result():
    return global_var.result

def get_header_value():
    header = {
        'header':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'cookie':'JSESSIONID=aaa46_cDuOMzLarNAuMBx'
    }
    return header