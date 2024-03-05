from authors_app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash



class User(db.Model):
    _tablename_='users'
    id = db.Column(db.Integer,primary_key=True)
    first_name =db.Column(db.String(50),nullable =False)
    last_name =db.Column(db.String(100),nullable =False)
    email =db.Column(db.String(100),nullable =False,unique =True)
    contact=db.Column(db.Integer,nullable=False)
    user_type=db.Column(db.String(20),default='author')
    user_image =db.Column(db.BLOB,nullable=True)
    biography = db.Column(db.Text, nullable=True)  
    books= db.relationship('Book',backref='user')
    password_hash = db.Column(db.String(128))  # Store the hashed password
    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())

    def _init_(self,first_name,last_name,email,contact,password,user_type,image=None):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.contact=contact
        self.password=password
        self.user_type=user_type
        self.image=image


    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"
    

    #def set_password (self,password):
    #   self._password =bcrypt.generate_password_hash(password).decode('utf-8')