# Pyydetään käyttäjältä päivän lämpötila ja tulostetaan vastaus rajaehtojen puitteissa.

temperature = input("Anna päivän lämpötila:\n")
temperature = int(temperature)

if temperature >= 0 and temperature <= 10:
    print("KYLMÄÄ")

if temperature > 10 and temperature <= 15:
    print("KOLEAA")

if temperature > 15 and temperature <=20:
    print("NORMAALI LÄMPÖTILA")

if temperature > 20 and temperature <= 25:
    print("LÄMMINTÄ")

if temperature > 25 and temperature <= 30:
    print("HELLETTÄ")
