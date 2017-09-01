from flask_wtf import FlaskForm
from flask_babel import gettext
from wtforms import StringField
from wtforms.validators import DataRequired

from app.categories.models import Category


class NewCategory(FlaskForm):
    name = StringField(gettext('Category name:'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        name = Category.query.filter_by(name=self.name.data).first()
        if name:
            self.name.errors.append(gettext('Category with this name already exists!'))
            return False

        return True

class EditCategory(FlaskForm):
    name = StringField(gettext('Category name:'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        name = Category.query.filter_by(name=self.name.data).first()
        if name:
            self.name.errors.append(gettext('Category with this name already exists!'))
            return False

        return True

class DeleteCategory(FlaskForm):

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        return True