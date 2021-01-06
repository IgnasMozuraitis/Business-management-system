from input_form import db
from datetime import datetime

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(30), unique=True, nullable = False)
    manager = db.Column(db.String(30), unique=True, nullable = False)
    # phone_number = db.Column(db.Integer(), unique=True, nullable = False)
    # email = db.Column(db.String(50), unique=True, nullable = False)
    # adress = db.Column(db.String(50), unique=True, nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f"Klientas ({self.company_name} : {self.email} : {self.date_created}')"
