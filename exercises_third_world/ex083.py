expression = input("Enter the mathematical expression: ")
list_ = []

for simb in expression:
    if simb == '(':
        list_.append('(')
    elif simb == ')':
        if len(list_) > 0:
            list_.pop()
        else:
            list_.append(')')
            break

if len(list_) == 0:
    print("Your expression is CORRECT.")
else:
    print("Your expression is INCORRECT.")
