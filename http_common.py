# coding:utf-8

import http.client
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

headers = {"Content-type": "application/json; charset=utf-8"}


def url_common(method, path, body):
    conn = http.client.HTTPConnection("localhost:8698")
    conn.request(method, '/api'+path, json.dumps(body), headers)
    response = conn.getresponse()

    return response.read()


def http_post(path, body):
    return url_common("POST", path, body)



