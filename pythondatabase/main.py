from packages import connection


list_of_person = []
while True:
    question = str(input("Do you want add someone? [Yes/No] => ")).strip().upper()[0]
    if question == 'N':
        connection.show_data('people.person')
        break
    name = str(input("Write your name: ")).strip()
    surname = str(input("Write your surname: ")).strip()
    email = str(input("Write your email: ")).strip()
    address = str(input("Write yout address: ")).strip()
    end = str(input("Do you want continue? [Yes/No]: ")).strip().upper()[0]
    list_of_person.append(tuple([name, surname, email, address]))
    if end == 'N':
        break
    else:
        continue

connection.insert_data(list_of_person)