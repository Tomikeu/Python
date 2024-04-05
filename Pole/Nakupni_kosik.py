fruits = ["0. apple", "1. banana", "2. cherry", "3. kiwi", "4. mango"]

newlist = []
newlist = (str(newlist))

print(fruits)

while True:
    x = input("Napiš číslo o jaké zboží máte zájem: ")
    x = (int(x))

    newlist.append(fruits[x])
    fruits.pop(x)

    print(newlist)
    print(fruits)
    
    z = input("Máte eště o něco zájem ?")
    if z == "Ano":
        print("Dobře")
    else:
        break