""" SC Part2"""

import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')

curs = conn.cursor()
query = 'select ProductName, CompanyName as Supplier from Product, Supplier where Product.SupplierId = Supplier.Id Order by UnitPrice desc limit 10'

print('10 most expensive items and their suppliers', curs.execute(query).fetchall())

query = 'select Category.CategoryName, count(*) from Product,Category where Product.CategoryId = Category.Id group by Product.CategoryId order by count(*) DESC limit 1'

print('The largest category by number of unique products in it is: ', curs.execute(query).fetchone())

query = 'select Employee.FirstName, Employee.LastName, count(EmployeeTerritory.TerritoryId) from Employee, EmployeeTerritory where Employee.Id = EmployeeTerritory.EmployeeId GROUP by EmployeeTerritory.EmployeeId order by count(EmployeeTerritory.TerritoryId) desc limit 1'

print('The employee with the most territories is: ', curs.execute(query).fetchone())
