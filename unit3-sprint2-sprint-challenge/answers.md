""" Answers to SC questions ...

- In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables?
 One-to-Many. One Employee can have multiple territories, as seen in the
 EmployeeTerritory table. If you group by EmployeeId, you get multiple counts
 of TerritoryId but if grouped by TerritoryId, count of EmployeeId is always 1.

- What is a situation where a document store (like MongoDB) is appropriate, and
  what is a situation where it is not appropriate?
  MongoDB is a NoSQL database and it is appropriate to be used when the data is
  unstructured. For example if the data is bunch of documents, then MongoDB is
  a good choice. But if the data is or can be better exressed in form of
  interconnected tables, then MongoDB is not a good choice.

- What is "NewSQL", and what is it trying to achieve?
  Classic SQL has benefit of satisfying all ACID properties, and NOSQL  has
  benefit of being fast and simple. NewSQL is a vision to provide both of those
  benefits. NewSQL also attempts to over the limitations of each, scalability
  and flexibility of RDBMS, and making updates and making good analytical reports.

"""
