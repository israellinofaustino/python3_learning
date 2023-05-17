print("-=" * 25)
print(f'{"HELP SYSTEM PyHELP":^50}')
print("-=" * 25)

while True:
    print("-=" * 25)
    command = str(input("Function ou Library (exit[] to stop)=> ")).strip().lower()
    print("-=" * 25)
    if command == 'exit[]':
        print("Thanks, see you!")
        break
    print(help(command))
