import pandas as pd
import psycopg2

# Neccessary information about the Database
dbname = 'uxdlljnv'
user = 'uxdlljnv'
password = 'PrNBttEvyflonZQbwTptgWqxwZkLWgc6'
host = 'rajje.db.elephantsql.com'

#Make connection and get cursor
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

df = pd.read_csv('titanic.csv')

#insert each row by iterating through the dataframe
for index, row in df.iterrows():
  row_string = '(' + str(row['Survived']) + ', ' + str(row['Pclass']) + ', ' + "'" + row['Name'].replace("'", "") + "'" + ', ' + "'" + row['Sex'] + "'" + ', ' + str(row['Age']) + ',' + str(row["Siblings/Spouses Aboard"]) + ', ' + str(row["Parents/Children Aboard"]) + ', ' + str(row['Fare']) + ')'
  insert_row = """
    INSERT INTO titanic
    (Survived, Pclass, Name, Sex, Age, "Siblings/Spouses Aboard", "Parents/Children Aboard", Fare)
    VALUES """ + row_string + ";"
  pg_curs.execute(insert_row)

#Close and Commit the changes to the database
pg_curs.close()
pg_conn.commit()
