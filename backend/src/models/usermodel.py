from config import db

class UserModel(db.Model):
    __tablename__ = 'tbl_userlist'

    user_id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))

    def __init__(self, display_name, username, password):
        self.display_name = display_name
        self.username = username
        self.password = password

    def json(self):
        return {
            'display_name': self.display_name,
            'username': self.username,
            'password': self.password
        }

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()
