first_term = int(input('Write the first term: '))
reason_ap = int(input('Write the reason for arithmetic progression: '))
user_terms = int(input('How many terms do you want see? => '))
term = first_term
count = 1
total = 0
upper = 10

while upper != 0:
    total = total + upper
    while count <= total:
        print(term, end=' -> ')
        term += reason_ap
        count += 1
    print('PAUSE')
    upper = int(input('How many terms do you want to show more? => '))
print(f'Progression finished with {total} terms shown.')
