from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    fileupload = FileField('Photo', validators=[FileRequired(), FileAllowed(['png', 'jpeg'], 'Images only!')])