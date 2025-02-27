from app import mongo
import bcrypt

def get_users():
    return list(mongo.db.users.find({}, {"password": 0}))

def get_user(user_id):
    return mongo.db.users.find_one({"_id": user_id}, {"password": 0})

def create_user(data):
    hashed_pw = bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())
    data["password"] = hashed_pw
    return mongo.db.users.insert_one(data)

def update_user(user_id, data):
    return mongo.db.users.update_one({"_id": user_id}, {"$set": data})

def delete_user(user_id):
    return mongo.db.users.delete_one({"_id": user_id})
