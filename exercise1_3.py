# Tehdään ohjelma joka kertoo matkan kulutuksen annetun pituuden perusteella.

trip = input("Anna matkan pituus:\n")
trip = float(trip)

fuel = 6.5/100

consumption = trip * fuel
consumption = round(consumption, 1)

print(f"Kulutus: {consumption} l")
