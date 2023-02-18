num_list = []

while True:
    number = int(input("Write a number => "))
    num_list.append(number)
    question = input("Du you want continue? [Y/N] => ").strip().upper()[0]
    if question == "N":
        break

print('-=' * 30)
if 5 in num_list:
    print("The value 5 is part of the list.")
else:
    print("The value 5 was not found in the list.")

print(f"You wrote {len(num_list)} elements.")
num_list.sort(reverse=True)
print(f"The values in descending order are => {num_list}")
