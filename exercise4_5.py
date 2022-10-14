# Tiedustellaan käyttäjältä onko hän opiskelija vai ei
# Kesäloman ulkopuolella oikeus alennettuun hintaan, ei kuut 6, 7, 8.


# kysytään onko käyttäjä opiskelija, käytetään boolean muuttujaa tiedon tallentamiseen.
is_student = input("Oletko opiskelija? (k/e)\n")
student = None

if is_student == "k":
    student = True

else:
    student = False

# kysytään kuukautta mille matka varataan, käytetään boolean muuttujaa kesäloman merkitsemiseen.
month = input("Mille kuukaudelle matka varataan? (1-12)\n")
month = int(month)
summer = None

# Onko kesäkuukausi
if 5 < month < 9:
    summer = True

else:
    summer = False

special_price = None

# jos on opiskelija eikä kesä erikoishinta muutoin normihinta.
if student == True and summer == False:
    special_price = True

else:
    special_price = False

if special_price:
    print("Alennus myönnetty!")

else:
    print("Normaali hinta.")
