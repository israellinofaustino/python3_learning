first_term = int(input('Write the first term: '))
reason_ap = int(input('Write the reason for arithmetic progression: '))
count = 0

while count <= 10:
    print(first_term, end=' -> ')
    first_term += reason_ap
    count += 1
print('END')
