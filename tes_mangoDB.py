from pymongo import MongoClient

uri = "mongodb+srv://mergetech2027_db_user:2006Raja@cluster0.0xrzpyq.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Connection failed:", e)