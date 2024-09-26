from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UploadPhotoForm(FlaskForm):
    photo = FileField('Загрузить фото', validators=[FileAllowed(['jpg', 'png'], 'Только изображения!')])
    description = StringField('Описание', validators=[DataRequired()])
    submit = SubmitField('Загрузить')