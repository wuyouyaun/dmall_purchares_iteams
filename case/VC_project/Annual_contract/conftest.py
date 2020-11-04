# coding:utf-8
import requests
import pytest
from case.VC_project.VCtest_login import VC_Login

import requests

# fixture 是 pytest内置函数

@pytest.fixture(scope= "session")
def login_xadmin(request):
    s = requests.session()
    VC_Login(s)
    c = VC_Login(s)
    print(c)
    return s

