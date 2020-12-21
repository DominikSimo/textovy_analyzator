TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']

# 1. Uvítanie a kontrola či údaje sedia zo zoznamu registrovaných uživatelov
zoznam = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
while True:
    print("-" * 40)
    print("Welcome to the app. Please log in: ")
    meno = input("Username: ")
    heslo = input("Password: ")
    print("-" * 40)
    if meno in zoznam and heslo == zoznam[meno]:
        print("Correctly entered name and password.")
        break
    else:
        print("Incorrect username or password.Try it again.")

# 2. Výber a úprava textu
print(f"We have {len(TEXTS)} texts to be analyzed.")
while True:
    cislo_textu = input(f"Enter a number btw {len(TEXTS[:1])} and {len(TEXTS)} to select: ")
    if cislo_textu.isnumeric() and len(TEXTS[:1]) <= int(cislo_textu) <= len(TEXTS):
        print("Correctly entered number.")
        break
    else:
        print("Incorrectly entered number."
              f"You must enter a NUMBER btw {len(TEXTS[:1])} and {len(TEXTS)} to select.")

vybrany_TEXT = TEXTS[int(cislo_textu) - 1]
upraveny_TEXT = []
for slovo in vybrany_TEXT.split():
    slovo = slovo.strip('.,')
    upraveny_TEXT.append(slovo)

# 3. Statistiky textu
prve_velke_pismena = []
velke_pismena = []
male_pismena = []
cisla = []
for slovo in upraveny_TEXT:
    if slovo.istitle():
        prve_velke_pismena.append(slovo)
    elif slovo.isupper():
        velke_pismena.append(slovo)
    elif slovo.islower():
        male_pismena.append(slovo)
    elif slovo.isnumeric():
        cisla.append(slovo)

print("-" * 40)
print(f"There are {len(upraveny_TEXT)} words in the selected text.")
print(f"There are {len(prve_velke_pismena)} titlecase words.")
print(f"There are {len(velke_pismena)} uppercase words.")
print(f"There are {len(male_pismena)} lowercase words.")
print(f"There are {len(cisla)} numeric strings.")
print("-" * 40)

# 4. Sloupcový graf
delka_slov = []
for slovo in upraveny_TEXT:
    delka_slov.append(len(slovo))
delka_slov.sort()

for delka in set(delka_slov):
    print(delka, "*" * delka_slov.count(delka), delka_slov.count(delka))

# 5. Součet čísel v textu
soucet_cisel = 0
for cislo in cisla:
    soucet_cisel = soucet_cisel + int(cislo)

print("-" * 40)
print("If we summed all the numbers in this text we would get:", soucet_cisel)
print("-" * 40)
