#Q1. What is MongoDB? Explain non-relational databases in short. In which scenarios it is preferred to use MongoDB over SQL databases?
'''
MongoDB is a NoSQL database. Non relational databases store data in document based format. It 
is suited for hierarchical data storage and have dynamic schema.

MongoDB is preferred:
1) When the data is semi structured or unstructured and the schema needs to be flexible.
2) Need horizontal scaling
3) Need to store different types of data
4) Not concerned about data consistency
'''


#Q2. State and Explain the features of MongoDB.
'''
Features of MongoDB:
1) Supports ad hoc queries - field queries, range queries and regular expression searches.
2) Indexing - can be declared on any field within documents improving search speed and performance.
3) Replication - increases data availability by creating multiple copies of data across servers.
4) Sharding - splits larger datasets across multiple distributed collections helping the database distribute
and better execute complex queries.
5) Load Balancing - supports large-scale load balancing through horizontal scaling features
like replication and sharding. 
'''


#Q3. Write a code to connect MongoDB to Python. Also, create a database and a collection in MongoDB.

import pymongo
client = pymongo.MongoClient("mongodb+srv://naveeng:throwthedisc@cluster0.vralyxn.mongodb.net/?retryWrites=true&w=majority")
db = client.test

db = client['workers']
jr_workers = db['jr_record']


'''Q4. Using the database and the collection created in question number 3, write a code to insert one record,
and insert many records. Use the find() and find_one() methods to print the inserted record.'''

oliver = {'name':'Oliver','age':26,'position':'analyst'}
jr_workers.insert_one(oliver)

lst = [{'name':'John','age':30,'position':'associate'},
      {'name':'Peter','age':24,'position':'analyst'},
      {'name':'Patrick','age':34,'position':'sr_associate'},]
jr_workers.insert_many(lst)

for i in jr_workers.find():
    print(i)

print(jr_workers.find_one())


#Q5. Explain how you can use the find() method to query the MongoDB database. Write a simple code to demonstrate this.
''' find() method returns a cursor to the documents. The parameters are optional and can be any criteria
to filter the documents. If no criteria is entered, all the documents are returned.'''

for k in jr_workers.find({'position':'analyst'}):
    print(k)


#Q6. Explain the sort() method. Give an example to demonstrate sorting in MongoDB.

'''sort() method is used to sort documents. It takes fieldname and direction as parameters.
The value +1 indicates ascending order and -1 indicates descending order'''

for i in jr_workers.find().sort('age', -1):
    print(i)


#Q7. Explain why delete_one(), delete_many(), and drop() is used.
'''
delete_one() deletes the first document that matches the specified criteria.

delete_many() deletes all the documents that match the specified criteria. If no criteria is mentioned it
deletes all the documents.

drop() is used to delete a collection. It returns true if deleted successfully and false if the file
does not exist.
'''