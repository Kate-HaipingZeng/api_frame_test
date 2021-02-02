import os
from excel_utils1 import ExcelUtils
from common.conf_utils import configer

current_path = os.path.dirname(__file__)
test_data_path = os.path.join(current_path, '../', configer.TEST_CASE_PATH)


class TestdataUtils():

    def __init__(self):
        self.test_data_path = test_data_path
        #   注意参数
        self.test_data = ExcelUtils(test_data_path, 'Sheet1').get_excel_value()

    def get_testdata_case_dict(self):
        test_case_dict = {}
        #   循环获取数据
        for n_row in self.test_data:
            #   dict_1.setdefault([key],value) 不同于dict_1.set([key],value)
            #   以字典的形式进行append

            test_case_dict.setdefault(n_row["测试用例编号"], []).append(n_row)
        # print(test_case_dict)
        return test_case_dict

    def get_testdata_case_list(self):
        test_case_list = []
        for k, v in self.get_testdata_case_dict().items():
            test_case_dict = {}
            test_case_dict["casename"] = k
            test_case_dict["caseinfo"] = v
            test_case_list.append(test_case_dict)
        return test_case_list


testdataUtils = TestdataUtils()
if __name__ == '__main__':

    # print(testdataUtils.get_testdata_case_list())
    # for test_case in testdataUtils.get_testdata_case_dict()['case03']:
    for test_case in testdataUtils.get_testdata_case_list():
        # print(test_case['caseinfo'][0]['请求参数'])
        print(test_case)
        # print('----------------')
        # print(test_case['caseinfo'])
    # print(testdataUtils.get_testdata_case_list())
