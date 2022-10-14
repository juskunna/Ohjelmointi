import math

# Lasketaan hedelmämuuttujille arvot
# Ensin yhden kirsikan arvo
cherry = (2 + (2 * 2) + 2 - 2 - 2) / 2

apple = (math.sqrt(3 + 10 - 4) / 3) + ((math.pow(5, 3) - 5) / 20) + 3
orange = apple - 9

# yhden banaanin arvo
banana = ((cherry * 2) - 10) / 3

pear = (banana * 3) - 8

# lopuksi hedelmäsalaatin arvo
fruitsalad = apple - (banana * 2) + (orange * 2) * (pear + cherry)
fruitsalad = int(fruitsalad)

print(f"Vastaus: {fruitsalad}")

