import pymysql
from DBUtils.PooledDB import PooledDB
import mysql.connector
from mysql.connector import errorcode
import time


config = {
  'host':<your host>,
  'user':<your username>,
  'password':<your password>',
  'database':<your database>
}

pool = PooledDB(pymysql,maxconnections=9, blocking=True, mincached=5, **config)


for i in range(1,10):
  locals()['conn'+str(i)] = pool.connection()
  print('connection' + str(i) + ' established')
  locals()['cursor'+str(i)] = locals()['conn'+str(i)].cursor()
  
  
  # Insert some data into table
  locals()['cursor'+str(i)].execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
  print("Inserted",locals()['cursor'+str(i)].rowcount,"row(s) of data.")
  locals()['conn'+str(i)].commit()






time.sleep(60)
cursor1.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
print("connection1 Inserted",cursor1.rowcount,"row(s) of data.")
conn1.commit()

