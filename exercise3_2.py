# Pyydetään käyttäjältä päivän lämpötila ja tulostetaan vastaus rajaehtojen puitteissa.

temperature = input("Anna päivän lämpötila:\n")
temperature = int(temperature)

if temperature >= 0 and temperature <= 10:
    print("KYLMÄÄ")

elif temperature > 10 and temperature <= 15:
    print("KOLEAA")

elif temperature > 15 and temperature <=20:
    print("NORMAALI LÄMPÖTILA")

elif temperature > 20 and temperature <= 25:
    print("LÄMMINTÄ")

elif temperature > 25 and temperature <= 30:
    print("HELLETTÄ")
