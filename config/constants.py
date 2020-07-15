# -*coding: UTF-8 -*-
"""
----------------------------------
@Author: 般若
@time：2019/8/22 8:53
@File：constants
-----------------------------------
"""

import os
import time

# 格式化当前时间
now = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))

# 项目路径
base_path = os.path.dirname(os.path.dirname(__file__))

# 配置文件目录路径
config_path = os.path.join(base_path, "config")
config_file_path = os.path.join(config_path, "config.conf")

# 测试报告目录路径
reports_path = os.path.join(base_path, "reports")
report_name = reports_path + "\\" + now + "_report.html"

# 日志文件路径
logs_path = os.path.join(base_path, "logs")
# 日志文件名
log_name = logs_path + "\\"+ now + ".log"

# 测试用例目录路径
cases_path = os.path.join(base_path, "cases")

# 数据目录路径
datas_path = os.path.join(base_path, "datas")
cases_file_path = os.path.join(datas_path, "cases.xlsx")

