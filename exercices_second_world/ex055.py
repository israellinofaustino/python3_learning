greater_weight = 0
lower_weight = 0

for people in range(1, 6):
    weight = float(input(f'Write a {people}° weight: '))
    if people == 1:
        greater_weight = weight
        lower_weight = weight
    else:
        if weight > greater_weight:
            greater_weight = weight
        if weight < lower_weight:
            lower_weight = weight
print(f'The biggest weight is {greater_weight :.2f}Kg')
print(f'The smallest weight is {lower_weight :.2f}Kg')
