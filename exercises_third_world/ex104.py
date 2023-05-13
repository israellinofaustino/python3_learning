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



n = valid_n("Write a number => ")
print(f"You just enter the number {n}.")
