#  sql
#  СУБД -система управления БД
import sqlite3
from sqlite3 import Error


def create_connektion(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error as err:
        print(err)
    return conn


def create_table(cann, sql):
    try:
        cursor = cann.cursor()
        cursor.execute(sql)
    except Error as err:
        print(err)


create_student_table = '''
CREATE TABLE students(
id INTEGER PRIMARY KEY,
fullname VARCHAR (100) NOT NULL,
mark DOUBLE (5,2) NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
birth_date DATE NOT NULL,
is_married BOOLEAN DEFAULT FALSE
)
'''
connekt = create_connektion(r'g22_3_3.db')

if connekt is not None:
    print('все отлично')
    create_table(connekt, create_student_table)
    print('код выполнен')
