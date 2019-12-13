""" Sprint Challenge """

import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')

#Put your variables here.

def make_db():
  """ Make demo table """
  curs = conn.cursor()
  create_table = 'CREATE TABLE demo (s varchar(10), x int, y int);'
  curs.execute(create_table)
  insert_sql = 'INSERT INTO demo values (\'g\', 3, 9);'
  curs.execute(insert_sql)
  insert_sql = 'INSERT INTO demo values (\'v\', 5, 7);'
  curs.execute(insert_sql)
  insert_sql = 'INSERT INTO demo values (\'f\', 8, 7);'
  curs.execute(insert_sql)
  curs.close()
  conn.commit()

def run_queries():
  """ Confirm the data """
  curs = conn.cursor()
  query = 'SELECT COUNT(*) from demo;'
  print('Total rows in demo', curs.execute(query).fetchall())
  query = 'SELECT COUNT(*) from demo where x>5 and y>5;'
  print('Total rows where x and y are greater than 5', curs.execute(query).fetchall())
  query = 'SELECT COUNT(DISTINCT y) from demo;'
  print('Number of unique values of y', curs.execute(query).fetchall())
  curs.close()

#if __name__ == "__main__"
make_db()
run_queries()
