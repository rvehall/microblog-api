from app import db
from sqlalchemy import Integer, String, DateTime
from datetime import datetime

class Post(db.Model):
    id = db.Column(Integer, primary_key=True)
    content = db.Column(String(120), index=True, unique=True)
    created_date = db.Column(DateTime, index=True, default=datetime.now())

    def __repr__(self):
        return '<Post {}>'.format(self.title)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
