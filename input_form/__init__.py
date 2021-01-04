from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/solarteka_database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin@localhost:5432/postgres"
app.config['SECRET_KEY'] = '57f5b19ebf0f6bbff4ffe2233a9e68b0ae91987df9fc6d23e0ab3dfc7f529c0f'


db = SQLAlchemy(app)
from input_form import routes