# -*coding: UTF-8 -*-
"""
----------------------------------
@Author: 般若
@time：2019/8/22 13:42
@File：logger
-----------------------------------
"""
import logging
from config.constants import log_name

class Logger:

    def __init__(self, logger):
        # 定义日志收集器
        self.logger = logging.getLogger(logger)

        # 指定日志收集器级别
        self.logger.setLevel(logging.INFO)

        # 定义日志输出渠道
        ch = logging.StreamHandler()    # 输出到控制台
        fh = logging.FileHandler(log_name)  # 输出到文件

        # 定义输出日志等级
        ch.setLevel(logging.INFO)
        fh.setLevel(logging.INFO)

        # 指定日志输出内容格式
        formatter = "%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s"
        cf = logging.Formatter(formatter)
        ff = logging.Formatter(formatter)

        ch.setFormatter(cf)
        fh.setFormatter(ff)

        # 日志器和渠道对接
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)


    def getLog(self):
        return self.logger

if __name__ == '__main__':
    log = Logger("haha").getLog()
    log.debug("debug~~~")
    log.info("info~~~")
    log.error("error~~~")
    log.critical("critical~~~")
    log.warning("warning~~~")



