# coding:utf-8

import http_common


def create():
    print(http_common.http_post("/order/pre", {"deviceId": "1", "product": {"id": "1", "num": 1}}))


if __name__ == '__main__':
    create()
