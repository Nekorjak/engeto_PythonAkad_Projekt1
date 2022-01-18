from time import sleep
from pprint import pprint


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

oddelovac1 = 84 * '-'
oddelovac2 = 84 * '='
uzivatele = {'bob': '123', 'ann': 'pass123', 'nike': 'password123', 'liz': 'pass123'}

# 1. Vyžádá si od uživatele přihlašovací jméno a heslo.
# 2. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.
# 3. Pokud je uživatel registrovaný, pozdrav jej a umožni mu analyzovat texty. Pokud není, upozorni jej a skončí.
# Nastavil jsem přihlášení na tři pokusy - jestli takový kód zvládnu.

pokus = 3

while uzivatele.get(jmeno := input('Zadejte jmeno: ')) != (heslo := input('Zadejte heslo: ')):
    pokus = pokus - 1
    # Sem se dostane na první dva neúspěšné pokusy.
    if pokus in range(1, 3):
        print(oddelovac1, 'Jméno nebo heslo jsou chybně zadány.'.center(len(oddelovac1)),
              'Máte ještě tento počet pokusů:'.center(len(oddelovac1)), f'{pokus}'.center(len(oddelovac1)),
              oddelovac1, sep='\n')
    # Sem se dostane po třetím neúspěšném pokusu a program skončí.
    else:
        print(oddelovac1, 'Přihlášení se nepovedlo.'.center(len(oddelovac1)),
              'Podívejte se do svého e-mailu nebo se zaregistrujte.'.center(len(oddelovac1)), oddelovac1, sep='\n')
        quit()
# Sem se dostane, když se úspěšně přihlásí
else:
    print(oddelovac2, 'Vítáme Vás v textovém analyzátoru'.center(len(oddelovac1)),
          'Na výběr máte tyto texty:'.center(len(oddelovac1)), oddelovac2, sep='\n')

# 4. Program nechá uživatel vybrat mezi třemi texty, uloženými v proměnné TEXTS. Pokud uživatel vybere takové číslo
# textu, které není v zadání, program jej upozorní a skončí. Pokud uživatel zadá jiný vstup než číslo,
# program jej rovněž upozorní a skončí.
# Ze zadání mi není jasné, zda mám uživateli texty vizualizovat či nikoli. Já si vybral, že to provedu pomocí
# pprintu slovníku "TEXTS_slovnik", protože se tím k textu přiřadí i čísla - je to, myslím, vizuálně user friendly.

# "Cleartext" odstraní z vizualizace nehezké konce "\n".
cleartext = [x.replace('\n', '') for x in TEXTS]
TEXTS_slovnik = {x: pismeno for x, pismeno in enumerate(cleartext, 1)}

# Prodleva tisku textů na 3 sekundy, aby uživatel viděl hlášku, než se mu posune obrazovka
sleep(2)
pprint(TEXTS_slovnik)

# Výběr textu a následná kontrola inputu
cislo_textu = input(f'\nPRO ANALÝZU SI VYBER ČÍSLO JEDNOHO Z TEXTŮ: ')

if not cislo_textu.isnumeric():
    print(oddelovac2, 'Nezadal jsi číslo!'.center(len(oddelovac1)),
          'Ukončuji program'.center(len(oddelovac1)), oddelovac2, sep='\n')
    quit()
elif int(cislo_textu) not in range(1, 4):
    print(oddelovac2, 'Vybral jsi číslo mimo nabízený rozsah!'.center(len(oddelovac1)),
          'Ukončuji program'.center(len(oddelovac1)), oddelovac2, sep='\n')
    quit()
else:
    print('\n', oddelovac2, 'Zde jsou výpočty:'.center(len(oddelovac1)), oddelovac1, sep='\n')

# 5. Pro vybraný text spočítá statistiky.
# Nejprve si kvůli přehlednosti dalších zápisů vyrobím proměnnou s vybraným textem. Následně si v další proměné
# vyčistím slova od čárek, teček apod. Nakonec si vyrobím seznam "slova" - tedy vyloučím čísla.

vybrany_text = TEXTS[int(cislo_textu) - 1]
TEXT_seznam = [objekt.strip(".,:?!/'") for objekt in vybrany_text.split()]
slova = [slovo for slovo in TEXT_seznam if slovo.isalpha()]

zarovnani = 40

# - počet slov,
print(f"{'Počet slov v textu' :>{zarovnani}} = {len(slova)}")

# - počet slov začínajících velkým písmenem,
start_velke_pismeno = [upper for upper in slova if upper.istitle()]
print(f"{'Počet slov začínajících velkým písmenem' :>{zarovnani}} = {len(start_velke_pismeno)}")

# - počet slov psaných velkými písmeny,
ALL_velke_pismeno = [ALL for ALL in slova if ALL.isupper()]
print(f"{'Počet slov psaných velkými písmeny' :>{zarovnani}} = {len(ALL_velke_pismeno)}")

# - počet slov psaných malými písmeny,
all_male_pismeno = [all for all in slova if all.islower()]
print(f"{'Počet slov psaných malými písmeny' :>{zarovnani}} = {len(all_male_pismeno)}")

# - počet čísel (ne cifer),
# Kvůli stringům kombinujícím čísla a písmena (např. "30F", nebo v jiných textech chybně spojená procenta např 25%)
# a kvůli čárkám a jiným znakům, vytahuju z textu vyčištěná čísla do "cisla_mezery". Nadbytečné mezery vyčistím
# v "cisla_string". Následně proměnnou převedu na integer do finálního listu "cisla", který potřebuji v posledním úkolu
# (součet), nebo pro další případné matematické operace.

cisla_mezery = ''.join(x if x.isdigit() else ' ' for x in vybrany_text)
cislo_string = cisla_mezery.split()
cisla = [int(index) for index in cislo_string]

print(f"{f'Počet čísel v textu' :>{zarovnani}} = {len(cisla)}")

# - sumu všech čísel (ne cifer) v textu.
print(f"{'Součet všech čísel v textu' :>{zarovnani}} = {sum(cisla)}\n{oddelovac2}")

# Graf.
# Z vyčištěných slov v proměnné "slova" spočítám pro každé slovo počet jeho hlásek a seřadím je
delka_slov = [len(slovo) for slovo in slova]
delka_slov.sort()

# Spočítám frekvcence jednotlivých délek ve "slovnik_delka_slov" Klíče jsou délky, hodnoty jsou frekvence délek.
slovnik_delka_slov = {delka: delka_slov.count(delka) for delka in delka_slov}

# Tisk grafu
print(f"\n{'LEN': <4}{'|' :>0}{'OCCURENCES' :^20}{'|' :>0} {'NR' : <1}\n{'-' * 29}")
for delka, frekvence in slovnik_delka_slov.items():
    print(f"{delka :<4}{'|' :>0}{'*' * frekvence :<16}{'|' :>5} {frekvence :<1}")
#zarovnávání v printu je uděláno ručně, tedy blbě, protože při změně výstupů (třeba velký počet hvězdiček) to asi nebude
# sedět. Jak to zarovnávání řídit právě podle měnících se prvků v grafu, to zatím netuším.
