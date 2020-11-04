# from ke16.form_data_xadmin import add_teacher_name
# from ke12.connet_mysql import select_sql,execute_sql
# import pytest
#
#
# # 前置操作：先清空数据
# @pytest.fixture(scope="function")
# def delete_teacher():
#     sql = "DELETE FROM djangoweb.hello_teacher WHERE teacher_name = 'yoyo333';"
#     execute_sql(sql)
#     yield
#     print("数据清理的操作")
#
#
#
# def test_add_teacher(login_xmain, delete_teacher):
#     # 新增数据
#     s =login_xmain
#     text = add_teacher_name(s)
#     # 查询数据库结果
#     sql = "SELECT count(*) as sum from djangoweb.hello_teacher WHERE teacher_name = 'yoyo333'"
#     result1 = select_sql(sql)[0]["sum"]
#     # 校验结果
#     assert result1 == 1