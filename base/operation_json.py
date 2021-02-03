#coding:utf-8
import json

class OperationJson:

    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = '../json_config/login.json'
        else:
            self.file_path = file_path
        self.data = self.read_file()

    #读取json文件
    def read_file(self):
        if self.file_path:
            with open(self.file_path) as fp:
                data = json.load(fp)
        else:
            with open('../json_config/login.json') as fp:
                data = json.load(fp)
        return data

    #根据关键字读取json
    def get_data(self, id):
        if id != None:
            return self.data[id]
        else:
            return None

    def write_data(self, data):
        with open('../json_config/cookie.json', 'w') as fp:
            fp.write(data)

if __name__ == "__main__":
    opera = OperationJson()
