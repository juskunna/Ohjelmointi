# input in minutes setting type as int
minutes = input("Anna minuutit:\n")
minutes = int(minutes)

#
hours = minutes // 60
remainder = minutes % 60

print(f"{hours}h {remainder}min")

