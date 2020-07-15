# -*coding: UTF-8 -*-
"""
----------------------------------
@Author: 般若
@time：2019/8/29 9:06
@File：HandleConfig
-----------------------------------
"""
from configparser import ConfigParser
from config.constants import config_file_path

class HandleConfig:

    def __init__(self, filename):
        self.filename = filename
        self.config = ConfigParser()
        self.config.read(self.filename, encoding="utf-8")


    def get_value(self, section, option):
        return self.config.get(section, option)


    def get_int(self, section, option):
        return  self.config.getint(section, option)


    def get_boolean(self, section, option):
        return self.config.getboolean(section, option)


    def get_float(self, section, option):
        return self.config.getfloat(section, option)


if __name__ == '__main__':
    hc = HandleConfig(config_file_path)
    url = hc.get_value("url", "prefix")
    print(url)