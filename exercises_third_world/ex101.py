from datetime import date


year = date.today().year


def vote(year_born):
    age = year - year_born
    
    if age <= 16:
        print(f"{age} years old. You can't vote yet (DENIED).")
    elif age > 16 and age < 18 or age > 60:
        print(f"{age} years old. Your vote is OPTIONAL.")
    elif age >= 18 and age <= 60:
        print(f"{age} years old. Your vote is MANDATORY.")


year_born = int(input("What's your year of birthday? "))
vote(year_born)
