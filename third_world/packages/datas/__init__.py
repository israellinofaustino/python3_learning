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
            print("\033[0;31mError, please enter a valid INTEGER number.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[0;31mUser interrupted data entry.\033[m")
            return 0
        else:
            return n


def valid_float_number(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mError, please enter a valid FLOAT/REAL number.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[0;31mUser interrupted data entry.\033[m")
            return 0
        else:
            return n
