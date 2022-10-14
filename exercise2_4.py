# lasketaan polttoaineen kokonaiskulutus.

# maantie ja kaupunkiajon kilometrit
distance_road = input("Maantie-ajon kilometrit:\n")
distance_road = float(distance_road)

distance_city = input("Kaupunki-ajon kilometrit:\n")
distance_city = float(distance_city)

# maantie kulutus 5,1l/100km ja kaupunkiajon 7,5l/100km
consumption_road = distance_road * (5.1 / 100)
consumption_city = distance_city * (7.5 / 100)

consumption_total = consumption_road + consumption_city
consumption_total = round(consumption_total, 2)

print(f"Kulutus: {consumption_total} l")
