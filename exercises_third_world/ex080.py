list_n = []

for count in range(0, 5):
    number = int(input("Write a number => "))
    if count == 0 or number > list_n[-1]:
        list_n.append(number)
        print(f"The number {number} has been added to the end of the list.")
    else:
        position = 0
        while position < len(list_n):
            if number <= list_n[position]:
                list_n.insert(position, number)
                print(f"Added at position {position} of list.")
                break
            position += 1
print('-=' * 30)
list_n.sort()
print(f"The values entered in order were => {list_n}")
