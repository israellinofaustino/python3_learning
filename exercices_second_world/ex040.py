grade1 = float(input('Write your first grade: '))
grade2 = float(input('Write your second grade: '))

averge = (grade1 + grade2) / 2

print('-=-' * 10)
if averge < 5:
    print('Disapproved!'.upper())
elif averge >= 5 and averge <= 6.9:
    print('Recuperation!'.upper())
elif averge >= 7:
    print('Approved!'.upper())
print('-=-' * 10)
print(f'Your averge is {averge}')
