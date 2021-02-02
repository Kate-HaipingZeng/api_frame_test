import os
import requests
import ast

from common.conf_utils import configer
from common.testdata_utils1 import testdataUtils


class RequestModel:
    def __init__(self):
        self.host = configer.HOST
        self.header = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        self.session = requests.session()

    def get_request(self, url, requests_info):
        response = self.session.get(url=url,
                                    params=requests_info)
        print(response.text)

    def post_reqeust(self, url, params, data):
        response = self.session.post(url=url,
                                     # header=self.header,
                                     data=requests_info
                                     )
        print(response.text)


requestModel = RequestModel()

if __name__ == '__main__':
    for test_case in testdataUtils.get_testdata_case_list():
        # print(test_case['caseinfo'][0]['请求参数'])
        method = test_case['caseinfo'][0]['请求方式']
        url = test_case['caseinfo'][0]['请求地址']
        requests_info = ast.literal_eval(test_case['caseinfo'][0]['请求参数'])
        print(requests_info)
        if method == 'get':
            requestModel.get_request(url, requests_info)
        if method == 'post':
            requestModel.post_reqeust(url, requests_info)

    # requests_info = {'请求参数': {'grant_type': 'client_credential', 'appid': 'wxdca5302e20354254',
    #                           'secret': '7ebfc88c2158f8af45c37189f1485314'}}
