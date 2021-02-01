#coding:utf-8

import xlrd
import xlwt
from xlutils.copy import copy


class OperationExcel:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
            self.data = self.get_data()
        else:
            self.file_name = '../json_config/case_data.xls'
            self.sheet_id = 0
        self.data = self.get_data()

    #获取sheet内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    #获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    #获取某个单元格内容
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    #写入数据
    def write_value(self, rows, cols, value):
        read = xlrd.open_workbook(self.file_name)
        write_data = copy(read)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(rows, cols, value)
        write_data.save(self.file_name)

    #根据caseid找到对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_rows_num(case_id)
        rows_data = self.get_rows_values(row_num)
        return rows_data

    def get_rows_num(self, case_id):
        num = 0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num = num + 1


    #根据行号找整行行内容
    def get_rows_values(self, rows):
        table = self.data
        row_data = table.row_values(rows)
        return row_data

    #获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id !=None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.cell_values(0)
        return cols



if __name__ == "__main__":
    opers = OperationExcel()