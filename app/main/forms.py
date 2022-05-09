from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import InputRequired

class CommentForm(FlaskForm):

    title = StringField('Comment title',validators=[InputRequired()])
    comment = TextAreaField('Pitch review', validators=[InputRequired()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    category = SelectField('Category', choices=[('short','Short and Simple'),('story','Story Based'),('humour','With Humour')],validators=[InputRequired()])
    post = TextAreaField('Your Pitch', validators=[InputRequired()])
    submit = SubmitField('Pitch')