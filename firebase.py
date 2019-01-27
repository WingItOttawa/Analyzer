import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Database:
    def __init__(self):
        cred = credentials.Certificate('equinews-service-key.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        print("Database connection initiated")

    def retrieveDocuments(self):
        docs = self.db.collection(u'master').get()
        return docs
