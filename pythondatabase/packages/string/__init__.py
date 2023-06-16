def line(object = 30):
    print("-" * object)


def title(text, quant1 = 30, quant2 = 30, center_mine = 30):
    line(quant1)
    print(text.center(center_mine))
    line(quant2)


def options(opt1 = "", opt2 = "", opt3 = "", opt4 = "", opt5 = ""):
    dict_ = {"1":opt1, "2":opt2, "3":opt3, "4":opt4, "000":opt5}
    for i, v in dict_.items():
        print(f"\033[0;32m{i} - {v}\033[m")
    line()


