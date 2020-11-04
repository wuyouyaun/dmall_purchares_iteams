# import requests
# import pytest
#
# from case.VC_project.connect_mysql import delete_db,db_connect
#
#
#
#
#
#
# @pytest.fixture(scope="session")
# def delete_register():
#     ''' 执行删除公司信息操作  '''
#     sql = "delete  from cx_company where company_name='深圳大源源3';"
#     delete_db(db=db_connect(), sql_delete=sql)
#     print("后置操作")
