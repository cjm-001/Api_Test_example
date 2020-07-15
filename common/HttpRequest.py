# -*coding: UTF-8 -*-
"""
----------------------------------
@Author: 般若
@time：2019/8/22 18:26
@File：HttpRequest
-----------------------------------
"""
import requests
import json

class HttpRequest:
    def __init__(self):
        # 创建会话，自动管理cookie
        self.session = requests.Session()

    def http_request(self, url, method="post", datas=None, headers=None):
        method = method.lower()
        # 请求参数格式化
        if isinstance(datas,dict):
            datas = datas
        else:
            datas = json.loads(datas)

        # 区别请求方式
        if method == "post":
            res = requests.post(url=url, data=datas, headers=headers)
        elif method == "get":
            res = requests.get(url=url, params=datas, headers=headers)
        else:
            res = None
            print("暂不支持其他请求方式")

        return res


    def session_close(self):
        """释放会话"""
        self.session.close()


if __name__ == '__main__':
    hr = HttpRequest()
    url = "https://api.douban.com/v2/music/search"
    datas = {"q":"邓紫棋","count":1}
    print(type(datas))

    res = hr.http_request(url, "post", datas)

    print(res.text)
    print(res.status_code)
    print(res.cookies)