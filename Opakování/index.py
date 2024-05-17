import random

# Generování náhodných polí
pole = []
pole1 = []

for i in range(random.randint(1, 10)):
    pole.append(random.randint(1, 10))

for i in range(random.randint(1, 10)):
    pole1.append(random.randint(1, 10))

# Seřazení polí
pole.sort()
pole1.sort()

print("První pole:", pole)
print("Druhé pole:", pole1)

# Porovnání velikosti polí
if len(pole) > len(pole1):
    print("První pole je větší.")
elif len(pole) < len(pole1):
    print("Druhé pole je větší.")
else:
    print("Obě pole mají stejnou velikost.")
