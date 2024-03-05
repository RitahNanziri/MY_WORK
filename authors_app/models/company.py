from authors_app import db
from datetime import datetime


class Company(db.Model):
    _tablename_='Companies'
    id = db.Column (db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable =False)
    origin =db.Column(db.String(100))
    description = db.Column(db.String(200))
    user_id =db.Column(db.Integer,db.ForeignKey('user.id'))
    user =db.relationship('User',backref='companies')
    created_at =db.Column(db.DateTime,default=datetime.now())
    updated_at =db.Column(db.DateTime,onupdate=datetime.now())
    
    def _repr_(self):
        return f"<Company(name='{self.name}', origin='{self.origin}')>"