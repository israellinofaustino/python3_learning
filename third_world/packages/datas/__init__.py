import os


def read_money(msg):
    valid = False
    while not valid:
        enter = str(input(msg)).replace(',', '.').strip()
        if enter.isalpha() or enter == '':
            print(f"\033[0;31mERROR: \"{enter}\" is not a valid price.\033[m")
        else:
            valid = True
            return float(enter)


def valid_int_number(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mError, please write a valid number.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[0;31mUser interrupted data entry.\033[m")
            return 3
        else:
            return n



def valid_float_number(msg):
    while True:
        try:
            n = float(input(msg).strip())
        except (ValueError, TypeError):
            print("\033[0;31mError, please enter a valid FLOAT/REAL number.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[0;31mUser interrupted data entry.\033[m")
            return 0
        else:
            return n


def line(object = 30):
    print("-" * object)


def verify_file_exist():
    path = 'D:/src/learning-python/fundamentals/CursoEmVideo/third_world/packages/people.txt'
    isFile = os.path.isfile(path)

    if isFile == False:
        f = open("people.txt", "a")
        f.write("-----------------------USERS----------------------")
        f.close()
        return f


def menu(text):
    line()
    print(text.center(30))
    line()


def options(opt1 = "", opt2 = "", opt3 = ""):
    dict_ = {"1":opt1, "2":opt2, "3":opt3}
    for i, v in dict_.items():
        print(f"{i} - {v}")
    line()


def show_users():
    file = open("people.txt", "r")
    line(40)
    users = file.readlines()
    for i in users:
        name = i.split(";")[0]
        age = i.split(";")[1]
        print(f"{name:<25}  {age} years old.")
    line(40)


def register_user():
    line(45)
    name = str(input("Whats your name? ").strip())
    age = valid_int_number("How old are you? ")
    file = open("people.txt", "a")
    # file.write(f"{name};")
    file.writable(f"{name};{str(age)};")
    file.close

