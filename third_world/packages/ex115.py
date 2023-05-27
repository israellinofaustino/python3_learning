import datas
from time import sleep


datas.line(50)
print(f"{'MAIN MENU':^50}")
datas.line(50)
sleep(1.5)
print("1 - See registered people")
sleep(1)
print("2 - Register new person")
sleep(1)
print("3 - Exit")
sleep(1)

datas.line(50)

datas.verify_file_exist()

while True:
    sleep(1)
    your_option = datas.valid_int_number("Your choice [options 1, 2 or 3] => ")
    sleep(1.5)
    if your_option == 1:
        file = open("people.txt", "r")
        datas.line(50)
        print(file.read())
        datas.line(50)
    elif your_option == 2:
        datas.line(50)
        name = str(input("Whats your name? ").strip())
        age = datas.valid_int_number("How old are you? ")
        datas.line(50)
        file = open("people.txt", "a")
        file.write(f"\n{name}, ")
        file.write(str(age))
        file.close
    elif your_option == 3:
        datas.line(50)
        sleep(1)
        print(f"{'Logging out of the system, see you later.':^50}")
        sleep(1)
        datas.line(50)
        break
