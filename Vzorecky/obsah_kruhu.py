#Přivítaní 
print("Vítejte v aplikaci pro výpočty.")

#Napisaní čísla r
a = input("Napiš číslo r\n")
a = int(a)

#Výpočet
if a>0:
    v = (3.14 * a**2)
    v = str(v)
    c = print("Výsledek je " + v)
else:
    print("Něco je špatně")