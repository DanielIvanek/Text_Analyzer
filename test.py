import re

text = '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.
'''

# Získání všech samostatných čísel ve větě
numbers = re.findall(r'\b\d+\b(?!N)', text)

# Výpis nalezených čísel
print("Samostatná čísla v textu:")
for number in numbers:
    print(number)