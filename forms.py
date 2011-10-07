from wtforms import Form, BooleanField, TextField, validators

class NameForm(Form):
    description = TextField('Description', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
