""" SC Part2"""

import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')

curs = conn.cursor()

def execute_with_doc_string(query, msg):
    """Executing Query provided and printing with message provided"""
    print(msg, curs.execute(query).fetchall())

query = 'select ProductName, CompanyName as Supplier from Product, Supplier where Product.SupplierId = Supplier.Id Order by UnitPrice desc limit 10'
msg = '10 most expensive items and their suppliers'
execute_with_doc_string(query, msg)

query = 'select Category.CategoryName, count(*) from Product,Category where Product.CategoryId = Category.Id group by Product.CategoryId order by count(*) DESC limit 1'
msg = 'The largest category by number of unique products in it is: '
execute_with_doc_string(query, msg)

query = 'select Employee.FirstName || \' \' || Employee.LastName as FullName, count(EmployeeTerritory.TerritoryId) from Employee, EmployeeTerritory where Employee.Id = EmployeeTerritory.EmployeeId GROUP by EmployeeTerritory.EmployeeId order by count(EmployeeTerritory.TerritoryId) desc limit 1'
msg = 'The employee with the most territories is: '
execute_with_doc_string(query, msg)
