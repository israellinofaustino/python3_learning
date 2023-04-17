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
print(f"{'cod':<4} {'name':<8} {'goals'} {'total goals':>38}")
print('-' * 60)
for i in enumerate(players):
    print(f"{i[0]:<4} {i[1]['name']:<8} {i[1]['goals']} {i[1]['total_goals']:>25}")

print('-=' * 30)

while True:
    quest = int(input("Show data of which player? (999 to end) => "))
    if quest == 999:
        break
    print('-=' * 20)
    print(f" -- PLAYER SURVEY {players[quest]['name']}")
    print('-=' * 20)
    for position, goals in enumerate(players[quest]['goals']):
        print(f"     In game {position + 1} scored {goals} goals.")
    print('-=' * 20)
