import pymysql
sql='/*--user=root;--password=123456;--host=127.0.0.1;--execute=1;--port=4901;*/\
inception_magic_start;\
use mysql;\
CREATE TABLE adaptive_office(id int);\
inception_magic_commit;'
try:
    conn=pymysql.connect(host='127.0.0.1',user='',passwd='',db='',port=6669)
    cur=conn.cursor()
    ret=cur.execute(sql)
    result=cur.fetchall()
    num_fields = len(cur.description)
    field_names = [i[0] for i in cur.description]
    print(field_names)
    for row in result:
        print(row[0], "|",row[1],"|",row[2],"|",row[3],"|",row[4],"|",
        row[5],"|",row[6],"|",row[7],"|",row[8],"|",row[9],"|",row[10])
    cur.close()
    conn.close()
except Exception as e:
     print("Mysql Error %d: %s" % (e.args[0], e.args[1]))