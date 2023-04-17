players = list()
player = dict()
goals = list()

while True:
    player['name'] = str(input("Name of player: "))
    many_games = int(input(f"How many games did the {player['name']} play? "))
    for c in range(0, many_games):
        goal = int(input(f"How many goals in match {c+1}? => "))
        goals.append(goal)
    player['goals'] = goals[:]
    goals.clear()
    player['total_goals'] = sum(player['goals'])
    players.append(player.copy())

    question = str(input("Do you want continue? [Y/N] => ")).strip().upper()[0]
    while question != 'Y' and question != 'N':
        print("ERROR! Please write just Y or N.")
        question = input("Do you want continue? [Y/N]: ").strip().upper()[0]
    if question == 'N':
        break


print('-=' * 30)
print('cod ', end='')
for i in player.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 60)
for k, v in enumerate(players):
    print(f"{k:>3} ", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print('-=' * 30)

while True:
    quest = int(input("Show data of which player? (999 to end) => "))
    if quest == 999:
        break
    if quest >= len(players):
        print(f"ERROR! There is no player with code {quest}.")
    else:
        print('-=' * 20)
        print(f" -- PLAYER SURVEY {players[quest]['name']}")
        print('-=' * 20)
        for position, goals in enumerate(players[quest]['goals']):
            print(f"     In game {position + 1} scored {goals} goals.")
        print('-=' * 20)
