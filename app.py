from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, ImportantDate, Notification, Photo
from flask_migrate import Migrate
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
@app.route('/home')
def index():
    dates = ImportantDate.query.all()
    return render_template("index.html", dates=dates)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/add', methods=['GET', 'POST'])
def add_date():
    if request.method == 'POST':
        title = request.form['title']
        date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        details = request.form.get('details')
        new_date = ImportantDate(title=title, date=date, details=details)
        db.session.add(new_date)
        db.session.commit()
        flash('Important date added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template("add_date.html")

@app.route('/view')
def view_dates():
    dates = ImportantDate.query.all()
    return render_template("view_dates.html", dates=dates)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_date(id):
    date = ImportantDate.query.get_or_404(id)
    if request.method == 'POST':
        date.title = request.form['title']
        date.date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        date.details = request.form.get('details')
        db.session.commit()
        flash('Important date updated successfully!', 'success')
        return redirect(url_for('view_dates'))
    return render_template("edit_date.html", date=date)

@app.route('/details/<int:id>')
def date_details(id):
    date = ImportantDate.query.get_or_404(id)
    return render_template("date_details.html", date=date)

if __name__ == '__main__':
    app.run(debug=True)