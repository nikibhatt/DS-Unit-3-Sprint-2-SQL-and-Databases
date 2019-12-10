import pandas as pd
import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')

curs = conn.cursor()

curs.execute('SELECT count(*) FROM charactercreator_character;')
print('Total number of Characters: ', curs.fetchone())

curs.execute('select count(*) from charactercreator_thief;')
print('Number of characters for thief:', curs.fetchone())

curs.execute('select count(*) from charactercreator_cleric;')
print('Number of characters for cleric:', curs.fetchone())

curs.execute('select count(*) from charactercreator_fighter;')
print('Number of characters for fighter:', curs.fetchone())

curs.execute('select count(*) from charactercreator_mage;')
print('Number of characters for mage:', curs.fetchone())

curs.execute('select count(*) from armory_item;')
print('Number of items from armory_item:', curs.fetchone())

curs.execute('select count(*) from armory_item, armory_weapon where item_id = item_ptr_id;')
print('Number of items that are weapons:', curs.fetchone())

curs.execute('select count(*) from armory_item, armory_weapon where item_id != item_ptr_id;')
print('Number of items that are NOT weapons:', curs.fetchone())

query = 'select cc.name, count(cc.character_id) as items from charactercreator_character as cc, armory_item as ai, charactercreator_character_inventory as cci where ai.item_id = cci.id and cc.character_id = cci.character_id group by cc.character_id order by cc.name LIMIT 20 ;'

curs.execute(query)
print('Number of items for each character: ', curs.fetchall())

query = 'select cc.name, count(cc.name) as weapons from charactercreator_character as cc, armory_item as ai, charactercreator_character_inventory as cci, armory_weapon as aw where ai.item_id = cci.id and cc.character_id = cci.character_id and ai.item_id = aw.item_ptr_id group by cc.character_id order by cc.name LIMIT 20;'
curs.execute(query)
print('Number of weapons for each character: ', curs.fetchall())

query = 'select sum(items)/count(*) as avg_items from (select cc.name, count(cc.character_id) as items from charactercreator_character as cc, armory_item as ai, charactercreator_character_inventory as cci where ai.item_id = cci.id and cc.character_id = cci.character_id group by cc.character_id order by cc.name)'
curs.execute(query)
print('Average number of items for each character: ', curs.fetchall())

query = 'select sum(weapons)/count(*) as avg_weapons from (select cc.name, count(cc.name) as weapons from charactercreator_character as cc, armory_item as ai, charactercreator_character_inventory as cci, armory_weapon as aw where ai.item_id = cci.id and cc.character_id = cci.character_id and ai.item_id = aw.item_ptr_id group by cc.character_id order by cc.name)'
curs.execute(query)
print('Average number of weapons for each character: ', curs.fetchone())

curs.close()

df = pd.read_csv('buddymove_holidayiq.csv')
df.to_sql('review',con=conn)

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

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
