"""
slovniky sluzia na ulozenie rozneho poctu objektov
kazdy identifikovatelny pomocou jedinecneho kluca

Slovniky sa casto nazyvaju maps, hashmaps, lookup tables(vyhladavacie tabulky),
or associative arrays(asociativne polia).
Umožňujú efektívne vyhľadávať, vkladať a mazať akýkoľvek objekt spojený s daným klucom.

Kluce mozu byt hocijaky hashovatelny objekt.
"""

"""cvicenie"""
slovnik = {'Hello': 56, 'at': 23, 'test': 43, 'This': 78, 'Why': 11}

print({kluc: hodnota         # 3. na vystupe urcim kam idu tie premenne
       for (kluc, hodnota)   # 2. ku kazdemu clenu paru priradim  nazvy premennych
       in slovnik.items()})  # 1. zo slovnik my to vypise vsetky pary - XXXX, XXXX

print(slovnik)

'''
Creation
'''

slovnik = {'kluc1': ['55'], 'kluc2': 'hodnota2', 'kluc3': 'hodnota3', 'kluc4': 'hodnota4'}
empty_slovnik = {}
another_empty_slovnik = dict()

print(slovnik)

'''Pridaj do slovnika, ak kluc existuje zmen hodnotu.'''
slovnik['kluc2'] = 'hodnotaXXX'
slovnik['kluc2'] = 'hodnotaXXX'

print(slovnik)

'''It can be a list of tuples or another  slovnik of kluc-hodnota pairs'''
slovnik.update({'kluc2': 23, 'kluc3': 89})

'''ak kluc je string nemusime davat {}'''
slovnik.update(after=10)
print(slovnik)

slovnik.update({'kluc4': [1, 2, 3]})  # list ako hodnota

''' ku klucu pridaj hodnotu v liste, povodna ostava, najprv vytvorit list'''
slovnik["kluc1"].append('33')
'''!!!!! hodnota v slovniku musi byt list ( v [] )'''

'''Retrieval of hodnota for a particular kluc'''
hodnota = slovnik["kluc1"]
print(hodnota)
'''if not found => klucError'''

'''Deletion.'''
''' whole  slovnik
del slovnik
'''

'''element with kluc'''
del slovnik['kluc1']

''' removes element with kluc and returns its hodnota'''
slovnik.pop('kluc2', 32)
'''32 : The default hodnota that will be returned if the given kluc does not exist in the  slovnik.'''
'''if not found => klucError'''

kluc_na_vymaz = 'at'
if kluc_na_vymaz in slovnik:
    slovnik.pop(kluc_na_vymaz)
else:
    print(f'kluc {kluc_na_vymaz} is not in the  slovnik')
    '''alebo continue'''
print(slovnik)

'''Removing a kluc from a  slovnik'''
kluc_na_vymaz = 'at'
if kluc_na_vymaz in slovnik:
    del slovnik[kluc_na_vymaz]
else:
    print(f'kluc {kluc_na_vymaz} is not in the  slovnik')
    '''alebo continue'''
print(slovnik)

'''clear contents of  slovnik'''
slovnik.clear()

'''vycisti vnorene slovniky v liste slovnikov'''
list_of_slovnik = [
        {'Name': 'Shaun', 'Age': 35},
        {'Name': 'Ritika', 'Age': 31},
        {'Name': 'Smriti', 'Age': 33},
        {'Name': 'Jacob', 'Age': 23},
]
print(list_of_slovnik)

''' Clear all slovnik in a list of slovnik'''

for elem in list_of_slovnik:
    elem.clear()
print('Updated  slovnik:')
print(list_of_slovnik)

'''Insert a  slovnik into another  slovnik'''

my_slovnik0 = {"username": "XYZ", "email": "xyz@gmail.com", "location": "Washington"}
my_slovnik1 = {"firstName": "Nick", "lastName": "Price"}

my_slovnik0["name"] = my_slovnik1

print(my_slovnik0)

'''Remove even hodnoty in  slovnik'''

'''slovnik of string and integers'''
slovnik = {'Hello': 56, 'at': 23, 'test': 43, 'This': 78, 'Why': 11}
slovnik = {kluc: hodnota
           for kluc, hodnota in slovnik.items()
           if hodnota % 2 != 0}
print(slovnik)

'''Filter a  slovnik'''

slovnik = {7: 'sam', 8: 'john', 9: 'mathew', 10: 'riti', 11: 'aadi', 12: 'sachin'}

'''filter by kluce'''

''' Filter  slovnik by keeping elements whose kluce are divisible by 2'''
newslovnik0 = dict(filter(lambda elem: elem[0] % 2 == 0, slovnik.items()))
'''or '''
newslovnik = {kluc: hodnota for (kluc, hodnota) in slovnik.items() if kluc % 2 == 0}

print('Filter 1 : ')
print(newslovnik0)
print(newslovnik)

'''filtruj podla hodnot'''
'''ponechaj elementy ktore maju dlzku stringu 6'''
newslovnik2 = dict(filter(lambda elem: len(elem[1]) == 6, slovnik.items()))
'''or'''
newslovnik2b = {kluc: hodnota for (kluc, hodnota) in slovnik.items() if len(hodnota) == 6}

print('Filter 2 : ')
print(newslovnik2)
print(newslovnik2b)

'''vytvor, kovertuj z listu, elementy listu budu kluce'''
'''List of strings'''
zoznam_stringov = ["kluc1", "kluc2", "kluc3", "kluc4", "kluc5", "kluc6"]

slovnik_slov1 = {i: 66 for i in zoznam_stringov}
''' vysledok  =  element:66, namiesto elementu, zo zoznamu'''
print(slovnik_slov1)

