r1 = float(input('First segment: '))
r2 = float(input('Second segment: '))
r3 = float(input('Third segment: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('The above segments CAN FORM a triangle, ', end='')
    if r1 == r2 == r3:
        print('EQUILATERAL')
    elif r1 != r2 != r3 != r1:
        print('SCALENE')
    else:
        print('ISOSCELES')
else:
    print('The above segments CANNOT form a triangle!')
