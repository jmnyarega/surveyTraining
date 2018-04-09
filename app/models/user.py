from app import db

class User(db.Model):
    '''
    Defines properties for a user to generate users table in db
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), unique=True)
    lastname = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    mobile = db.Column(db.String(120))
    gender = db.Column(db.String(10))
    profession = db.Column(db.String(10))
    created_at = db.Column(db.DateTime())

    def __init__(
        self,
        firstname,
        lastname,
        email,
        mobile,
        gender,
        profession,
        created_at
        ):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.mobile = mobile
        self.gender = gender
        self.profession = profession
        self.created_at = created_at

    def __str__(self):
        return "User(id='%s')" % self.id
