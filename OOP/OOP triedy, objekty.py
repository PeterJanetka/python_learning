"""
# methods = metody, chovanie, {funkcia v clase = metoda}
# attributes = atributy, data, data field, datova zlozka, vlastnosti,
# class = trieda,
# objekt = instancia triedy

Objekt - konkretna reprezentacia triedy.
                       (instancia triedy)

Pomocou objektov uchovavame stav.

Stav objektu definujeme pomocou atributov ( premennych)
ktore su naviazane na ten konkretny objekt.

Spravanie, metody definujeme v triede
ale vieme ich pouzit/vykonat az nad samotnym objektom.

Stav a spravanie, sa viazu iba k objektu.

Spravanie definujeme pomocou metod triedy (funkcii)

Pomocou self pristupujeme k instancii objektu
(self je reprezentaciou objektu triedy)

objekty sa vytvaraju v konstruktore
do konstruktoru dalej posielame premenne ktore budu definovat stav objektu

==

vytvorenie instancie(objektu) triedy:
vyvolam triedu pomocou mena triedy a
predam argumenty ("Milan") parametrom konstruktoru (name_p).

==

By using the “self” keyword we can access the attributes and methods
of the class in python. It binds the attributes with the given arguments.


"""


class Person:
    def __init__(self, name_p, surname_p):
        self.name = name_p
        self.surname = surname_p

    def introduce_yourself(self):
        print(f"Hi I am {self.name}")


milan = Person("Milan", "Velky")
milan.name
milan.surname
milan.introduce_yourself

"""


Objektovo orientovany program pozostava zo skupiny interagujucich objektov.

Vnutorna implementacia objektov nieje pristupna uzivatelovi 
pretoze je zabalena v objekte. (enkapsulacia, zapuzdrenie)

Objekt mozeme mat vlastnosti: 
polia(data, atributy) a metody(spravanie objektu).

Trieda je abstraktnejsi koncept ako objekt, triedu mozeme  povazovat 
za sablonu ktora popisuje spolocnu strukturu skupiny objektov.

"""
