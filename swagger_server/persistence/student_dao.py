import os
import pymongo
from bson.objectid import ObjectId

class StudentDAO:
    def __init__(self):
        self.client = pymongo.MongoClient(os.getenv("MONGO_URI", "mongodb://mongo:27017/"))
        self.db = self.client[os.getenv("DB_NAME", "student_db")]
        self.collection = self.db[os.getenv("COLLECTION_NAME", "students")]

    def add(self, student):
        if not student:
            return "Invalid provided student data", 400

        student_exists = self.collection.find_one({
            "first_name": student.first_name,
            "last_name": student.last_name
        })

        if student_exists:
            return "already exists", 409

        res = self.collection.insert_one(student.to_dict())
        return str(res.inserted_id)

    def get_by_id(self, student_id):
        if not student_id:
            return "Invalid provided student_id", 400

        student = self.collection.find_one({"_id": ObjectId(student_id)})
        if not student:
            return "not found", 404

        # ObjectID can not be natively not JSON serializable
        student["_id"] = str(student["_id"])
        return student

    def delete(self, student_id):
        try:
            student_id = ObjectId(student_id)
        except Exception as e:
            return "Invalid provided student_id", 400

        student = self.collection.find_one({"_id": student_id})
        if not student:
            return "not found", 404

        self.collection.delete_one({"_id": student_id})

        # ObjectID can not be natively not JSON serializable
        student["_id"] = str(student["_id"])
        return student
