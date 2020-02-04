import pymysql
from DBUtils.PooledDB import PooledDB
import mysql.connector
from mysql.connector import errorcode
import time


config = {
  'host':'renjiemysql.mysql.database.azure.com',
  'user':'harry@renjiemysql',
  'password':'RenjieAzure@25',
  'database':'test'
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


'''
for i in range(1,9):
  locals()['conn'+str(i)] = pool.connection()
  print('connection' + str(i) + ' established')
  locals()['cursor'+str(i)] = locals()['conn'+str(i)].cursor()
  
  # Drop previous table of same name if one exists
  locals()['cursor'+str(i)].execute("DROP TABLE IF EXISTS inventory;")
  print("Finished dropping table (if existed).")
  locals()['cursor'+str(i)].execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
  print("Finished creating table.")

  # Insert some data into table
  locals()['cursor'+str(i)].execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
  print("Inserted",locals()['cursor'+str(i)].rowcount,"row(s) of data.")

  locals()['conn'+str(i)].commit()
'''


'''
# Construct connection string
try:
   conn = pool.connection()
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()


  # test conneciton time out 
  # time.sleep(10)

  # Drop previous table of same name if one exists
  cursor.execute("DROP TABLE IF EXISTS inventory;")
  print("Finished dropping table (if existed).")

  # Create table
  cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
  print("Finished creating table.")

  # Insert some data into table
  cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
  print("Inserted",cursor.rowcount,"row(s) of data.")
  cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
  print("Inserted",cursor.rowcount,"row(s) of data.")
  cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
  print("Inserted",cursor.rowcount,"row(s) of data.")

  # Cleanup
  conn.commit()
  cursor.close()
  conn.close()
  print("Done.")
'''