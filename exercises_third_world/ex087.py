matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
even = 0
column_three = 0
max_second_line = []

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Write a number to [{l}, {c}] => "))
        if matriz[l][c] % 2 == 0:
            even += matriz[l][c]
        column_three = matriz[0][1] + matriz[1][1] + matriz[2][1]
        max_second_line = matriz[1][0], matriz[1][1], matriz[1][2]
print("-=" * 15)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print("-=" * 15)
print(f"The sum of even values is => {even}")
print(f"The sum of the values in the second column is => {column_three}")
print(f"The largest value in the second row is => {max(max_second_line)}")
