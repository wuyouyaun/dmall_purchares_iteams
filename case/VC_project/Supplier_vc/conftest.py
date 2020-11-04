import requests
import pytest
from case.VC_project.VCtest_login import VC_Login


@pytest.fixture(scope="session")
def vc_login_adminx():
    s=requests.session()
    VC_Login(s)
    yield s






