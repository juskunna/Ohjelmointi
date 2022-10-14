# Pyydetään käyttäjältä lähetyksen tyyppi kirje/paketti.
post_type = input("Oletko lähetys kirje vai paketti? k/p\n")

# Jos kirje, kysytään mahtuuko postilaatikkoon.
if post_type == "k":
    post_size = input("Mahtuuko lähetys postilaatikkoon? k/e\n")

# Pyydetään lähetyksen paino.
post_weight = input("Anna lähetyksen paino:\n")
post_weight = int(post_weight)

post_fare = 0

# Painon mukaiset lisämaksut, per täydet 100g.
# Kirje 200-500g 4snt, >500g 7snat.
if post_type == "k" and 200 <= post_weight <= 500:
    post_fare = 0.50 + (post_weight // 100 * 0.04)

elif post_type == "k" and post_weight > 500:
    post_fare = 0.50 + (post_weight // 100 * 0.07)

elif post_type == "k":
    post_fare = 0.50

# Paketti 200-500g 8snt, >500g 14snt.
if post_type == "p" and 200 <= post_weight <= 500:
    post_fare = 2 + (post_weight // 100 * 0.08)

elif post_type == "p" and post_weight > 500:
    post_fare = 2 + (post_weight // 100 * 0.14)

elif post_type == "p":
    post_fare = 2

# Tarkistetaan tuleeko ison kirjeen lisämaksu, paino yli 500g eikä mahdu postilaatikkoon
if post_weight > 500 and post_size == "e":
    post_fare = post_fare + 2

# Tulostetaan lopullinen postimaksu.
print(f"Lähetyksesi postimaksu on: {post_fare} €")
