import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-9694f-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "9919103105":
        {
            "name": "Geet Jindal",
            "major": "AI",
            "starting_year": 2019,
            "total_attendance": 9,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-04-23 14:54:34"
        },
    "9919103114":
        {
            "name": "Shivansh Tripathi",
            "major": "ML",
            "starting_year": 2019,
            "total_attendance": 15,
            "standing": "A",
            "year": 4,
            "last_attendance_time": "2022-12-18 13:24:46"
        }
}

for key, value in data.items():
    ref.child(key).set(value)