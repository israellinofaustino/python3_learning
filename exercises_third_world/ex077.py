words = ('LEARN', 'PROGRAM', 'LANGUAGE', 'PYTHON', 'COURSE', 'FREE',
         'STUDY', 'PRACTICE', 'WORK', 'MARKET', 'PROGRAMMER', 'FUTURE')

for word in words:
    print(f'\nIn the word {word.upper()} we have => ', end='')
    for letters in word:
        if letters.upper() in 'AEIOU':
            print(letters, end=' ')
