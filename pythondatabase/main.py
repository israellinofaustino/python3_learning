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

mycursor = mydatabase.cursor()
# mycursor.execute("CREATE DATABASE people")
# mycursor.execute("CREATE TABLE person (name VARCHAR(255), surnane VARCHAR(255), email VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("ALTER TABLE person ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


# print("-=" * 45)
# mycursor.execute("SHOW DATABASES")
# for base in mycursor:
#     print(base, end='')
# print()
# print("-=" * 45)
# mycursor.execute("SHOW TABLES")
# for tables in mycursor:
#     print(tables)
# print("-=" * 6)

person = []
while True:
    name = str(input("Write your name: ")).strip()
    surname = str(input("Write your surname: ")).strip()
    email = str(input("Write your email: ")).strip()
    address = str(input("Write yout address: ")).strip()
    end = str(input("Do you want continue? [yes/no]: ")).strip().upper()[0]
    person.append(tuple([name, surname, email, address]))
    if end == 'N':
        break
    else:
        continue

sqlinsert = "INSERT INTO person (name, surname, email, address) VALUES (%s, %s, %s, %s)"
mycursor.executemany(sqlinsert, person)
mydatabase.commit()
print(mycursor.rowcount, " was inserted.")
