from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URI"))
db = client.github_events
events = db.events
