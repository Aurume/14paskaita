# funkcija,kuri įvestą datą (formatas dd.mm.yyyy) keistų į yyyy mm dd.
# galiu naudoti re.sub() - su juo keiciami eiluciu simboliai.
# g<3> atitinka mano metus, g<2> - menesiai, g<1>- metai.

import re

def keisti_datos_formata(mano_data):
    pvz = re.compile(r'(\d{2})\.(\d{2})\.(\d{4})')
    rezultatas = pvz.sub('\g<3> \g<2> \g<1>', mano_data)
    return rezultatas

print(keisti_datos_formata('22.02.2022'))
