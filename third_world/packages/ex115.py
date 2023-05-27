import datas
from time import sleep


datas.line(50)
print(f"{'MENU PRINCIPAL':^50}")
datas.line(50)
sleep(1.5)
print("1 - Ver pessoas cadastradas")
sleep(1)
print("2 - Cadastrar nova pessoa")
sleep(1)
print("3 - Sair do sistema")
sleep(1)

datas.line(50)

datas.verify_file_exist()

while True:
    sleep(1)
    your_option = datas.valid_int_number("Sua escolha [opções 1, 2 ou 3] => ")
    sleep(1.5)
    if your_option == 1:
        file = open("people.txt", "r")
        datas.line(50)
        print(file.read())
        datas.line(50)
    elif your_option == 2:
        datas.line(50)
        name = str(input("Whats your name? ").strip())
        age = datas.valid_int_number("How old are you? ")
        datas.line(50)
        file = open("people.txt", "a")
        file.write(f"\n{name}, ")
        file.write(str(age))
        file.close
    elif your_option == 3:
        datas.line(50)
        sleep(1)
        print(f"{'Saindo do sistema, até logo.':^50}")
        sleep(1)
        datas.line(50)
        break
