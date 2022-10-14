# Pyydetään käyttäjää antamaa rahaa ja ostosten hinta,
# jos rahat eivät riitä pyydetään lisää.
# Jos ollaan vieläkin vajaa kerrotaan rahojen riittämättömyys.

# käyttäjältä pyydettävät muuttujat
money_given = input("Anna rahaa:\n")
money_given = int(money_given)

price = input("Ostosten hinta:\n")
price = int(price)

# tehdään muuttujat vaihtorahoille ja annettujen rahojen summalle
leftover = 0
money_total = 0

# ensin rahat riittävät
if money_given >= price:
    leftover = money_given - price

    print(f"Kiitos. Annetaan takaisin {leftover} €")

# rahat eivät riitä ja pyydetään lisää
else:
    money_more = input("Rahat eivät riitä, anna lisää rahaa:\n")
    money_more = int(money_more)

    money_total = money_given + money_more

# tarkistetaan onko vieläkään tarpeeksi rahaa
    if money_total >= price:
        leftover = money_total - price

        print(f"Kiitos. Annetaan takaisin {leftover} €")
    else:
        print("Sinulla ei ole tarpeeksi rahaa.")
