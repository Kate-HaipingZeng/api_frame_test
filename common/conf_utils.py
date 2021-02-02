import os
import configparser

# from common.config_utils import ConfigUtils


config_path = os.path.join(os.path.dirname(__file__), '..', 'conf/conf.ini')


class Configer():
    def __init__(self):
        self.configpareser = configparser.ConfigParser()
        self.configpareser.read(config_path)

    @property
    def TEST_CASE_PATH(self):
        test_case_path = self.configpareser.get('path', 'TEST_CASE_PATH')
        return test_case_path

    @property
    def TEST_CASE_PATH1(self):
        test_case_path = self.configpareser.get('path', 'TEST_CASE_PATH1')
        return test_case_path

    # @property
    # def WRITE_PATH(self):
    #     write_path = self.configpareser.get('path', 'WRITE_PATH')
    #     return write_path
    #
    # @property
    # def LOG_PATH(self):
    #     log_path = self.configpareser.get('path', 'LOG_PATH')
    #     return log_path
    #
    # @property
    # def CURL_PATH(self):
    #     curl_path = self.configpareser.get('path', 'CURL_PATH')
    #     return curl_path

    @property
    def HOST(self):
        host = self.configpareser.get('path', 'HOST')
        return host


configer = Configer()