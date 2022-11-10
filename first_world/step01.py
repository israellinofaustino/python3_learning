n1 = int(input('Write a value: '))
n2 = int(input('Write more one value: '))

sum = n1 + n2
print(f'The sum between {n1} and {n2} is => {sum}')

text = input('Write something: ')

print(f'The primitive type of this value is => {type(text)}')

print(f'Is it a string? {text.isalpha()}')

print(f'Is it a number or text? {text.isalnum()}')

print(f'Is it numeric? {text.isnumeric()}')

print(f'All letters are capitalized? {text.isupper()}')

print(f'Is it a number? {text.isdigit()}')

print(f'Are all letters lowercase? {text.islower()}')

print(f'What was typed is only spaces? {text.isspace()}')

print(f'Is it a title? {text.istitle()}')
