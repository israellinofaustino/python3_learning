import mysql.connector


def connection_mysql_db():
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
