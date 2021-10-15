# Teisendab kasutaja poolt kroonides sisestatud summa eurodesse ja väljastab ümardatud tulemuse.

eek = input("Sisesta summa kroonides: ")
calc = int(eek) / 15.6
eur = round(calc)
print("Sul on " + str(eur) + " eurot.")