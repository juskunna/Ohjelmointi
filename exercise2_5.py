import random

# Arvotaan luku 1 ja 10 väliltä
number1 = random.randint(1, 10)
print(f"Arvottu luku: {number1}\n")

# Arvotaan sivut 2 ja 10 väliltä
side1 = random.randint(2, 10)
print(f"Arvottu 1 sivu: {side1}\n")

side2 = random.randint(2, 10)
print(f"Arvottu 2 sivu: {side2}\n")

# Lasketaan suorakulmion pinta-ala arvottujen sivujen avulla
area = side1 * side2
print(f"Arvotuista sivuista laskettu pinta-ala: {area}\n")
