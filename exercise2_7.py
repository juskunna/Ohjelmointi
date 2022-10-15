import math

# Pyydetään käyttäjää antamaan arvot muuttujille a, b ja c. Ratkaistaan niiden avulla toisen asteen yhtälö.
a = input("Anna arvo muuttajalle a:\n")
a = int(a)

b = input("Anna arvo muuttujalle b:\n")
b = int(b)

c = input("Anna arvo muuttujalle c:\n")
c = int(c)

x1 = 0
x2 = 0


    # 2, 4, 4, ei arvoja
    # 2, 6, 0, 2 arvoa
    # 2, -4, 2, 1 arvo
    # toisen asteen yhtälön ratkaisukaava -b +- neliöjuuri (b^2 - 4 * a * c) / 2 * a
try:

    x1 = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

# Juuren otto negatiivisesta vie tuloksen ulos reaalilukualueelta
# joka aiheuttaa virhetilanteen joka napataan ilmoittamaan X:n virheellisiä arvoja.

except ValueError:
    print("X:llä ei ole reaalijuuria.")

else:
    if x1 == x2 and int:
        print(f"X:n arvo on: {x1}")

    else:
        print(f"x1:n arvo on: {x1} ja x2: {x2}")
