from datetime import date

actual = date.today().year
born_year = int(input('Write your born year: '))
person_years = actual - born_year

print(f'Quem nasceu em {born_year} tem {person_years} anos em {actual}')

if person_years == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif person_years < 18:
    saldo = 18 - person_years
    print(f'Ainda faltam {saldo} anos para o alistamento')
    ano = actual + saldo
    print(f'Seu alistamento será em {ano}')
elif person_years > 18:
    saldo = person_years - 18
    print(f'Você ja deveria ter se alistado há {saldo} anos')
    ano = actual - saldo
    print(f'Seu alistamento foi {ano}')
    