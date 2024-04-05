fruits = ["0. apple", "1. banana", "2. cherry", "3. kiwi", "4. mango"]
newlist = []

print("--------------------------------------------------------------")
print(fruits)
print("--------------------------------------------------------------")


while True:
    x = int(input("Napiš číslo o jaké zboží máte zájem: "))
    if x<len(fruits) and 0<x:
        newlist.append(fruits[x])
        fruits.pop(x)

        print("--------------------------------------------------------------")
        print("Váš košík: ", newlist)
        print("Dostupné zboží: ", fruits)
        print("--------------------------------------------------------------")
    
        z = input("Máte eště o něco zájem? (Ano/Ne): ")
        if z.lower() != "ano":
            break
    else:
        break