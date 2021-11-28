# -*- coding: UTF-8 -*-
import requests

url = "http://111.200.241.244:49294"
headers = {
    "Referer": "123.123.123.123",
    "Origin": "https://www.Sycsecret.com",
    "User-Agent": "Syclover",
    "X-Forwarded-For": "123.123.123.123"
}
r = requests.get(url=url, headers=headers)
r.encoding='utf-8'
print(r.text)
