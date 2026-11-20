from pymongo import MongoClient

#connect to the database clinic_message
client = MongoClient("mongodb://localhost:27017/")
db = client["clinic_messaging"]
messages = db["messages"]

