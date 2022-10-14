# Pyydetään käyttäjältä tekstiä ja käännetään se ja tehdään testit tyhjyyteen ja palindromiin.

# Kysytään käyttäjältä teksti.
text = input("Anna jokin teksti:\n")
text = str(text)

# Käännetään se toisinpäin ja tulostetaan.
reversed_text = text[::-1]
print(reversed_text)

# Jos annetaan tyhjä teksti tulostetaan "Antamasi teksti on tyhjä."
if text == "":
    print("Antamasi teksti on tyhjä.")

# Testataan onko teksti palindromi ja tulostetaan Kyllä tai ei.
elif text == reversed_text:
    print("Palindromi: KYLLÄ")

else:
    print("Palindromi: EI")
