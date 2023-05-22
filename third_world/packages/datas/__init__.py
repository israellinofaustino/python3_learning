def read_money(msg):
    valid = False
    while not valid:
        enter = str(input(msg)).replace(',', '.').strip()
        if enter.isalpha() or enter == '':
            print(f"\033[0;31mERROR: \"{enter}\" is not a valid price.\033[m")
        else:
            valid = True
            return float(enter)


def valid_n(msg):
    ok = False
    value = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            value = int(n)
            ok = True
        else:
            print("\033[0;31mError, please enter a valid integer.\033[m")
        if ok:
            break
    return value

