import re
# Parašykite funkciją, kuri į parametrus priimtų tekstą ir žodžių,kuriuos reikia jame išcenzūruoti sąrašą.
# Pvz, žodis "kvaraba" yra baisus keiksmažodis,ir mums reikia duotame tekste pakeisti k*****a.
#
# iškvietus funkciją, pvz.:[\s[a-zA-Z\W]+:cenzura('baisūs žodžiai, tokie kaip kvaraba, žaltys..', 'kvaraba', 'žaltys')
# mums atspausdintų baisūs žodžiai, tokie kaip k*****a, ž****s..
# žodžių cenzūravimui naudokite regex, o jų sukeitimui tekste naudokite .replace()

def cenzura(tekstas, *keiksmai):
    for zodis in keiksmai:
        pvz = re.compile(r'([a-ząčęėįšųūž])([a-ząčęėįšųūž]+)([a-ząčęėįšųūž])')
        # [pirma raide][visos kitos viduryje][paskutine raide]
        baisiazodziai = pvz.search(zodis)
        dedam_cenzura = len(baisiazodziai.group(2)) * "*"
        zodis_su_cenzura = pvz.sub(f"\g<1>{dedam_cenzura}\g<3>", zodis)
        tekstas = tekstas.replace(zodis, zodis_su_cenzura)
    print(tekstas)
cenzura('baisūs žodžiai, tokie kaip kiaulė, kvaraba, rupūžė, žaltys..', 'kvaraba', 'žaltys', 'kiaulė', 'rupūžė')
