import mysql.connector


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


def insert_data(list_data):
    mycursor = mydatabase.cursor() 
    sqlinsert = "INSERT INTO person (name, surname, email, address, date_time) VALUES (%s, %s, %s, %s, NOW())"
    mycursor.executemany(sqlinsert, list_data)
    committ()

