from app.database import db, CRUDMixin
from sqlalchemy import asc
import datetime


class Category(CRUDMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False, unique=True)
    created_ts = db.Column(db.DateTime(timezone=True),
            server_default=db.func.current_timestamp(),)
    updated_ts = db.Column(db.DateTime(timezone=True),
            onupdate=db.func.current_timestamp(),)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='category')

    def __init__(self, name, user_id):
        self.name = name
        self.created_ts = datetime.datetime.now()
        self.user_id = user_id

    def __repr__(self):
        return '<Category %s>' % self.name

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }

    @classmethod
    def getCategories(cls):
        list = cls.query.order_by(asc(cls.name))
        return list

    @classmethod
    def getCurrentCategory(cls, category_id):
        category = cls.query.filter_by(id=category_id).one()
        return category
