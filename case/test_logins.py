from common.httprunner_log import login
import requests
import pytest
import time
def test_login():

    s=requests.session()
    kk=login(s)
    # print("4434343")
    # print(kk)
    assert "首页" in kk

