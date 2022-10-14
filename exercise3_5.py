# pyydetään käyttäjältä pistemäärä
score = input("Anna pistemäärä:\n")
score = int(score)

# tulostetaan arvosana 0-5 käyttäjän antaman pistemäärän perusteella
# määritetään pistemäärärajat eri arvosanoille

if 0 <= score <= 50:
    print("Arvosana: 0")

elif 51 <= score <= 60:
    print("Arvosana: 1")

elif 61 <= score <= 70:
    print("Arovsana: 2")

elif 71 <= score <= 80:
    print("Arvosana: 3")

elif 81 <= score <= 90:
    print("Arvosana: 4")

elif 91 <= score <= 100:
    print("Arvosana: 5")

# jos pistemäärä ei ole arvosanojen rajojen välissä tulostetaan siitä viesti
else:
    print("Pistemäärä ei ole mahdollinen")
