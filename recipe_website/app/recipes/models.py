from database import db, CRUDMixin
import datetime


class Recipe(CRUDMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250))
    image_url = db.Column(db.String(250))
    created_ts = db.Column(db.DateTime(timezone=True),
                           server_default=db.func.current_timestamp(),)
    updated_ts = db.Column(db.DateTime(timezone=True),
                           onupdate=db.func.current_timestamp(),)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref='recipe')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='recipe')

    def __init__(self, name, user_id, category_id, description, image_url):
        self.name = name
        self.description = description
        self.image_url = image_url
        self.created_ts = datetime.datetime.now()
        self.user_id = user_id
        self.category_id = category_id

    def __repr__(self):
        return '<Recipe %s>' % self.name

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'image': self.image_url,
            'id': self.id
        }

    @classmethod
    def getRecipeList(self, category_id):
        list = self.query.filter_by(category_id=category_id)
        return list

    @classmethod
    def getCurrentRecipe(self, recipe_id):
        recipe = self.query.filter_by(id=recipe_id).one()
        return recipe
