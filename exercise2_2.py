import math
# lasketaan suorakulmaisen kolmion hypotenuusa käyttäjältä pyydettyjen kateettien suhteen.
# pyydetään suorakulmaisen kolmion kateetit.
cath_a = input("Anna kolmion ensimmäinen kateetti:\n")
cath_a = float(cath_a)

cath_b = input("Anna kolmion toinen kateetti:\n")
cath_b = float(cath_b)

# hypotenuusa c = sqrt a^2+b^2
hypotenuse = math.sqrt(cath_a ** 2 + cath_b ** 2)
hypotenuse = round(hypotenuse, 2)

print(f"Hypotenusan pituus: {hypotenuse} m")