slovnik_slov2 = slovnik.fromkeys(zoznam_stringov, 66)
'''vysledok   = funkcia ( iterovatelny objekt, hodnota na priradenie ku kazdemu klucu)'''

print(slovnik_slov2)

''' list element ako hodnoty'''
slovnik_slov3 = {I: zoznam_stringov[I] for I in range(0, len(zoznam_stringov))}
'''vysledok   =  I: zoznam_stringov[I] kde I je z rozsahu(0 - max index(zoznam_stringov))
   kluc bude cislovka index(zoznam_stringov), hodnota bude element zo zoznam_stringov '''
print(slovnik_slov3)

'''Premenovat kluc, ponechanie hodnoty
nejde zmenit, treba vymazat a vlozit nanovo
'''
hodnotaX = slovnik_slov2.pop('kluc3')
slovnik_slov2.update({'kluc1_NEW': hodnotaX})

'''Zlucit dva slovniky'''

'''!!!!! 1 cast - spolocne kluce budu mat ako hodnotu IBA hodnotu kluca z posledneho slovnika'''
slovnik1 = {'Ritika': 5, 'Sam': 7, 'John': 10}
slovnik2 = {'Aadi': 8, 'Sam': 20, 'Mark': 11}

slovnik1.update(slovnik2)
print(slovnik1)

'''alebo'''
slovnik3 = {**slovnik1, **slovnik2}
'''** rozlozi slovnik na jednotlive pary kluc, hodnota.'''
'''Cize slovnik3 sa sklada z jednotlivych parov slovnika 1 aj slovnika 2'''
print(slovnik3)

'''!!!!! 2 cast - zlucit slovniky a ponechat OBE hodnoty spolocnych klucov.'''

slovnik1 = {'Ritika': 5, 'Sam': 7, 'John': 10}
slovnik2 = {'Aadi': 8, 'Sam': 20, 'Mark': 11}


def zlucit_slovnik(slovnik1, slovnik2):               # parametre su slovniky. argumenty su pary KV
    slovnik3 = {**slovnik1, **slovnik2}               # zluci ale ostanu len hodnoty z posledneho slovnika
    for kluc, hodnota in slovnik3.items():            # cize
        if kluc in slovnik1 and kluc in slovnik2:     # ak je kluc v oboch slovnikoch
            slovnik3[kluc] = [hodnota, slovnik1[kluc]]
    '''kluc v zlucenom slovniku 3 = [hodnota kluca z 3(2), hodnota rovnakeho kluca zo slovnik1
                                                                (lebo bola prepisana v(3)]'''
    return slovnik3


slovnik3 = zlucit_slovnik(slovnik1, slovnik2)
print(slovnik3)
print("+")

slovnik1 = {'Ritika': 5, 'Sam': 7, 'John': 10}
slovnik2 = {'Aadi': 8, 'Sam': 20, 'Mark': 11}
slovnik3 = {'Mark': 18, 'Rose': 22, 'Wong': 22}

finalslovnik = zlucit_slovnik(slovnik3, zlucit_slovnik(slovnik1, slovnik2))
print(finalslovnik)

'''Operacie s klucmi a hodnotami'''
'''hodnoty'''
def concatenate(**objekt):           # parameter je list KV parov, ** ho rozlozi na jednotlive KV pary
    result = ""
    for hodnota in objekt.values():  # hodnota je hodnota z KV paru
        result += hodnota
    return result


print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
#   > RealPythonIsGreat!

''' kluce '''
def concatenate(**objekt):  # parameter je list KV parov, ** ho rozlozi na jednotlive KV pary
    result = ""
    for kluc in objekt:     # kluc je kluc z KV paru
        result += kluc
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
#   > abcde

'''Vypis vsetky pary zo slovnika'''
for kluc, hodnota in slovnik.items():
    print(kluc, '::', hodnota)

print("    v opacnom poradi")
zoznam_parov = list(slovnik.items())  # reversed nefunguje na slovniku
for kluc, hodnota in reversed(zoznam_parov):
    print(kluc, '::', hodnota)

'''Vypis vsetky pary z vnorenych slovnikov v slovniku'''

students = {
        'ID 1': {'Name': 'Shaun', 'Age': 35, 'City': 'Delhi'},
        'ID 2': {'Name': 'Ritika', 'Age': 31, 'City': 'Mumbai'},
        'ID 3': {'Name': 'Smriti', 'Age': 33, 'City': 'Sydney'},
        'ID 4': {'Name': 'Jacob', 'Age': 23, 'City': {'perm': 'Tokyo', 'current': 'London'}},
}


def vypis_vsetky_pary(slovnikovy_objekt):
    for kluc, hodnota in slovnikovy_objekt.items():  # pre kazdy par zo slovnika(argument)
        if isinstance(hodnota, dict):  # ak je hodnota ^ instanciou slovnik
            vypis_vsetky_pary(hodnota)  # pouzi znova funkciou na tuto hodnotu
        else:
            print(kluc, '::', hodnota)  # inak vypis " kluc :: hodnota "


vypis_vsetky_pary(students)

print("    Vypis vsetky pary z vnorenych zoznamov v slovniku")

slovnik = {'is':   [1, 3, 4, 8, 10],
           'at':   [3, 10, 15, 7, 9],
           'test': 33,
           'this': [2, 3, 5, 6, 11],
           'why':  [10, 3, 9, 8, 12]}

for kluc, hodnoty in slovnik.items():
    if isinstance(hodnoty, list):
        for hodnota in hodnoty:
            print(kluc, hodnota)
    else:
        print(kluc, hodnoty)

print("#### Vypis vsetky hodnoty zo slovnika")

list_of_hodnoty = list(slovnik.values())
print(list_of_hodnoty)
