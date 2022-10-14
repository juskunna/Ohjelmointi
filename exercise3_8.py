# Pyydetään ostosten kokonaissumma euroina
price = input("Anna ostosten loppusumma:\n")
price = int(price)

# Kysytään onko käyttäjä opiskelija? k/e
is_student = input("Oletko opiskelija? k/e\n")
student = None

if is_student == "k":
    student = True

elif is_student == "e":
    student = False

# Onko käyttäjä kanta-asiakas? k/e
is_regular = input("Oletko kanta-asiakas? k/e\n")
regular = None

if is_regular == "k":
    regular = True

elif is_regular == "e":
    regular = False

# Jos kanta-asiakas paljonko pisteitä
if regular:
    customer_points = input("Ilmoita kanta-asiakaspisteidesi määrä:\n")
    customer_points = int(customer_points)


# Onko alennuskoodia FALL22 tai BK2SCHOOL
discout_code = input("Alennuskoodi?\n")

# jos FALL22
    #  price = price * 0.9
if discout_code == "FALL22":
    price = price * 0.9

# jos BK2SCHOOL
    # jos opiskelija
        # price = price * 0.8
if student:
    if discout_code == "BK2SCHOOL":
        price = price * 0.8

# jos kanta-asiakas + pisteitä
    # lisätään uudet pisteet, 100 per 10€
    # pienennetään loppusummaa, 5€ per 1000 pistettä

if regular:
    if customer_points > 0:
        customer_points += (price // 10) * 100
        price -= (customer_points // 1000) * 5

# jos loppusumma <= 99€ lisätään postimaksu 7.95€
if price < 99:
    price += 7.95
    print(f"Ostostesi loppusumma on: {price} €")

# muuten tulostetaan loppusumma
else:
    print(f"Ostostesi loppusumma on: {price} €")