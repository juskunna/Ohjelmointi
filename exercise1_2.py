# tehdään ohjelma joka pyytää tuotteen hintaa ilman alvia ja laskee sitten alvillisen hinnan ja tulostaa sen.

# input
price = input("Anna tuotteen veroton hinta:\n")
price = float(price)

tax = 1.24

# calculation and output
total = price * tax
total = round(total, 2)
print(f"Verollinen hinta on: {total}€")
