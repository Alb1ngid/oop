# SQL - Structured Query "language"
#  СУБД система управлен баз данн
import sqlite3
from sqlite3 import Error


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)
    return conn


def create_table(cann, sql):
    try:
        cursor = cann.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)


def create_student(cann, student):
    try:
        sql = '''INSERT INTO students
        (fullname,mark,hobby,birth_date,is_married)
        VALUES (?,?,?,?,?)'''
        cursor = cann.cursor()
        cursor.execute(sql, student)
        cann.commit()
    except Error as e:
        print(e)


create_student_table = '''
CREATE TABLE students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
fullname VARCHAR (200) NOT NULL,
mark DOUBLE (5,2) NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
birth_date DATE NOT NULL,
is_married BOOLEAN DEFAULT FALSE
)
'''

connect = create_connection(r'test.db')
if connect is not None:
    print('все отлично')
    # create_table(connect, create_student_table)
    create_student(connect, ('Beka dj', 23.99, 'стихи', '2003-06-08', False))
    create_student(connect, ('Bek dj', 23.99, 'стихи', '2003-06-08', False))
    print('выполнено')
