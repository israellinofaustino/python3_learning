import datas
from time import sleep


datas.menu("\033[0;34mMAIN MENU\033[m", center_mine=40)
sleep(1.5)
datas.options("See registered people", "Register new person", "Exit")
datas.verify_file_exist()

while True:
    sleep(1)
    your_option = datas.valid_int_number("\033[0;33mYour choice [options 1, 2 or 3] => \033[m")
    sleep(1.5)
    if your_option == 1:
        datas.show_users()
    elif your_option == 2:
        datas.register_user()
    elif your_option == 3:
        sleep(0.5)
        datas.menu("\033[0;31mLogout of the system, bye.\033[m", quant1=40, quant2=40, center_mine=47)
        break