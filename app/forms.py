
from flask_wtf import FlaskForm
from datetime import date
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DecimalField, SelectField,  MultipleFileField, FloatField, DateField
from wtforms.validators import DataRequired, Email, Length, NumberRange, Optional
from flask_wtf.file import FileAllowed, FileRequired, FileField


#For the Add Land Form
class AddLandForm(FlaskForm):
  title = StringField('Titre', validators=[DataRequired()])
  location = StringField('Emplacement', validators=[DataRequired()])
  price = DecimalField('prix (in GF)', validators=[DataRequired(), NumberRange(min=0)])
  description = TextAreaField('Description', validators=[DataRequired(), Length(min=8)])
  features = StringField('Features', validators=[Optional()])
  status = StringField('Status', validators=[DataRequired()])
  mainImage = FileField('Main Image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images Only!')], render_kw={"class": "upload-Images"})
  gallery = MultipleFileField('Gallery Images', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images Seulement!')], render_kw={"class": "upload-Images"})

  latitude = FloatField('Latitude', validators=[Optional()])
  longitude = FloatField('Longitude', validators=[Optional()])
  #Owner informatin
  name = StringField('Num', validators=[DataRequired()])
  phone = StringField('Phone', validators=[DataRequired()])
  email = StringField('Email', validators=[Email()])
  submit = SubmitField('Ajouter le terrain')


# The Class for the Login Page
class LoginForm(FlaskForm):
  Name = StringField('Username', validators=[DataRequired()])
  Password = PasswordField('Password', validators=[DataRequired()])
  Submit = SubmitField('se connecte')
# The Class for the Contact
class ContactForm(FlaskForm):
  FirstName = StringField('Nom', validators=[DataRequired()])
  LastName = StringField('Prénom', validators=[DataRequired()])
  Phone = StringField('Phone', validators=[DataRequired()])
  Email = StringField('Email', validators=[DataRequired(), Email()])
  Message = TextAreaField('Messages', validators=[DataRequired(), Length(min=15)])
  Submit = SubmitField('Envoyer')


class DeleteForm(FlaskForm):
  submit = SubmitField('Delete')

class SellLandForm(FlaskForm):
  land_id = SelectField('Sélectionner le terrain', choices=[], coerce=int, validators=[DataRequired()], render_kw={"class": "upload-Images"})
  buyerName = StringField('Nom de lacheteur ', validators=[DataRequired()])
  phone = StringField('Phone', validators=[DataRequired()])
  sale_date = DateField('Date de vente', format='%Y-%m-%d', default=date.today)
  documents = FileField('Téléverser des Documnet', validators=[FileAllowed(['jpg', 'jpeg', 'pdf', 'png'], 'Images or PDFs only!')], render_kw={"class": "upload-Images"})
  submit = SubmitField('Marquer comme vendu')