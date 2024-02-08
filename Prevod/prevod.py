print("---------------------------------------")

type = input("Zadejte typ adresy (decimální/binární): \n")

adresa = input("Zadejte IP adresu: \n")

#nastav aby te to nepustilo kdyz napises 256.256.256.256
#převod
if adresa < 45:
    if type.lower() == "decimální" or type.lower() == "dec" or type.lower() == "decimalni":
        bin = '.'.join(format(int(x), '08b') for x in adresa.split('.'))
        print("Binární IP adresa: ", bin)
    elif type.lower() == "binární" or type.lower() == "bin" or type.lower() == "binarni":
        dec = '.'.join(str(int(x, 2)) for x in adresa.split('.'))
        print("Decimální IP adresa: ", dec)
    else:
        print("Něco je špatně.")

    #třída
    trida = int(adresa.split('.')[0])
    if 1 <= trida <= 126:
        print("Třída A")
    elif 128 <= trida <= 191:
        print("Třída B")
    elif 192 <= trida <= 223:
        print("Třída C")
    elif 224 <= trida <= 239:
        print("Třída D")
    elif 240 <= trida <= 255:
        print("Třída E")
    else:
        print("Něco je špatně.")
else:
    print("Něco je špatně")