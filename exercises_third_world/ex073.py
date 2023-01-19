times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
         'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG',
         'Botafogo', 'Santos', 'Goiás', 'Red Bull Bragantino', 'Coritiba',
         'Cuiabá', 'Ceará', 'Atlético-GO', 'Chapecoense', 'Juventude')

print('-=' * 90)
print(f'The top 5 football teams in the table are => {times[:5]}')
print('-=' * 90)
print(f'The last 4 ranked are => {times[-4:]}')
print('-=' * 90)
print(f'Football teams in alphabetical order => {sorted(times)}')
print('-=' * 90)
print(f"The Ceará team is in the position => {times.index('Ceará')+1}")
