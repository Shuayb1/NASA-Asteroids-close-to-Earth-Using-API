import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["my_database"]
mycol = mydb["customers"]

mydoc = [{"name": "Ade", "address": "Highway 37"}, {"name": "Wos", "address": "Highway 38"},
          {"name": "John", "address": "Highway 39"}, {"name": "Kola", "address": "Highway 40"}]

# x = mycol.insert_many(mydoc)
print('************************************************\n')
print('The number of documents in my collection: %s' % mycol.count())
print('\n****************\n')

print('All entries with ‘Kola’ in field ‘name: %s' % mycol.count({'name':'Ade'}))
print('\n****************\n')

x = mycol.find_one()

print('Printing all entries: %s' % x)

print('\n************************************************')

