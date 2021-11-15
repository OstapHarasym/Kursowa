from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import *
import calc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kr580'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calculus.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    calcType = db.Column(db.String(20), nullable=False)
    calcTime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Stats %r>' % self.id


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/integral/', methods=['GET', 'POST'])
def integral():
    form = IntegralForm()
    if form.is_submitted():
        action = Stats(calcType='Інтеграл')
        db.session.add(action)
        db.session.commit()
        result = calc.integrate(request.form.get('foo'), request.form.get('up'), request.form.get('down'))
        return render_template('integral.html', form=form, result=result)
    return render_template('integral.html', form=form, result='')


@app.route('/differential/', methods=['GET', 'POST'])
def differential():
    form = DiffForm()
    if form.is_submitted():
        action = Stats(calcType='Диф.рівняння')
        db.session.add(action)
        db.session.commit()
        result = calc.differential(request.form.get('foo'), request.form.get('y0'), request.form.get('up'), request.form.get('down'))
        return render_template('differential.html', form=form, result=result[0])
    return render_template('differential.html', form=form, result='Результат')


@app.route('/matrix/', methods=['GET', 'POST'])
def matrix():
    form = MatrixForm()
    if form.is_submitted():
        action = Stats(calcType='Матриця')
        db.session.add(action)
        db.session.commit()
        result = calc.determinant(request.form.values())
        return render_template('matrix.html', form=form, result=result)
    return render_template('matrix.html', form=form, result='')


@app.route('/row/', methods=['GET', 'POST'])
def row():
    form = RowForm()
    if form.is_submitted():
        action = Stats(calcType='Ряд')
        db.session.add(action)
        db.session.commit()
        result = calc.progression_sum(request.form.get('foo'), int(request.form.get('count')))
        return render_template('row.html', form=form, result=result)
    return render_template('row.html', form=form, result='')


@app.route('/limit/', methods=['GET', 'POST'])
def limit():
    form = LimitForm()
    if form.is_submitted():
        action = Stats(calcType='Границя')
        db.session.add(action)
        db.session.commit()
        result = calc.lim(request.form.get('foo'), request.form.get('to'))
        return render_template('limit.html', form=form, result=result)
    return render_template('limit.html', form=form, result='')


@app.route('/stats/')
def stats():
    calc.stats(Stats.query.all())
    return render_template('stats.html')


if __name__ == '__main__':
    app.run(debug=True)
