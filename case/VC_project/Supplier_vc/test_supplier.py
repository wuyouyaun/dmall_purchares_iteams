import requests
import pytest
import os
from case.VC_project.connect_mysql import select_sql,delete_db,db_connect
from case.VC_project.Supplier_vc.supplier_port import Save_imformation_company,Upload,update_images
from case.VC_project.Supplier_vc.readyaml import read_company_information

dirpath=os.path.dirname(os.path.realpath(__file__))
yamlpath = os.path.join(dirpath, "suppliers.yml")
data=read_company_information(yamlpath)



@pytest.fixture(scope="function")
def delete_register():
    ''' 执行删除公司信息操作  '''
    sql = "delete  from cx_company where company_name='深圳大源源3';"
    delete_db(db=db_connect(), sql_delete=sql)
    print("1111")
    print("后置操作")
    yield

def test_delete_register(vc_login_adminx, delete_register):
    s=vc_login_adminx
    add_save = Save_imformation_company(s)
    assert add_save['code'] == 0
    assert add_save['succ'] == True


# class Company_Certification():
@pytest.mark.parametrize("type,expected",
                        data
                         )
def test_company_cerifcation(vc_login_adminx, type, expected):
    '''
    资质证照上传   type 0 营业执照  1 组织机构代码 2 税务登记证 3 银行开户许可证
    :return:
    '''
    s=vc_login_adminx
    Uploads=Upload(s, type=type)
    assert Uploads['message'] == expected['message']
    assert Uploads['succ'] == expected['succ']
