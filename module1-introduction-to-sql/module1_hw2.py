import pandas as pd
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv')

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

curs = conn.cursor()

#df.to_sql('review',con=conn)

curs.execute('select count(*) from review;')
print('Number of rows in review: ', curs.fetchone())

query = 'select count(*) from review where Nature >= 100 and Shopping >= 100;'
curs.execute(query)
print('Count of those who review more than 100 in Nature and Shopping category: ', curs.fetchone())

curs.execute('select sum(Nature)/count(*) from review where Nature >0;')
print('Avrage number of reviews in Nature category: ', curs.fetchone())

curs.execute('select sum(Shopping)/count(*) from review where Shopping >0;')
print('Avrage number of reviews in Shopping category: ', curs.fetchone())

curs.execute('select sum(Sports)/count(*) from review where Sports >0;')
print('Avrage number of reviews in Sports category: ', curs.fetchone())

curs.execute('select sum(Religious)/count(*) from review where Religious >0;')
print('Avrage number of reviews in Religious category: ', curs.fetchone())

curs.execute('select sum(Theatre)/count(*) from review where Theatre >0;')
print('Avrage number of reviews in Theatre category: ', curs.fetchone())

curs.execute('select sum(Picnic)/count(*) from review where Picnic >0;')
print('Avrage number of reviews in Picnic category: ', curs.fetchone())

curs.close()
