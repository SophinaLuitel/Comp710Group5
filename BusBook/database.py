from flask_sqlalchemy import SQLAlchemy
from flask import Flask
db = SQLAlchemy()
SQLALCHEMY_BINDS = {
    'users':        'sqlite:///users.sqlite3',
    'flight':      'sqlite:///flights.sqlite3'
}


class User(db.Model):
    __bind_key__ = 'users'
    _id = db.Column("id" ,db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

class Flights(db.Model):
    __bind_key__ = 'flights'
    _id = db.Column("id" ,db.Integer, primary_key=True)
    startLocation = db.Column("startLocation", db.String(100))
    startDate = db.Column("startDate", db.String(100))
    endLocation = db.Column("endLocation", db.String(100))
    endDate = db.Column("endDate", db.String(100))
    currentCapacity = db.Column("currentCapacity", db.Integer)
    maxCapacity = db.Column("maxCapacity", db.Integer)
    

    def __init__(self, name, email):
        self.name = name
        self.email = email