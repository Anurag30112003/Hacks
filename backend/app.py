from flask import Flask
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://anuragdev:anuragsharma123@cluster0.dnlwq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]

mycol = mydb["customers"]

mydict = {"name":"John","address":"New York"}

# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]

# x = mycol.insert_many(mylist)

myquery = { "address": "New York" }


mydoc = mycol.find(myquery)



for x in mydoc:
  print(x)



    

app = Flask(__name__)

@app.route('/variable')
def get_variabel():
    return {'variable': 'helloworld from flask'}