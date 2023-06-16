from packages import connection, string, numbers


string.title('MENU OPTIONS')
string.options('SHOW USERS', 'REGISTER A NEW USER', 'EDIT A USER', 'DELETE A USER', 'EXIT')


while True:
    your_option = numbers.valid_int_number("\033[0;33mYour choice [options 1, 2, 3, 4 or 000] => \033[m")
    if your_option == 1:
        connection.show_data('people.person')
    elif your_option == 2:
        connection.register_user()
    elif your_option == 3:
        connection.edit_user()
    elif your_option == 4:
        connection.delete_user()
    elif your_option == 000:
        string.title("\033[0;31mLogout of the system, bye.\033[m", quant1=40, quant2=40, center_mine=47)
        break

