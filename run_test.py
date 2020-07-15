# -*coding: UTF-8 -*-
"""
----------------------------------
@Author: 般若
@time：2019/8/29 9:23
@File：run_test
-----------------------------------
"""
import unittest
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from config.constants import report_name,reports_path,now
from common import SendEmail


if __name__ == '__main__':
    with open(report_name, "wb") as file:
        suite = unittest.defaultTestLoader.discover("cases",pattern="*Cases.py")

        runner = HTMLTestRunner(stream=file,
                                title="豆瓣音乐api自动化测试报告",
                                verbosity=2,
                                description="详细结果如下：",
                                tester="huym")

        runner.run(suite)

    sleep(5)
    # 查找最新生成的报告
    new_report = SendEmail.new_report(reports_path)
    # 发送邮件
    SendEmail.send_mail(new_report, report_name, now)
