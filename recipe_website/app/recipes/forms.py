from flask_wtf import FlaskForm
from flask_babel import gettext
from wtforms import StringField
from wtforms.validators import DataRequired

from .models import Recipe


class NewRecipe(FlaskForm):
    name = StringField(gettext('Recipe name:'), validators=[DataRequired()])
    description = StringField(gettext('Recipe Description:'),
                              validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        return True


class EditRecipe(FlaskForm):
    name = StringField(gettext('Recipe name:'), validators=[DataRequired()])
    description = StringField(gettext('Recipe Description:'),
                              validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        return True


class DeleteRecipe(FlaskForm):

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        return True
