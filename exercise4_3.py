# Tallennetaa teksti muuttujaan ja tulostetaan.
text = "The quick brown fox jumps over the lazy dog. That \
sentence contains every letter in the English alphabet. Neat!"

print(text)

# Korvataan merkkijonossa 'text' sana 'fox' sanalla 'duck'.
text = text.replace("fox", "duck")

print(text)

print()

# Pyydetään merkkijonosta 'text' poistettava sana.
word = input("Anna poistettava sana:\n")

# Jos sana löytyy poistetaan se
if word in text:
    text = text.replace(word, "")
    print(text)

# Jos ei tulostetaan ilmoitus siitä.
else:
    print("Sanaa ei löytynyt.")

print()

# Lasketaan merkkijonon pituus.
text_length = len(text)

print(f"Merkkejä: {text_length}\n")

# Lasketaan myös sanojen määrä.
words = text.split()
words_num = len(words)

print(f"Sanoja: {words_num}\n")

# Korvataan merkkijonon pisteet rivinvaihdoilla.
text = text.replace(".", "\n")
print(text)

print()

# Pyydetään käyttäjältä merkkijono ja tarkistetaan sen pituus.
usertext = input("Anna jokin lause:\n")
usertext_lenght = len(usertext)

# Jos merkkijono 20 merkkiä tai alle tulostetaan merkkijonon sellaisenaan.
if usertext_lenght <= 20:
    print(usertext)

else:
    subtext = usertext[0:20]
    print(subtext + "" + "...")
