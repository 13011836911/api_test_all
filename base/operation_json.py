#coding:utf-8
import json

class OperationJson:

    def __init__(self):
        self.data = self.read_file('../json_config/login.json')

    #读取json文件
    def read_file(self, file_path=None):
        if file_path:
            with open(file_path) as fp:
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


if __name__ == "__main__":
    opera = OperationJson()
