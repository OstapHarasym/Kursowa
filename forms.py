from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField


# Форма для введення даних для обчислення границі
class LimitForm(FlaskForm):
    foo = StringField('Функція')
    to = StringField('Прямує до')
    submit = SubmitField('Порахувати')


# Форма для введення даних для обчислення інтеграла
class IntegralForm(FlaskForm):
    foo = StringField('Функція')
    up = StringField('Верхня межа')
    down = StringField('Нижня межа')
    submit = SubmitField('Порахувати')


# Форма для введення даних для обчислення ряду
class RowForm(FlaskForm):
    foo = StringField('Формула n - елемента ряду')
    count = IntegerField('Кількість перших елементів для суми')
    submit = SubmitField('Порахувати')


# Форма для введення даних для обчислення диф.рівняння
class DiffForm(FlaskForm):
    foo = StringField('Функція')
    y0 = StringField('Y0')
    up = StringField('Від')
    down = StringField('До')
    submit = SubmitField('Порахувати та побудувати графік')


# Форма для введення даних для обчислення визначника матриці
class MatrixForm(FlaskForm):
    a00 = IntegerField()
    a01 = IntegerField()
    a02 = IntegerField()
    a10 = IntegerField()
    a11 = IntegerField()
    a12 = IntegerField()
    a20 = IntegerField()
    a21 = IntegerField()
    a22 = IntegerField()
    submit = SubmitField('Порахувати визначник')
