import math

# pyydetään käyttäjältä 3 sivun pituutta
side_a = input("Anna särmiön ensimmöisen sivun pituus:\n")
side_a = float(side_a)

side_b = input("Anna särmiön toisen sivun pituus:\n")
side_b = float(side_b)

side_c = input("Anna särmiön kolmannen sivun pituus:\n")
side_c = float(side_c)

# lasketaan tilavuus
cuboid_volume = side_a * side_b * side_c

# tulos
print(f"Särmiön tilavuus: {cuboid_volume} m3")

# pyydetään pallon säde
sphere_radius = input("Anna pallon säde:\n")
sphere_radius = float(sphere_radius)

# lasketaan tilavuus, pyöristetään 2 desimaaliin
sphere_volume = (4/3) * math.pi * (sphere_radius ** 3)
sphere_volume = round(sphere_volume, 2)

# tulos
print(f"Pallon tilavuus: {sphere_volume} m3")
