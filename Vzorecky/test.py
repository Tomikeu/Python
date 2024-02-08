"""
text = "ahoj ahoj ahoj"
# Zjistíme index prvního výskytu slova "ahoj"
index_1 = text.find("ahoj")
# Zjistíme index druhého výskytu slova "ahoj"
index_2 = text.find("ahoj", index_1 + 1)
# Zjistíme index třetího výskytu slova "ahoj"
index_3 = text.find("ahoj", index_2 + 1)
# Nahradíme pouze třetí výskyt slova "ahoj" za jiný text
if index_3 != -1:
    text = text[:index_3] + "novy_text" + text[index_3 + len("ahoj"):]
print(text)
"""
text = "Honza Vojta Zuzana Magdalena Majda Amáta Amata Albína Albina Ariana Adéla Adela Alžběta Alzbeta Ondra"

# Rozdělíme text na slova
words = text.split()

# Nahradíme poslední výskyt písmene "a" ve každém slově
new_words = [word[:-1] + "o" if word.endswith("a") else word for word in words]

# Sestavíme zpět text
new_text = " ".join(new_words)

print(new_text)