def player(name, goals):
    if name == '':
        name = '<unknown>'
    if goals == '':
        goals = 0
    if goals != int:
        goals = 0
    return f"The player {name} scored {goals} goal(s)."


name = str(input("Name of the Footboll Player => ")).strip()
goals = input("How many goals? => ").strip()

print(player(name, goals))
