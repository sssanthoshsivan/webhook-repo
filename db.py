from pymongo import MongoClient
import os

uri = os.getenv("MONGO_URI")
if not uri:
    raise RuntimeError("MONGO_URI not set. Check .env file.")

client = MongoClient(uri)
db = client.github_events
events = db.events
