# Tee ohjelma, joka päättelee käyttäjän syöttämästä
# vuodesta, onko kyseinen vuosi karkausvuosi vai ei.

# kysytään käyttäjältä vuosi
year = input("Anna vuosiluku:\n")
year = int(year)

# Jos vuosiluku on jaollinen 400, kyseessä on aina karkausvuosi.
if year % 400 == 0:
    print("Karkausvuosi.")

# Jos vuosiluku ei ole jaollinen 400 tarkistetaan muut ehdot.
if year % 400 != 0:

    # Jos vuosiluku on jaollinen 100, kyseessa ei ole karkausvuosi.
    if year % 100 == 0:
        print("Ei ole karkausvuosi.")

    # Jos vuosiluku on jaollinen 4, kyseessä on karkausvuosi.
    if year % 4 == 0:
        print("Karkausvuosi.")

    # Muulloin kyseessä ei ole karkausvuosi.
    else:
        print("Ei ole karkausvuosi.")
