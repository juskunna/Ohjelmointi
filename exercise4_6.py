# Kysy ulkolämpötila
temperature = input("Anna ulkolämpötila:\n")
temperature = int(temperature)

# ja kosteusprosentti
humidity = input("Anna ilman kosteusprosentti:\n")
humidity = int(humidity)

# luodaan tarvittavat boolean muuttujat
freezing = False
heatwave = False
raining = False
hailstorm = False

# jos lämpötila < 0, freezing = True
if temperature < 0:
    freezing = True

# jos kosteus > 80, raining = True,
if humidity > 80:
    raining = True

# paitsi jos lämpötila < -20, silloin hailstorm = True
if humidity > 80 and temperature < -20:
    hailstorm = True

# jos lämpötila > 20, heatwave = True
if temperature > 20:
    heatwave = True

# tulosta lämpötila ehdoilla
# freezing = true, "Pakkasta."
# raining = true, "Sataa."
# hailstorm = true, "Sataa rakeita!"
# heatwave = true, "Helleaalto!"
# raining ja heatwave = true, "Kosteaa ja tukalaa."

print(f"Lämpötila on {temperature}C")

if raining and heatwave:
    print("Kosteaa ja tukalaa.")

elif hailstorm:
    print("Sataa rakeita!")

elif freezing:
    print("Pakkasta.")

elif raining:
    print("Sataa.")

elif heatwave:
    print("Helleaalto!")
