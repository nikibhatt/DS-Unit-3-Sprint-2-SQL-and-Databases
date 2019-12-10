#!pip install psycopg2-binary

import psycopg2

dbname = 'uxdlljnv'
user = 'uxdlljnv'
password = 'PrNBttEvyflonZQbwTptgWqxwZkLWgc6'
host = 'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

# pg_curs.execute('SELECT * FROM test_table;')
# print(pg_curs.fetchall())

#!"c:\Program Files (x86)\GnuWin32\wget" https://github.com/nikibhatt/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3

#!mv 'rpg_db.sqlite3?raw=true' rpg_db.sqlite3

import sqlite3

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

characters = sl_curs.execute('select * from charactercreator_character').fetchall()

sl_curs.close()
sl_conn.commit()

for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
  pg_curs.execute(insert_character)

pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = pg_curs.fetchall()

pg_curs.close()
pg_conn.commit()

for character, pg_character in zip(characters, pg_characters):
    assert character == pg_character
