def terreno(width, length):
    line()
    calculate = width * length
    return calculate


def line():
    print('-=' * 35)


line()
print(f'{"Land Control":^70}')
line()
widt = float(input("Width (m): "))
lengt = float(input("Length (m): "))

result = terreno(widt, lengt)
print(f"{f'The land area of {widt:.2f} x {lengt:.2f} is {result:.2f}m2.':^70}")
line()
