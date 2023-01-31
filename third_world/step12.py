list_n = [2, 3, 5, 7, 1, 9, 10]
list_num = []

a = [2, 4, 6, 7, 8]
b = a[:]
b[2] = 9
print(f'List A => {a}')
print(f'List B => {b}')

for count in range(0, 5):
    list_num.append(int(input('Write a value: ')))

for c, n in enumerate(list_num):
    print(f'Na posição {c} encontrei o valor {n}')

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
