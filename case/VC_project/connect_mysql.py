import pytest
import requests
import pymysql



# 打开数据库连接
def db_connect():
    db=pymysql.connect( host="10.40.2.23",
                        port=5707,
                        user="my_user_5707",
                        password="my_user_5707@df&",
                        db="df_vc_basemanage_supplier"
                        )
    return db

# 使用cursor()方法创建一个游标对象cur
# cur=db.cursor()
#
# #使用execute()方法执行sql查询
# cur.execute('select * from cx_company where company_name="深圳大源源呗1"')
# data=cur.fetchall()
# print(data)

def select_sql(db,sql):
    '''
    查询
    :param sql:
    :return:
    '''
    cur=db.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    print(data)



# select_sql(db=db_connect(),sql='select * from cx_company where company_name="深圳大源源呗1"')

def delete_db(db,sql_delete):
    cur = db.cursor()
    try:
        cur.execute(sql_delete)   # 执行
        db.commit()              # 提交
    except Exception as e:
        print("操作异常: %s" % str(e))
        # 错误回滚
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    delete_db(db=db_connect(), sql_delete="delete  from cx_company where company_name='深圳大源源呐';")
    select_sql(db=db_connect(), sql='select * from cx_company where company_name="深圳大源源呐"')