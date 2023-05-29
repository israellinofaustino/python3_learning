import datas
from time import sleep


datas.menu("MAIN MENU")
sleep(1.5)
datas.options("See registered people", "Register new person", "Exit")
datas.verify_file_exist()

while True:
    # sleep(1)
    your_option = datas.valid_int_number("Your choice [options 1, 2 or 3] => ")
    # sleep(1.5)
    if your_option == 1:
        datas.show_users()
    elif your_option == 2:
        datas.register_user()
    elif your_option == 3:
        # sleep(1)
        datas.menu("Logout of the system, bye.")
        break