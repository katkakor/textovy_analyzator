"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Kateřina Kordiovská
email: kordiovskak@gmail.com
discord: Katerina K#9622

"""

#Vyžádá si od uživatele přihlašovací jméno a heslo,
user = input("Name:")
password = input("Password:")
line = "-" * 40
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}
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
garpike and stingray are also present.'''
]

#zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů
if registered_users.get(user) == password:
#pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,
    print(f"Username", {user})
    print(f"Password", {password})
    print(line)
    print(f"Welcome to the app, {user} \nWe have 3 texts to be analyzed.")
    print(line)
#pokud není registrovaný, upozorni jej a ukonči program
else:
    print(f"username", {user})
    print(f"password", {password})
    print(f"unregistered user, terminating the program..")
    quit()
#Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS:
selected_text = (input(f"Enter a number btw. 1 and 3 to select: "))

#Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí,
#pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.
if selected_text.isnumeric() and int(selected_text) >= 1 and int(selected_text) <=3:
    print(line)
else:
    print("The entered credentials are not right terminating the program")
    quit()

#počet slov
analyzed_text = (TEXTS[int(selected_text) - 1])
lenght = len(analyzed_text.split())
print(f"There are", {lenght}, "words in the selected text.")

#sumu všech čísel (ne cifer) v textu.
spaces = analyzed_text.split()
count = 0
for c in spaces:
    if c.isnumeric():
        count = count + int(c)
print(f"The sum of all the numbers", {count})
              
#počet čísel (ne cifer)   
cnt = 0
for a in spaces:
    if a.isnumeric():
        cnt = cnt + 1
print(f"There are", {cnt}, "numeric strings.")
        
#počet slov psaných velkými písmeny
#počet slov psaných malými písmeny
newstring = ''
count1 = 0
count2 = 0
for a in spaces:
    if (a.isupper()) == True and (a.isalpha()):
        count1 += 1
        newstring += (a.lower())
    elif (a.islower()) == True:
        count2 += 1
        newstring += (a.upper())
print("There are", {count1}, "uppercase words.")
print("There are", {count2}, "lowercase words.")

#počet slov začínajících velkým písmenem
count3 = 0
mezery = analyzed_text.split()
for index, symbol in enumerate(mezery):
    if symbol[0].isupper():
        count3 = count3 + 1
print(f"There are", {count3}, "titlecase words.")


#Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu
# ocisteni slov od carek a tecek 
words = list()
for a in spaces:
    words.append(
        a.strip(".,").lower()
    )
# pridani slov a cetnost slov se stejnym poctem do slovniku 
new_dict = dict()
for x in words:
    if len(x) not in new_dict:
        new_dict[len(x)] = 1        
    else:
        new_dict[len(x)] = new_dict[len(x)] + 1

# serazeni
dict_sorted = sorted(new_dict.items())
print(line)
print("LEN|".ljust(2), "\tOCCURENCES","|NR.".rjust(5))
print(line)
# vypsani cetnosti slov
for index, symbol in dict_sorted:
     print(str(index).rjust(2), "|", symbol*"*", (12-symbol+1)*" ", "|", str(symbol))

