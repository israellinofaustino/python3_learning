import mysql.connector
from time import sleep
import datetime
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
    string.line(130)
    string.columns(f'{"ID":<5}', f'{"Name":<15}', f'{"Surname":<25}', f'{"Email":<25}', f'{"Address":<25}', f'{"Registration Date":<25}')
    string.line(130)
    for i in result:
        registration_date = i[5]
        print(f"{i[0]:<5} {i[1]:<15} {i[2]:<25} {i[3]:<25} {i[4]:<25}", registration_date.strftime('%Y %b %d, %I:%M%p'))
    string.line(130)


def show_specify(id):
    mycursor = mydatabase.cursor()
    sql = f"SELECT * FROM person WHERE id = {id}"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for i in myresult:
        return(f"\033[0;35mID => {i[0]} - Name => {i[1]} - Surname => {i[2]} - Email => {i[3]} - Address => {i[4]}\033[m")


def register_user():
    list_of_person = list()
    string.line(45)
    name = str(input("Write your name: ")).strip()
    surname = str(input("Write your surname: ")).strip()
    email = str(input("Write your email: ")).strip()
    address = str(input("Write your address: ")).strip()
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
    while True:
        string.line(100)
        your_option = numbers.valid_int_number("\033[0;33mWhitch user do you want modify? Please write the id user [000 to go back to the menu]=> \033[m")
        if your_option == 000:
            string.title("\033[0;31mBack to the main menu.\033[m", quant1=40, quant2=40, center_mine=47)
            break
        if verify_id(your_option) == True:
            string.line(130)
            print(show_specify(your_option))
            list_of_person = list()
            string.line(130)
            name = str(input("New name: ")).strip()
            surname = str(input("New surname: ")).strip()
            email = str(input("New email: ")).strip()
            address = str(input("New address: ")).strip()
            list_of_person.append(tuple([name, surname, email, address]))
            try:
                mycursor = mydatabase.cursor()
                sqlupdate = f"UPDATE people.person SET name='{name}', surname='{surname}', email='{email}', address='{address}', date_time=NOW() WHERE id={int(your_option)}"
                mycursor.execute(sqlupdate)
                committ()
            except:
                print("\033[0;31mSomething wrong happend.\033[m")
                print(sqlupdate)

            string.line()
            print("\033[0;31mChanging informations...\033[m")
            string.line()
            sleep(2.5)
            print(f"\033[0;32mUser {name} successfully edited!\033[m")
            string.line()
            sleep(1)


def delete_user():
    while True:
        your_option = numbers.valid_int_number("\033[0;33mWhitch user do you want delete? Please write the id user [000 to go back to the menu]=> \033[m")
        if your_option == 000:
            string.title("\033[0;31mBack to the main menu.\033[m", quant1=40, quant2=40, center_mine=47)
            break
        if verify_id(your_option) == True:
            try:
                mycursor = mydatabase.cursor() 
                sqldelete = f"DELETE FROM person WHERE id = {your_option}"
                mycursor.execute(sqldelete)
                committ()
            except:
                print("\033[0;31mSomething wrong happend.\033[m")

            string.line()
            print("\033[0;31mDeleting user...\033[m")
            string.line()
            sleep(2.5)
            print(f"\033[0;32mUser {your_option} successfully deleted!\033[m")
            string.line()
            sleep(1)


def verify_id(id, result = False):
    ids = list()
    mycursor = mydatabase.cursor() 
    table_name = "person"
    mycursor.execute(f"SELECT id FROM {table_name}")
    result = mycursor.fetchall()
    result_list = [list(result) for result in result]
    for i in result_list:
        ids.append(i[0])
    if id not in ids:
        string.line()
        print("User not found in our database!")
        string.line()
        result = False
    else:
        result = True
    return result
