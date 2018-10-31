import mysql.connector
# attention please: if you want to import this module ,please run this install command line : pip install mysql-connector

#define a mysql operation tool class
class MysqlTools(object):

   def __init__(self,db_user_name,db_password,db_name,db_host,db_port):
       self.db_user_name = db_user_name
       self.db_password = db_password
       self.db_name = db_name
       self.db_host = db_host
       self.db_port = db_port

   def connect_db(self):
       self.conn = mysql.connector.connect(
           user=self.db_user_name,
           password=self.db_password,
           database=self.db_name,
           host = self.db_host,
           port = self.db_port)

   def close_db(self):
       if self.conn:
           self.conn.close()

   def create_table(self,create_sql):
       if self.conn:
          cursor = self.conn.cursor()
          cursor.execute(create_sql)
          print('create success! ')
          self.conn.commit()
          cursor.close()
       else:
           print('fail to create table . the connection does not exists! ')

   def insert_table(self,insert_sql,insert_params):
       if self.conn:
          cursor = self.conn.cursor()
          cursor.execute(insert_sql,insert_params)
          print('insert result count: ',cursor.rowcount)
          self.conn.commit()
          cursor.close()
       else:
           print('fail to insert table . the connection does not exists! ')

   def batch_insert_table(self, insert_sql, insert_params):
       if self.conn:
          cursor = self.conn.cursor()
          cursor.executemany(insert_sql,insert_params)
          print('batch insert result count: ',cursor.rowcount)
          self.conn.commit()
          cursor.close()
       else:
           print('fail to insert table . the connection does not exists! ')

   def query_table(self,query_sql,query_params):
       if self.conn:
          cursor = self.conn.cursor()
          cursor.execute(query_sql,query_params)
          print('query result : ',cursor.fetchall())
          cursor.close()
       else:
           print('fail to insert table . the connection does not exists! ')

   def delete_record(self,delete_sql,delete_params):
       if self.conn:
          cursor = self.conn.cursor()
          cursor.execute(delete_sql,delete_params)
          print('delete result count: ',cursor.rowcount)
          self.conn.commit()
          cursor.close()
       else:
           print('fail to delete table . the connection does not exists! ')




# now we begin to test the tool class
mysql_obj = MysqlTools('root','root','test','10.0.251.142','3306')
mysql_obj.connect_db()

if mysql_obj.conn:
    mysql_obj.create_table('create table user(id varchar(20) primary key, name varchar(20))') # create table
    mysql_obj.insert_table('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
    mysql_obj.insert_table('insert into user (id, name) values (%s, %s)', ['2', 'Jecka']) # insert one
    mysql_obj.batch_insert_table('insert into user (id, name) values (%s, %s)', [('3', 'AAAA'),('4','BBBB'),('5','CCCC')])  # batch insert
    mysql_obj.query_table('select * from user where name= %s', ('Jecka',))  # query
    mysql_obj.delete_record('delete from user where name= %s', ('AAAA',))  # delete

    mysql_obj.close_db()