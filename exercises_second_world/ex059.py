from time import sleep

n1 = float(input('Write the first number: ').strip())
n2 = float(input('Write the second number: ').strip())

while n1 != '' and n2 != '':
    sleep(2)
    print('-=' * 10)
    print('[1] - Sum')
    print('[2] - Mult')
    print('[3] - Upper')
    print('[4] - New Numbers')
    print('[5] - Exit')
    print('-=' * 10)
    sleep(1)
    user_choice = int(input('What is your choice? => ').strip())
    print('-=' * 20)
    if user_choice == 1:
        print(f'The sum of values {n1 :.2f} and {n2 :.2f} = {n1 + n2 :.2f}')
    elif user_choice == 2:
        print(f'The mult of values {n1 :.2f} and {n2 :.2f} = {n1 * n2 :.2f}')
    elif user_choice == 3:
        if n1 > n2:
            print(f'Between {n1} and {n2} the largest num is {n1 :.2f}')
        elif n2 > n1:
            print(f'Between {n1} and {n2} the largest num is {n2 :.2f}')
        else:
            print(f'Number {n1} and {n2} is same.')
    elif user_choice == 4:
        print('Write your new numbers below!')
        sleep(2)
        print('-=' * 15)
        n1 = float(input('Write the first number: '))
        n2 = float(input('Write the second number: '))
    elif user_choice == 5:
        print('Finalizing the software...')
        sleep(2)
        break
    else:
        print('Invalid option, try again.')
