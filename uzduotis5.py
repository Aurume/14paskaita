# Išsaugokite visą tekstą iš nuorodos į failą:
# https://raw.githubusercontent.com/robotautas/kursas/master/RegEx/most_visited.html
# čia yra html fragmentas, kuriame sudėti lankomiausi puslapiai 2019.
# Ištraukite šių puslapių sąrašą regex pagalba.
import re

with open("nuorodu_topai.html", 'r') as file:
    lankomiausi = file.read()
    pvz = re.compile(r'\w+\.\w+\.?\w*')
    isrinkti = pvz.findall(lankomiausi)
    print(isrinkti)
