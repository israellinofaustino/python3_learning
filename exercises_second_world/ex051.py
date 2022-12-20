print('-=' * 19)
print('10 Terms of an Arithmetic Progression')
print('-=' * 19)

first_term = int(input('First Termo: '))
reason = int(input('Reason: '))
tenth = first_term + (10 - 1) * reason

for c in range(first_term, tenth + reason, reason):
    print(c, end=' => ')
print('END')
