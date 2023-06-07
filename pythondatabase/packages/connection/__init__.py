import mysql.connector
from packages import string, numbers

mydatabase = mysql.connector.connect(
    host='localhost',
    username='root',
    password='',
    database='people'
)
if mydatabase.is_connected() == True:
    print('Successfully Connected!')
else:
    print('Something wrong happend with the database connection.')


def committ():
    return mydatabase.commit()


def show_data(table_name):
    mycursor = mydatabase.cursor() 
    mycursor.execute(f"SELECT * FROM {table_name}")
    result = mycursor.fetchall()
    for i in result:
        print(i)


def register_user():
    list_of_person = list()
    string.line(45)
    name = str(input("Write your name: ")).strip()
    surname = str(input("Write your surname: ")).strip()
    email = str(input("Write your email: ")).strip()
    address = str(input("Write yout address: ")).strip()
    list_of_person.append(tuple([name, surname, email, address]))
    try:
        mycursor = mydatabase.cursor() 
        sqlinsert = "INSERT INTO person (name, surname, email, address, date_time) VALUES (%s, %s, %s, %s, NOW())"
        mycursor.executemany(sqlinsert, list_of_person)
        committ()
    except:
        print("Something wrong happend.")
    else:
        string.title("Successfully registered.", quant1=45, quant2=45, center_mine=45)


def edit_user():
    print('LOADING...')


def delete_user():
    print('LOADING...')

