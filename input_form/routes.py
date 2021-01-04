from input_form import app, db
from input_form.models import Client

from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for
import psycopg2

from .forms import ClientInputForm, RegistrationForm

# app.debug = True

POSTGRES_URI = "postgresql://postgres:admin@localhost:5432/postgres"

connection = psycopg2.connect(POSTGRES_URI)

try:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE transactions (user_name TEXT, email TEXT);"
                           )
except psycopg2.errors.DuplicateTable:
    pass


company_name = "Solarteka"

@app.route('/')
def index():
    return render_template('add_user.html', title = company_name)

@app.route('/test')
def test():
    return render_template('testing_extends.html', title = company_name)

@app.route('/clients')
def clients():
    form = ClientInputForm()
    return render_template('clients.html', title = company_name, form=form)

@app.route('/vizualusduomenys')
def visual_data():
    return render_template('visual_data.html', title = company_name)

@app.route('/registruotis')
def register():
    return render_template('register.html', title = 'Registruotis')

@app.route('/prisijungti')
def signup():
    return render_template('signup.html', title = 'Prisijungti')

# @app.route('/clients')
# def clients():
#     return render_template('clients.html', title = company_name)

@app.route('/post_user', methods=['GET', 'POST'])
def post_user():
    if request.method == "POST":
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO transactions VALUES(%s, %s);",
                               (
                                    request.form.get("username"),
                                    request.form.get("email")
                               ),
        )
        # user = User(request.form['username'], request.form['email'])
        # db.session.add(user)
        # db.session.commit()
    return redirect(url_for('index'))


@app.route('/personalovaldymas')
def show_transactions():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM transactions;")
            employee_page = cursor.fetchall()
    return render_template('employee_page.html', entries = employee_page)