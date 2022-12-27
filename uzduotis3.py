# Atspausdinti visa teksta tokiu formatu:
# Event: Workshop & Tutorial proposals due
# Date: November 21, 2019

import re

tekstas = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020
'''

pvz = re.compile(r'(.+):\s([A-Z]\w+\s\d+,\s\d{4})', re.MULTILINE)
sk = 1
for eilute in tekstas.splitlines():
    #pvz = re.compile(r'(.+):\s([A-Z]\w+\s\d+,\s\d{4})', re.MULTILINE)
    rezultatas = pvz.search(eilute)
    print(f'{sk}.\nEvent: {rezultatas.group(1)}\nDate: {rezultatas.group(2)}\n')
    #print(f'Date: {rezultatas.group(2)}')
    sk += 1


