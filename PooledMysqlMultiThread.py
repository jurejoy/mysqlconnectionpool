import pymysql
from DBUtils.PooledDB import PooledDB
import mysql.connector
from mysql.connector import errorcode
import time
import threading
from threading import RLock


def task(arg):
    locals()['conn'+str(arg)] = pool.connection()
    print('connection' + str(arg) + ' established')
    locals()['cursor'+str(arg)] = locals()['conn'+str(arg)].cursor()
    locals()['cursor'+str(arg)].execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
    locals()['conn'+str(arg)].commit()
    result = locals()['cursor'+str(arg)].fetchall()
    locals()['cursor'+str(arg)].close()
    print(result)


config = {
  'host':<your host>,
  'user':<your username>,
  'password':<your password>',
  'database':<your database>
}

def task(arg):
    locals()['conn'+str(arg)] = pool.connection()
    print('connection' + str(arg) + ' established')
    locals()['cursor'+str(arg)] = locals()['conn'+str(arg)].cursor()
    locals()['cursor'+str(arg)].execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
    locals()['conn'+str(arg)].commit()
    result = locals()['cursor'+str(arg)].fetchall()
    locals()['cursor'+str(arg)].close()
    print(result)

pool = PooledDB(pymysql,maxconnections=10, blocking=True, mincached=5, **config)

for i in range(1,20):
    t = threading.Thread(target=task, args=(i,))
    t.start()

