from config import db


class ThoughtModel(db.Model):
    __tablename_ = 'tbl_thoughtlist'

    thought_id = db.Column(db.Integer, primary_key=True)

    # user_id = db.Column(db.Integer, db.Foreignkey('tbl_userlist.user_id'))
    # user = db.relationship('UserModel')

    thought_content = db.Column(db.String(255))
    is_done = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, thought_content, is_done):
        self.thought_content = thought_content
        self.is_done = is_done
    
    def json(self):
        return { 'ID': self.thought_id, 'isDone': self.is_done }

    @classmethod
    def find_by_id(cls, thought_id):
        return cls.query.filter_by(thought_id=thought_id).first()
    
    @classmethod
    def find_by_content(cls, thought_content):
        return cls.query.filter_by(thought_content=thought_content).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


