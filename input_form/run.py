from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for
import psycopg2


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.debug = True
db = SQLAlchemy(app)
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


# transactions = [
#     ('jonas', 'jonas@darbas.com'),
#     ('Petras', 'petras@darbas.com')
# ]


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_name = db.Column(db.String(30))
#     email = db.Column(db.String(30), unique = True)
#
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def __repr__(self):
#         return '<User %r>' % self.username

@app.route('/')
def index():
    return render_template('add_user.html')

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


@app.route('/transactions')
def show_transactions():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM transactions;")
            transactions = cursor.fetchall()
    return render_template('employee_page.html', entries = transactions)


if __name__ == "__main__":
    app.run()
