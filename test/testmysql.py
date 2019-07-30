import pymysql
#!/usr/bin/python
#安装完成的mysql的位置：     C:\Program Files\MySQL\MySQL Server 8.0
# 打开数据库连接
db = pymysql.connect(host="127.0.0.1", port =3306 ,user="root", password="123456", database="test", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 定义要执行的SQL语句
sql = """ 
CREATE TABLE USER1 (
id INT auto_increment PRIMARY KEY ,
name CHAR(10) NOT NULL UNIQUE,
age TINYINT NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;
"""
# 使用execute方法执行SQL语句
# cursor.execute(sql)
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print( "Database version : %s " % data)

cursor.close()
# 关闭数据库连接
db.close()