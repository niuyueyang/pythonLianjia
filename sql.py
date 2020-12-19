# 查询数据
import pymysql

db_conn = pymysql.connect(db='数据库名',host='网站ip',user='用户名',password='密码')

db_cursor = db_conn.cursor()
try:
    sql = 'select * from food where name like \'%香蕉%\''
    result = db_cursor.execute(sql)
    data = db_cursor.fetchall()
    db_conn.commit()
    print(data)
except:
    db_conn.rollback()

db_conn.close()


# 插入数据
# import pymysql
#
# db_conn = pymysql.connect(db='数据库名',host='网站ip',user='用户名',password='密码')
#
# db_cursor = db_conn.cursor()
# try:
#     sql = 'insert into test(name) values (%s)'
#     data = [
#         ('july'),
#         ('june'),
#         ('marin')
#     ]
#     result = db_cursor.executemany(sql, data)
#     # data = db_cursor.fetchall()
#     db_conn.commit()
#
#     # 获取最新的那一条数据的ID
#     # last_id = db_cursor.lastrowid
#     print("最后一条数据的ID是:", result)
# except:
#     db_conn.rollback()
#
# db_conn.close()

# 删除
# import pymysql
# db_conn = pymysql.connect(db='数据库名',host='网站ip',user='用户名',password='密码')
# db_cursor = db_conn.cursor()
# try:
#     sql = "delete from test where name=%s;"
#     name = "june"
#     # 拼接并执行SQL语句
#     result = db_cursor.execute(sql, [name])
#     # data = db_cursor.fetchall()
#     db_conn.commit()
#
#     # 获取最新的那一条数据的ID
#     # last_id = db_cursor.lastrowid
#     print("删除的数据量:", result)
# except:
#     db_conn.rollback()
# db_conn.close()

# 更新
# import pymysql
# db_conn = pymysql.connect(db='数据库名',host='网站ip',user='用户名',password='密码')
# db_cursor = db_conn.cursor()
# try:
#     sql = "update test set name=%s where id=%s;;"
#     name = "june"
#     # 拼接并执行SQL语句
#     result = db_cursor.execute(sql, [name, 3])
#     # data = db_cursor.fetchall()
#     db_conn.commit()
#
#     # 获取最新的那一条数据的ID
#     # last_id = db_cursor.lastrowid
#     print("更新的数据量:", result)
# except:
#     db_conn.rollback()
# db_conn.close()
