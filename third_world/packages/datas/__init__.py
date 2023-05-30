import os
from time import sleep

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
        f.close()
        return f


def menu(text, quant1 = 30, quant2 = 30, center_mine = 30):
    line(quant1)
    print(text.center(center_mine))
    line(quant2)


def options(opt1 = "", opt2 = "", opt3 = ""):
    dict_ = {"1":opt1, "2":opt2, "3":opt3}
    for i, v in dict_.items():
        print(f"\033[0;32m{i} - {v}\033[m")
    line()


def show_users():
    file = open("people.txt", "r")
    line(40)
    users = file.readlines()
    for i in users:
        name = i.split(";")[0]
        age = i.split(";")[1]
        print(f"\033[0;35m{name:<25}  {age} years old.\033[m")
        sleep(0.5)
    line(40)


def register_user():
    line(45)
    name = str(input("Whats your name? ").strip())
    age = valid_int_number("How old are you? ")
    try:
        file = open("people.txt", "a")
        file.write(f"\n{name};{str(age)};".lstrip())
        file.close()
    except:
        print("Something wrong happend.")
    else:
        menu(f"'{name}' successfully registered.", quant1=45, quant2=45)

