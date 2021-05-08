import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

result = db.collection('users').get()

for each in result:
    print(each.to_dict()['userhandle'])
