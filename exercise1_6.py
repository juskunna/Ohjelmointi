cents = input("Anna 1-100 senttiä:\n")
cents = int(cents)

cents_fifty = cents // 50
change = cents % 50
print(f"50 snt kolikoita {cents_fifty} kpl")

cents_twenty = change // 20
change = change % 20
print(f"20 snt kolikoita {cents_twenty} kpl")

cents_ten = change // 10
change = change % 10
print(f"10 snt kolikoita {cents_ten} kpl")

cents_five = change // 5
change = change % 5
print(f"5 snt kolikoita {cents_five} kpl")

cents_two = change // 2
change = change % 2
print(f"2 snt kolikoita {cents_two} kpl")

cents_one = change // 1
print(f"1 snt kolikoita {cents_one} kpl")
