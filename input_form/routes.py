from input_form import app, db
from input_form.models import Client

from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for
import psycopg2

from .forms import ClientInputForm, BigTestForm


from datetime import datetime




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


company_name_which_use_system = "Solarteka"

@app.route('/')
def index():
    return render_template('add_user.html', title = company_name_which_use_system)

@app.route('/clients', methods=['GET', 'POST'])
def test():
    form = ClientInputForm()
    return render_template('testing_extends.html', title = company_name_which_use_system, form = form)

@app.route('/test')
def clients():
    form = ClientInputForm()
    #form.group_id.choices = [(g.id, g.name) for g in Group.query.order_by('name')]
    return render_template('clients.html', title = company_name_which_use_system, form=form)

@app.route('/vizualusduomenys')
def visual_data():
    return render_template('visual_data.html', title = company_name_which_use_system)

@app.route('/registruotis')
def register():
    return render_template('register.html', title = 'Registruotis')

@app.route('/prisijungti')
def signup():
    return render_template('signup.html', title = 'Prisijungti')

# @app.route('/clients')
# def clients():
#     return render_template('clients.html', title = company_name_which_use_system)

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











@app.route("/big_test", methods = ["GET", "POST"])
def client_input():
    form = BigTestForm()
    # if form.validate_on_sumbit():
    #     return "Sėkmingai išsaugota"    
    return render_template("big_test.html", form = form)

@app.route("/get_data_from_input", methods = ['GET','POST'])
def show_data():
    form = BigTestForm()
    # information_to_save_from_html_to_database = BigTestDatabase(company_name_database = client_name_input_from_html, phone_number_database = client_number_input_from_html)
    # db.session.add(information_to_save_from_html_to_database)
    # db.session.commit()
    
    client_name_input_from_html = form.company_name.data
    client_number_input_from_html = form.phone_number.data
    return client_name_input_from_html + ' kurio vertė ' + str(client_number_input_from_html)


class BigTestDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name_database = db.Column(db.String(40))
    phone_number_database = db.Column(db.Integer)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, company_name_database, phone_number_database):
        self.company_name_database = company_name_database
        self.phone_number_database = phone_number_database