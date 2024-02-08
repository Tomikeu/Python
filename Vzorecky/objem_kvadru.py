#Přivítaní 
print("Vítejte v aplikaci pro výpočty.")

#Napisaní čísla r
a = input("Napiš číslo a\n")
a = int(a)
b = input("Napiš číslo b\n")
b = int(b)
c = input("Napiš číslo c\n")
c = int(c)

#Výpočet
if a>0:
    v = (a * b * c)
    v = str(v)
    c = print("Výsledek je " + v)
else:
    print("Něco je špatně")