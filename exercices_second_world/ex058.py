import random
import emoji

machine_choice = random.randint(0, 10)
player_choice = 0
count = 0

print('I just thought of a number between 0 and 10, try to guess it.'.upper())

if machine_choice == 0:
    player_choice = 1
while player_choice != machine_choice:
    player_choice = int(input('Which number the computer chose? => '))
    if player_choice < machine_choice:
        print(emoji.emojize('Not yet, try a upper number! :sad_but_relieved_face:'))
    else:
        print('Try a less number!')
    count += 1

print('-=' * 30)
print(emoji.emojize(f'YEEEEES, YOU WIN! The computer chose {machine_choice} and you {player_choice} :grinning_cat:'))
print(emoji.emojize(f'You tryed to guess {count} times :grinning_face_with_smiling_eyes:'))
print('-=' * 30)
