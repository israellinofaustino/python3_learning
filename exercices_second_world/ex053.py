phrase = input('Write some phrase: ').strip().upper()
words = phrase.split()
phrase_no_spaces = ''.join(words)
invert = phrase_no_spaces[::-1]

print(f'\nThe inverse of {phrase_no_spaces} is {invert}')
if invert == phrase_no_spaces:
    print('This sentence is a PALINDROME')
else:
    print('This sentence is NOT a PALINDROME')
