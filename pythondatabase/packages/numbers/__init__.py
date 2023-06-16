def valid_int_number(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mError, please write a valid number.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[0;31mUser interrupted data entry.\033[m")
            return 000
        else:
            return n