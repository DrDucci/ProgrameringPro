#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Filer
Namn: Melissa Molnstrand
Klass: Lärare
Datum: 2022-01-11

En introduktion till filhantering

För att detta exempel skall fungera krävs det att ett dokument finns i projektet som heter newfile.txt

"""

# *** DEL 1 ***
# Skriva ut filens innehåll med with
with open('new.txt', 'r') as f:
    print(f.read().encode("windows-1252").decode("utf-8"))

# *** DEL 2 ***
# Skriv ut filens innehåll med hjälp av ett objekt som innehåller filen
f = open('new.txt', 'r')
print(f.read().encode("windows-1252").decode("utf-8"))

# *** DEL 3 ***
# Om vi använder read och anger en siffra som parameter så kommer den hämta antalet tecken som är angivet
# som parameter. Om vi användare då read() på samma objekt, f, så kommer den fortsätta därifrån den slutade.
# Vi kan se det som en markör som förflyttar sig det antalet tecken som står angivet, och sedan stannar där.
f = open('new.txt', 'r')
print(f.read(5).encode("windows-1252").decode("utf-8"))
print(f.read(3).encode("windows-1252").decode("utf-8"))
print(f.read(6).encode("windows-1252").decode("utf-8"))
print(f.read(10).encode("windows-1252").decode("utf-8"))


# *** DEL 4 ***
# Seek fungerar så att parametern vi som vi anger, går till det tecknet i filen
f = open('new.txt', 'r')
f.seek(5)
print(f.read(5).encode("windows-1252").decode("utf-8"))
f.seek(3)
print(f.read(5).encode("windows-1252").decode("utf-8"))

# *** DEL 5 ***
# Med hjälp av readlines() kan vi läsa av hela filen och sätta in den i en lista, där varje rad blir ett objekt i listan
# Viktigt att tänka på är att sista tecken i varje rad är \n, så när vi använder print() kommer det bli dubbla radbryt.
# Detta kan vi ordna med att på varje sträng använda funktionen .strip()

f = open('new.txt', 'r')
listanMedRader = f.readlines()

for rad in listanMedRader:
    print(rad.encode("windows-1252").decode("utf-8").strip())

# *** DEL 6 ***
# Viktigt när vi skapat ett objekt är att vi stänger ner objektet efter när vi är klara med det:

f = open('new.txt', 'r')
listanMedRader = f.readlines()
f.close() # Vi använder funktionen close() för detta

for rad in listanMedRader:
    print(rad.encode("windows-1252").decode("utf-8").strip())

