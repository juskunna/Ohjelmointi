import math

# Pyydetään käyttäjää antamaan arvot muuttujille a, b ja c. Ratkaistaan niiden avulla toisen asteen yhtälö.
a = input("Anna arvo muuttajalle a:\n")
a = int(a)

b = input("Anna arvo muuttujalle b:\n")
b = int(b)

c = input("Anna arvo muuttujalle c:\n")
c = int(c)

# toisen asteen yhtälön ratkaisukaava -b +- neliöjuuri (b^2 - 4 * a * c) / 2 * a
x1 = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
print(f"x1:n arvo on: {x1} ja x2: {x2}")
