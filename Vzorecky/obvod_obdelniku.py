#Přivítání
print("Vítejte v aplikaci pro výpočty.")

#Napsaní čisla a, b
a = input("Délka strany a\n")
b = input("Délka strany b\n")

#Přeměna na int
a = int(a)
b = int(b)

#Výpočet
if a>0 and b>0:
    v = (2 * (a + b))
    v = str(v)
    c = print("Výsledek je " + v)
else:
    print("Něco je špatně")