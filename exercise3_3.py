# Ohjelma joka kysyy käyttäjältä viikon työtuntimäärän sekä tuntipalkan.
# Lasketaan niiden perustella viikon ansiot.

workhours = input("Syötä viikon työtunnit:\n")
workhours = float(workhours)

hourly_wage = input("Syötä tuntipalkkasi:\n")
hourly_wage = float(hourly_wage)

salary_week = 0
salary_base = 0
salary_overtime = 0

# jos tunnit ovat 40 tai vähemmän lasketaan tunnit kertaa tuntipalkka ja tulostetaan
if workhours <= 40:
    salary_week = workhours * hourly_wage
    salary_week = round(salary_week, 2)


# jos tehty ylitöitä, tunnit yli 40, lasketaan peruspalkka ensimmäiselle 40 tunnille ja
# ylityöpalkka ylimeneville tunneille 50% korotettuna jotka lasketaan yhteen viikkopalkaksi.
else:
    salary_base = 40 * hourly_wage

    salary_overtime = (workhours - 40) * hourly_wage * 1.5

    salary_week = salary_base + salary_overtime
    salary_week = round(salary_week, 2)

print(f"Viikon ansiosi ovat: {salary_week}")