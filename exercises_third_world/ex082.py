list_of_numbers = []
list_of_even = []
list_of_odd = []

while True:
    user_num = int(input("Write a number => "))
    list_of_numbers.append(user_num)

    if user_num != 0:
        if user_num % 2 == 0:
            list_of_even.append(user_num)
        else:
            list_of_odd.append(user_num)

    question = input("Do you want continue? [Y/N] => ").strip().upper()[0]
    if "N" in question:
        break

print(f"The complete list is: {list_of_numbers}")
print(f"The even list is: {list_of_even}")
print(f"The odd list is: {list_of_odd}")
