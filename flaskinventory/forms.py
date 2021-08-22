from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class addproduct(FlaskForm):
    prodname = StringField('Book Name', validators=[DataRequired()])
    prodqty = IntegerField('Quantity', validators=[NumberRange(min=1, max=5), DataRequired()])
    prodsubmit = SubmitField('Save Changes')


class editproduct(FlaskForm):
    editname = StringField('Book Name', validators=[DataRequired()])
    editqty = IntegerField('Quantity', validators=[NumberRange(min=1, max=5), DataRequired()])
    editsubmit = SubmitField('Save Changes')


class addlocation(FlaskForm):
    locname = StringField('Student Name', validators=[DataRequired()])
    locsubmit = SubmitField('Save Changes')


class editlocation(FlaskForm):
    editlocname = StringField('Student Name', validators=[DataRequired()])
    editlocsubmit = SubmitField('Save Changes')


class moveproduct(FlaskForm):
    mprodname = SelectField(
        'Book Name')
    src = SelectField(
        'Source')
    destination = SelectField(
        'Destination')
    mprodqty = IntegerField('Quantity', validators=[NumberRange(min=1, max=5), DataRequired()])
    movesubmit = SubmitField('Move')
