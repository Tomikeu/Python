n = input("Jak se jmenuješ ? (Napiš pouze křestní jmeno)\n")
i = ["Tomas", "Tomáš", "Matěj", "Matej", "Lukas", "Lukáš", "Matyas", "Matyáš", "Daniel", "Tobias", "Tobiáš", "Samuel", "Tadeas", "Tadeáš", "Jonas", "Jonáš", "Ondřej", "Ondrej"]
o = ["Honza", "Vojta", "Zuzana", "Magdalena", "Majda", "Amáta", "Amata", "Albína", "Albina", "Ariana", "Adéla", "Adela", "Alžběta", "Alzbeta", "Ondra"]
e = ["Jakub", "Jan", "Adam", "Zikmund", "Adolf", "Albert", "Tibor"]
petr = ["Petr"]
u = ["Vojtech"]
eu = ["Vítek", "Vitek"]

while True:
    if n in i:
        print("Vítej " + n + "i")
        break
    elif n in o:
        pismena = n.split()
        nove_pismeno = [pismeno[:-1] + "o" if pismeno.endswith("a") else pismeno for pismeno in pismena]
        novy_text = " ".join(nove_pismeno)
        print("Vítej " + novy_text)
        break
    elif n in e:
        print("Vítej " + n + "e")
        break
    elif n in petr:
        novy_text = n.replace("r", "ř")
        print("Vítej " + novy_text + "e")
        break
    elif n in u:
        print("Vítej " + n + "u")
        break
    elif n in eu:
        novy_text = n.replace("e", "")
        print("Vítej " + novy_text + "u")
        break
    else:
        
        add = input("Omlouvám se, vaše jméno není v databázi, chcete ho přidat ?\n")
        if add.lower() in ["ano", "jo"]:
            novy = input("Jelikož nejsem člověk potřebuji poradit.\nPokud vaše jméno oslovíte (Ahoj, jmeno) jaké je písmeno na konci\n Pokud i - napište i\nPokud o - napište o\nPokud e - napište e\n Pokud u - napište u\nPokud ani jedno napiš end\n")
            if novy == "i":
                i.append(n)
            elif novy == "o":
                o.append(n)
            elif novy == "e":
                e.append(n)
            elif novy == "u":
                u.append(n)
            elif novy == "end":
                print("Konec")
            else:
                print("Zkuste to znovu.")
        elif add.lower() in ["ne", "nechci"]:
            print("Dobře, užíjte si kalkulačku.")
            break
        else:
            print("Něco je špatně")
