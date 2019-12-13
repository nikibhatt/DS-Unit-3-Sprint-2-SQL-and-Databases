""" Describe file """

import sqllite3

conn = sqllite3.connect('Name_of_database')

#Put your variables here.

def make_db()
  """ Describe this function here """
  curs = conn.cursor()
  #execute your queries to create database and insert
  curs.close()
  conn.commit()

def run_queries()
  """ Describe this function here """
  curs.cursor()
  print(curs.execute('SELECT * from table;').fetchall())

if __name__ == "__main__"
  make_db()
  run_queries()  
