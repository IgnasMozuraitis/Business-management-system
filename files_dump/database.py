"""
20201230 After cleaning files structure not necessary for running app

"""

# import sqlite3
#
# # Query The DB and Return All Records
# def show_all():
#     # Connect to database and create cursor
#     conn = sqlite3.connect('employee.db')
#     c = conn.cursor()
#
#     # Query The Datbase
#     c.execute("SELECT username, * FROM employees")
#     items = c.fetchall()
#
#     for item in items:
#         print(item)
#
#     # Commit our command
#     conn.commit()
#     # Close our connection
#     conn.close()
#
#
# # Add A New Record To The Table
# def add_one(username, email):
#     # Connect to database and create cursor
#     conn = sqlite3.connect('employee.db')
#     c = conn.cursor()
#     c.execute("INSERT INTO employees VALUES (:username, :email)",
#           {'username':username, 'email':email})
#     # Commit our command
#     conn.commit()
#     # Close our connection
#     conn.close()
#
#
# username = 'naujasdarbuotojas1'
# email = 'naujasdarbuotojas1@darbas.com'
#
# conn = sqlite3.connect('employee.db')
#
# c = conn.cursor()
#
# # c.execute("""CREATE TABLE employees (
# #             username text,
# #             email text
# #             )""")
# #
# c.execute("INSERT INTO employees VALUES (:username, :email)",
#           {'username':username, 'email':email})
# conn.commit()
#
# # c.execute("SELECT * FROM employees WHERE username = ?", ('naujasdarbuotojas',)
# # print(c.fetchall())
#
#
# c.execute("SELECT * FROM employees WHERE username = username", {'username': 'naujasdarbuotojas'})
# print(c.fetchall())
#
# conn.commit()
#
# conn.close()