import re
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


def strong_password(form, field):
    p = field.data
    if len(p) < 8:
        raise ValidationError("Parol kamida 8 ta belgidan iborat bo'lishi kerak.")
    if not re.search(r'[A-Z]', p):
        raise ValidationError("Parolda kamida 1 ta katta harf (A-Z) bo'lishi kerak.")
    if not re.search(r'[a-z]', p):
        raise ValidationError("Parolda kamida 1 ta kichik harf (a-z) bo'lishi kerak.")
    if not re.search(r'\d', p):
        raise ValidationError("Parolda kamida 1 ta raqam bo'lishi kerak.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', p):
        raise ValidationError("Parolda kamida 1 ta maxsus belgi bo'lishi kerak.")


class RegisterForm(FlaskForm):
    username = StringField('Foydalanuvchi nomi',
        validators=[DataRequired('Majburiy maydon.'),
                    Length(min=3, max=80, message="3-80 ta belgi bo'lishi kerak.")])
    email = StringField('Email manzil',
        validators=[DataRequired('Majburiy maydon.'),
                    Email("To'g'ri email kiriting.")])
    password = PasswordField('Parol',
        validators=[DataRequired('Majburiy maydon.'), strong_password])
    confirm_password = PasswordField('Parolni tasdiqlang',
        validators=[DataRequired('Majburiy maydon.'),
                    EqualTo('password', message='Parollar mos kelmadi.')])
    submit = SubmitField("Ro'yxatdan o'tish")

    def validate_username(self, field):
        from models import User
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Bu foydalanuvchi nomi band.')

    def validate_email(self, field):
        from models import User
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError("Bu email allaqachon ro'yxatdan o'tgan.")


class LoginForm(FlaskForm):
    email = StringField('Email manzil',
        validators=[DataRequired('Majburiy maydon.'),
                    Email("To'g'ri email kiriting.")])
    password = PasswordField('Parol',
        validators=[DataRequired('Majburiy maydon.')])
    submit = SubmitField('Kirish')
