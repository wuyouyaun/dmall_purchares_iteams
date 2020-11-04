import requests
import pymysql



# 打开数据库连接
def db_connect():
    db=pymysql.connect( host="mysql5702.test.inner-dmall.com.hk",
                        port=5702,
                        user="my_user_5702",
                        password="my_user_5702@df^",
                        db="dmall_ware"
                        )
    return db




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


def delete_db(db,sql_delete):
    cur = db.cursor()
    try:
        cur.execute(sql_delete)   # 执行
        db.commit()              # 提交
    except Exception as e:
        print("操作异常: %s" % str(e))
        # 错误回滚
        db.rollback()
    finally:                                               # rf_id,sku_id
        db.close()



if __name__=="__main__":
    '''删除新建课组'''
    delete_db(db=db_connect(), sql_delete="delete  from ware_ware where rf_id='柬埔寨商家-01';")
    delete_db(db=db_connect(), sql_delete="delete  from ware_sku where rf_id='柬埔寨商家-01';")
    delete_db(db=db_connect(), sql_delete="select * FROM ware_ext where sku_id in( select sku_id from ware_sku where rf_id = '柬埔寨商家-01')")



    select_sql(db=db_connect(), sql='select * from cat_framework_level where code="DF9d"')