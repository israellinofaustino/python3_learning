list_n = [2, 3, 5, 7, 1, 9, 10]
list_num = []
fruit_list = ["blackberry", "melon", "melon", "pear"]
clear_list = ["Male", "Female", "Age", "DTB", "location", "Email", "Phone"]

clear_list.clear()
print(clear_list)

fruit_list.remove("melon")
fruit_list.pop(0)
fruit_list.pop()
print(fruit_list)

del list_n[6]
print(list_n)

list_n.insert(0, 1)
list_n.insert(3, 4)
print(list_n)

list_n[1:2] = 22, 23, 24, 25
print(list_n)
list_n[1:4] = 97, 96, 95
print(list_n)

list_test = ["text", 111, True, False, 1.9]
print(type(list_test))

thislist = ["coconut", "banana", "cherry"]
thislist.extend(fruit_list)

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
else:
    print("I did not find 'apple' in the list :(")
    print(thislist)

a = [2, 4, 6, 7, 8]
b = a[:]
b[2] = 9
print(f'List A => {a}')
print(f'List B => {b}')

for count in range(0, 5):
    list_num.append(int(input('Write a value: ')))

for possition, number in enumerate(list_num):
    print(f'Na posição {possition} encontrei o valor {number}')

list_n.sort(reverse=True)
print(list_n)
list_n.reverse()
print(list_n)
list_n.append(11)
print(list_n)
list_n.insert(0, 0)
print(list_n)

if 5 in list_n:
    list_n.pop()
    print(list_n)
else:
    print('number 5 not found :(')
