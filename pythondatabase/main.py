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

person = []
while True:
    question = str(input("Do you want add someone? [Yes/No] => ")).strip().upper()[0]
    if question == 'N':
        mycursor.execute("SELECT * FROM people.person")
        result = mycursor.fetchall()
        for i in result:
            print(i)
        break    
    name = str(input("Write your name: ")).strip()
    surname = str(input("Write your surname: ")).strip()
    email = str(input("Write your email: ")).strip()
    address = str(input("Write yout address: ")).strip()
    end = str(input("Do you want continue? [Yes/No]: ")).strip().upper()[0]
    person.append(tuple([name, surname, email, address]))
    if end == 'N':
        break
    else:
        continue

sqlinsert = "INSERT INTO person (name, surname, email, address, date_time) VALUES (%s, %s, %s, %s, NOW())"
mycursor.executemany(sqlinsert, person)
mydatabase.commit()
print(mycursor.rowcount, " rows.")
