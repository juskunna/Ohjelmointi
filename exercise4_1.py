from datetime import date

# Yhdistetään muuttujien päivämäärä, asiakkaan nimi, syntymävuosi ja saldo tiedot yhdeksi muuttujaksi.

today = date.today()
date_text = today.strftime("%d.%m.%Y.")

name = "Testi Henkilöinen"

birthyear = 1982

balance = 1698

print(f"{name} ({birthyear}), saldo: {balance} €, päivitetty {date_text}")