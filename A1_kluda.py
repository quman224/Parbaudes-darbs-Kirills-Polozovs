skaits = 0

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        dalas = rinda.split()
        if any(d.strip("[]:") == "WARNING" for d in dalas[:4]):
            skaits = skaits + 1

print("Atrasts:", skaits)
