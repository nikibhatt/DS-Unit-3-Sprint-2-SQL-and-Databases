import pandas as pd
import psycopg2

dbname = 'uxdlljnv'
user = 'uxdlljnv'
password = 'PrNBttEvyflonZQbwTptgWqxwZkLWgc6'
host = 'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

df = pd.read_csv('titanic.csv')

for index, row in df.iterrows():
  # row['Name'] = row['Name'].astype(str)
  # row['Sex'] = row['Sex'].astype(str)
  row_string = '(' + str(row['Survived']) + ', ' + str(row['Pclass']) + ', ' + "'" + row['Name'].replace("'", "") + "'" + ', ' + "'" + row['Sex'] + "'" + ', ' + str(row['Age']) + ',' + str(row["Siblings/Spouses Aboard"]) + ', ' + str(row["Parents/Children Aboard"]) + ', ' + str(row['Fare']) + ')'
  insert_row = """
    INSERT INTO titanic
    (Survived, Pclass, Name, Sex, Age, "Siblings/Spouses Aboard", "Parents/Children Aboard", Fare)
    VALUES """ + row_string + ";"
  pg_curs.execute(insert_row)

pg_curs.close()
pg_conn.commit()
