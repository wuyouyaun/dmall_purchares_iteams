
import requests
from case.DF_project.df_testlogin import DF_Login
import pytest

@pytest.fixture(scope="session")
def df_login_xadmin(request):
    s = requests.session()
    DF_Login(s)
    return s