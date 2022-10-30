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


def create_student(cann, student):
    try:
        sql = ''' INSERT INTO students
        (fullname,mark,hobby,birth_date,is_married)
        VALUES(?,?,?,?,?)'''
        cursor = cann.cursor()
        cursor.execute(sql, student)
        cann.commit()
    except Error as err:
        print(err)


create_student_table = '''
CREATE TABLE students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
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
    # create_table(connekt, create_student_table)
    create_student(connekt, ("Mark Daniels", 77.12, "Football", "1999-01-02", False))
    create_student(connekt, ("Alex Brilliant", 77.12, None, "1989-12-31", True))
    create_student(connekt, ("Diana Julls", 99.3, "Tennis", "2005-01-22", True))
    create_student(connekt, ("Michael Corse", 100.0, "Diving", "2001-09-17", True))
    create_student(connekt, ("Jack Moris", 50.2, "Fishing and cooking", "2001-07-12", True))
    create_student(connekt, ("Viola Manilson", 41.82, None, "1991-03-01", False))
    create_student(connekt, ('beka dz', 44.44, 'стихи', '2003-06-06', False))
    print('код выполнен')
