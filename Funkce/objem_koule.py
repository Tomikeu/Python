def objem_koule(r):
    r = int(r)
    v = 4/3 * 3.14 * r ** 3
    v = float(v)
    return v

x = input("Zadejte proměnou r\n")

print("Výsledek je: ", objem_koule(x))