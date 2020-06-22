import requests
import pytest
import json
import pymssql


# 登录运营平台
@pytest.fixture(scope="class")
def login():
    headers = {
        "User-Agent": "Chrome/10",
        "flag": "guns",
        "Content-Type": "application/json"
    }
    body = {
        "username": "rhcj-gbl",
        "password": "123456",
        "addressmac": "04:0E:3C:D2:D0:B3"
    }
    data = json.dumps(body)
    response = requests.post('http://173.190.105.128:18082/login', data=data, headers=headers)
    cookie = response.cookies
    return cookie

# 建立数据库连接
@pytest.fixture(scope="class")
def db():
    db = pymssql.connect("172.190.105.193", "dbhtnews_dev", "MqfUcGymupuTmsad", "DBHTNews_DEV")
    yield db
    db.close()