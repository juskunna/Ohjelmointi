# Pyydä käyttäjältä kaksi numeroa ja tulostetaan vain isompi,
# #jos yhtäsuuret tulostetaan "Numerot yhtä suuret".

# Sijoitetaan annetut luvut muuttujiin.
number1 = input("Anna ensimmäinen numero:\n")
number1 = int(number1)

number2 = input("Anna toinen numero:\n")
number2 = int(number2)

# Verrataan annettuja lukuja ja tulostetaan suurempi,
# lukujen ollessa saman suuruiset tulostetaan viesti siitä.

if number1 < number2:
    print(f"Suurempi luku on: {number2}")
elif number1 > number2:
    print(f"Suurempi luku on: {number1}")
else:
    print("Numerot ovat yhtä suuret.")
