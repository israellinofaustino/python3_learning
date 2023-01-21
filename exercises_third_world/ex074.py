from random import randint

n_list = (randint(1, 10), randint(1, 10), randint(1, 10),
          randint(1, 10), randint(1, 10))

print(f'The drawn values were => {n_list}')
print(f'The > value is: {max(n_list)} and the < is: {min(n_list)}')
