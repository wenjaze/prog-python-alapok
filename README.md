### Python/Programozás alapok

#### 0. Változó (Variable) :
A változók nem másak mint lefoglalt memória"helyek", melyek adatok tárolására szolgálnak.
#### 1. Deklaráció (Declaration) : 
A deklaráció amikor bevezetsz egy új változót a programodba.
A deklaráció formája :
változó neve = érték
```python
valtozo_int = 32
valtozo_double = 12442458995.12341245
valtozo_float = 0.122
valtozo_bool = True
valtozo_char = 'D'
valtozo_string = "Ez egy string."
```

Változó tipusok : 
*A byte méretek a C-ben használt méretek*
- int(egész) - egész számot tárolunk benne, egy int mérete a memóriában : 4 byte 
- double (nem egész számok) - double-t akkor használunk, ha nem egész számot akarunk és a szám nagy
- float (nem egész szám) - float-ot többnyire akkor használunk ha valami hasonló számról van szó : 0,2     5,3     tehát szintén nem egész szám, viszont kisebb helyet foglal mint  a double.
- bool(igaz vagy hamis) - két értéke lehet : True, False
- char(karakter) - 1 db bármilyen karaktert tartalmazhat. Mérete a memóriában : 1 byte
- string(karakter sorozat)

__*PYTHON:*__
_Pythonban minden változótípus egy objektum, ezért nem kell a deklaráláskor megadni a típust. A Pythonon kívül sok nyelvben azonban meg kell, lásd:_
- C
- C++
- Java
- C#

#### 2. Operátorok (Operators) : 
Az operátorok, műveletek amikkel manipulálni tudjuk a programunkban deklarált változók értékét(elég pongyola fogalmazás de nem nagyon tudok mit mondani rólunk, magukért beszélnek).

- `+` : osszead ket valtozot(sum)
- `-` : kivon két változot egymasbol(subtract)
- `*` : szorzás(multiply)
- `/` : osztás(divide)
- `%` : maradékos osztás pl.: 5 % 3 = 2(mod)
- `=` : értékadás (assign)
- `++` : érték növelés 1-el(increment), 2 fomája van,
    posztinkementáció : i++ vagy preinkrementáció : ++i a különbség,
    hogy a ++i-nél mindenképpen először növeli egyel az értékét. (ez majd kesobb lesz erdekesebb, amugy kb. semmi különség) (EZ PYTHONBAN NINCS)
- `==` : Egyenlőség vizsgálat -> igaz bool érték ha igaz, hamis bool érték ha hamis az egyenlőség

    `--` : érték csökkentés 1-el
    `+=` : az jelenti pl x += 5 ugyanaz mint x = x+5
    `-=` : ugyanaz mint az osszeadás csak kivonás
    `*=` : x \*= 5 ugyanaz mint x = x\*5

#### 3. Feltétel tevés (Condition,if statement): 
Amikor feltétel tevésről beszélünk, akkor minden esetben az if-re gondolunk(van más formája is a "switch-case" kifejezés)
A feltétel tevés szintaktikája : 

```python
if a==b:
    print("Egyenlőek")
```

Ha a feltétel teljesül akkor lefut a kód ami a következő sorban van,
egy tabulátorral beljebb, ha nem akkor a feltétel utáni sorban lévő kód nem fog lefutni. Ha azt akarjuk, hogy akkor is történjen valami, ha a feltételünk nem teljesül akkor az `else` kifejezést használva megtehetjük. Tehát ha azt akarjuk pl.: ha egyenlőek írja ki, hogy "Egyenlőek", ha nem akkor írja ki hogy "Nem egyenloek", akkor ennyit kell hozzáírnunk a fenti kódhoz.

```python
else
    print("nem egyenloek")
```

Továbbá fontos még, hogy ha több feltételt akarunk írni akkor az "elif" kifejezést kell használni. pl.:
Egy menüt írunk a programunkhoz és az 1,2,3-beírásával választunk menüpontot:
ha 1-et irsz uj fiokot hozhatsz letre, ha 2-t meglevo fiokon modosithatsz, 3 kilépés.

```python
if (valasztott == 1):
    #...
    #uj fiok letrehozasa
    #...
elif (valasztott == 2):
    #...
    #meglevo fiok modositasa
    #...
elif (valasztott == 3):
    #...
    #kilepes
    #...
else:
    #...
    #cout << "nincs ilyen menüpont";
    #...
```

#### 4. Ciklusok (Loops) : 
A ciklusok arra szolgálnak, hogy egy sokszor ismétlődő folyamatot egyszerűbben megírjunk . Például, ki akarom iratni, hogy "Hello World" 5 ször egymás után, akkor ez lenne a kód pl Python-ban :
```python
print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")
```
most ciklussal : 

```python
for i in range(0,5):
    print("Hello World")
```
A ciklusok egy ciklusfejből és egy ciklus magból állnak.
A ciklus fejben meghatározzuk, hogy a ciklus mettől meddig menjen,
a ciklus magban pedig azt, hogy mi fog történni egyetlen ciklus lefutás alatt.



while : Előltesztelő ciklus, ami azt jelenti, hogy többnyire úgy használod, hogy 
előre deklarálsz egy változót, utána jöhet a ciklusfej, itt a for-tól eltérően egy feltételt adsz majd meg és ez határozza meg meddig megy a ciklus. Előző példa while-al:

```python
    i = 0
    while (i<5):
        print("Hello World!")
        i+=1
```

#### 5. Bemenet/Kimenet (I/O) : 
Pythonban a bemenet kimenet kezelése, sokkal könnyebb mint a nyelvek
nagy részében.

*Input:*
```python
    nev = input("Ird ide a neved:")
```
*Output*
```python
    print(nev)
```

Formázások :
- ```"\n"``` -> új sor
- ```"\t"``` -> tabulátor


Feladat : Írasd ki 1-100-ig a számok négyzetét.
Feladat : Kérd be a Felhasználó nevét, életkorát,tárold el őket változókban, majd ha az életkor kevesebb mint 18, írd ki, hogy Hello, <név> !, ha a felhasználónk idősebb mint 18, írd ki, hogy Üdv, <név>!.