from time import sleep
students = list()
while True:
    nome = str(input("Name: "))
    note1 = float(input("1º Note: "))
    note2 = float(input("2º Note: "))
    media = (note1 + note2) / 2
    students.append([nome, [note1, note2], media])
    still = input("Do you want continue? [Y/N] => ").strip().upper()[0]
    if still == "N":
        break

print('-=' * 20)
print(f"{'Nº':<4}{'NAME':<10}{'MEDIA':>8}")
print('-' * 50)
for i, student in enumerate(students):
    print(f"{i:<4}{student[0]:<10}{student[2]:>8.1f}")
    sleep(1)
print('-' * 50)

while True:
    specific = int(input("Show which student's grade? (999 to stop) => "))
    if specific == 999:
        break
    if specific <= len(students) - 1:
        print('-=' * 25)
        print(f"{students[specific][0]} notes are {students[specific][1]}")
        print('-=' * 25)
