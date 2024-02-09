#Animace
import os 
import sys

def console_frame(output):
	os.system('clear' if os.name == 'posix' else 'CLS')
	sys.stdout.write(output + "\n")
	sys.stdout.flush()

import time
import math

for t in range(50):
	console_frame("\n".join(["*" * (30 + int(30 * math.sin(.1 * x + .1 * t))) for x in range(30)])) # time-varying sine wave
	time.sleep(.04)

n = input("Jak se jmenujete ? (Napiš pouze křestní jmeno)\n")
i = "Tomas Tomáš Matěj Matej Lukas Lukáš Matyas Matyáš Daniel Tobias Tobiáš Samuel Tadeas Tadeáš Jonas Jonáš Ondřej Ondrej"
o = "Honza Vojta Zuzana Magdalena Majda Amáta Amata Albína Albina Ariana Adéla Adela Alžběta Alzbeta Ondra"
e = "Jakub Jan Adam Zikmund Adolf Albert Tibor"
petr = "Petr"
u = "Vojtech"
eu = "Vítek Vitek"

print("--------------------------------")
if n in i:
    print("Vítej v aplikaci pro výpočty " + n + "i")
elif n in o:
    pismena = n.split()
    nove_pismeno = [pismeno[:-1] + "o" if pismeno.endswith("a") else pismeno for pismeno in pismena]
    novy_text = " ".join(nove_pismeno)
    print("Vítej v aplikaci pro výpočty " + novy_text)
elif n in e:
    print("Vítej v aplikaci pro výpočty " + n + "e")
elif n in petr:
    novy_text= n.replace("r", "ř")
    print("Vítej v aplikaci pro výpočty " + novy_text + "e")
elif n in u:
    print("Vítej v aplikaci pro výpočty " + n + "u")
elif n in eu:
    novy_text = n.replace("e", "")
    print("Vítej v aplikaci pro výpočty " + novy_text + "u")
else:
    print("Zkuste to znovu")
print("--------------------------------")

#Výběr
print("Vyberte kalkulačku :")
v = input("1. Klasická kalkulačka\n2. Kalkulačka na výpočet obsahu...\n- ")

#Kalkulačka
if v == "1." or v == "1" or v == "Klasická kalkulačka" or v == "Klasicka kalkulacka":
    x = input("Napiš číslo X\n")
    y = input("Napiš číslo Y\n")
    z = input("Vyber znaménko\n1. Sčítání\n2. Odečítání\n3. Násobení\n4. Dělení\n5. Mocnina\n6. Odmocnina\n")

    x = (int(x))
    y = (int(y))

#Sčítání
    if z == "Sčítání" or z == "1." or z == "1. Sčítání" or z == "1" or z == "scitani":
        m = x
        m += y
        m = (str(m))
        print("Výsledek je " + m)
#Odečítání
    elif z == "Odečítání" or z == "2." or z == "2. Odečítání" or z == "2" or z == "odecitani":
        m = x
        m -= y
        m = (str(m))
        print("Výsledek je " + m)
#Násobení
    elif z == "Násobení" or z == "3." or z == "3. Násobení" or z == "3" or z == "nasobeni":
        m = x
        m *= y
        m = (str(m))
        print("Výsledek je " + m)
#Dělení
    elif z == "Dělení" or z == "4." or z == "4. Dělení" or z == "4" or z == "deleni":
        if y == 0:
            print("y nesmí být 0")
        else:
            m = x
            m /= y
            m = (str(m))
            print("Výsledek je" + m)
#Mocnina
    elif z == "Mocnina" or z == "5." or z == "5. Mocnina" or z == "5" or z == "mocnina":
        m = x
        m **= y
        m = (str(m))
        print("Výsledek je " + m)
#Odmocnina
    elif z == "Odmocnina" or z == "6." or z == "6. Odmocnina" or z == "6" or z == "odmocnina":
        m = x
        m *= 1
        m /= y
        m = (str(m))
        print("Výsledek je " + m)

#Kalkulačna na výpočet obsahu atd..
elif v == "2." or v == "2" or v == "Kalkulačka na výpočet obsahu..." or v == "Kalkulacka na vypocet obsahu..." or v == "Kalkulačka na výpočet obsahu" or v == "Kalkulacka na vypocet obsahu":

    k = input("1. Obsah kruhu\n2. Obsah obdelníku\n3. Obvod obdelníku\n4. Objem kvadru\n")

#Obsah kruku
    if k == "1" or k == "1." or k == "obsah kruhu":
        a = input("Napiš číslo r\n")

        a = int(a)

        if a>0:
            v = 3.14
            v *= a**2
            v = str(v)
            c = print("Výsledek je " + v)
        else:
            print("Něco je špatně.")

#Obsah obdelníku
    elif k == "2" or k == "2." or k == "obsah obdelníku" or k == "obsah obdelniku":
    
        a = input("Délka strany a\n")
        b = input("Délka strany b\n")

        a = int(a)
        b = int(b)

        if a>0 and b>0:
            v = a
            v *= b
            v = str(v)
            c = print("Výsledek je " + v)
        else:
            print("Něco je špatně.")

#Obvod obdelníku
    elif k == "3" or k == "3." or k == "obvod obdelníku" or k == "obvod obdelniku":
        a = input("Délka strany a\n")
        b = input("Délka strany b\n")

        a = int(a)
        b = int(b)

        if a>0 and b>0:
            v = (2 * (a + b))
            v = str(v)
            c = print("Výsledek je " + v)
        else:
            print("Něco je špatně.")

#Objem kvádru
    elif k == "4" or k == "4." or k == "objem kvadru":
        a = input("Napiš číslo a\n")
        b = input("Napiš číslo b\n")
        c = input("Napiš číslo c\n")

        a = int(a)
        b = int(b)
        c = int(c)

        if a and b and c>0:
            v = a
            v *= b
            v *= c
            v = str(v)
            c = print("Výsledek je " + v)
        else:
            print("Něco je špatně.")
    else:
        print("Něco je špatně.")
else:
    print("Něco je špatně.")