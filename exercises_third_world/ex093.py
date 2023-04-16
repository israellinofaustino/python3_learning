player = dict()
goals = list()

player['name'] = str(input("Name of player: "))
many_games = int(input(f"How many games did the {player['name']} play?"))
for c in range(0, many_games):
    player['goals'] = int(input(f"How many goals in match {c+1}? => "))
    goals.append(player['goals'])
    player['goals'] = goals
    player['total_goals'] = sum(player['goals'])

print('-=' * 30)
print(player)
print('-=' * 30)
for k, v in player.items():
    print(f"The field {k} have the value {v}")
print('-=' * 30)
print(f'Player {player["name"]} played {many_games} games.')
for k, v in enumerate(player['goals']):
    print(f"   => In martch {k+1}, scored {v} goals.")
print(f"It was a total {player['total_goals']} goals.")
