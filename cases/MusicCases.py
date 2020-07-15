# -*coding: UTF-8 -*-
"""
----------------------------------
@Author: 般若
@time：2019/8/29 18:05
@File：MusicCases
-----------------------------------
"""
import unittest
import json
from libs.ddt import ddt, data
from common.HttpRequest import HttpRequest
from common.ReadExcel import ReadExcel
from common.logger import Logger
from common.HandleConfig import HandleConfig
from config.constants import config_file_path, cases_file_path

hc = HandleConfig(config_file_path)
prefix = hc.get_value("url", "prefix")
result_col = hc.get_value("case_file", "result_col")
actual_col = hc.get_value("case_file", "actual_col")

re = ReadExcel(cases_file_path)
cases = re.getExcelCases()
# print(cases)

logger = Logger(logger="MusicCases").getLog()


@ddt
class MusicCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("开始测试")
        cls.hr = HttpRequest()

    @classmethod
    def tearDownClass(cls):
        logger.info("测试完成")

    @data(*cases)
    def test_music(self, case):
        """豆瓣音乐api测试"""
        url = prefix + case["url"]
        datas = case["datas"]
        req = self.hr.http_request(url,"post",datas)
        result = req.text

        try:
            self.assertIn(case["except"], result)
            logger.info("用例{case['title']}测试结果为：Pass")
            re.write_result(case["case_id"]+1, req.status_code, "Pass")
        except AssertionError as e:
            logger.info("用例{case['title']}测试结果为：Fail")
            re.write_result(case["case_id"]+1, req.status_code, "Fail")
            raise e


if __name__ == '__main__':
    unittest.main()