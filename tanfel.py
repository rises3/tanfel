# #v1
# tantargyFelosztas=[]
# with open("beosztas.txt", "r", encoding="UTF-8") as fin:
#     for sor in fin:
#         tantargyFelosztas.append(sor.strip())


# #for elem in tantargyFelosztas:
# #    print(f"{elem},")
    
# print(f"A listának {int(len(tantargyFelosztas)/4)} eleme van")

#v2

tanarok=[]
tantargyak=[]
osztalyok=[]
oraszamok=[]

rekord=[]

with open("beosztas.txt", "r", encoding="utf-8") as fin:
    for sor in fin:
        rekord.append(sor.strip())
        if len(rekord)==4:
            tanarok.append(rekord[0])
            tantargyak.append(rekord[1])
            osztalyok.append(rekord[2])
            oraszamok.append(int(rekord[3]))
            rekord=[]
            

print("2. feladat")
print(f"A bejegyzések száma: {len(tanarok)}")

print("3. feladat")
print(f"Az iskolában a heti összóraszám: {sum(oraszamok)}")

print("4. feladat")
beTanar=input("Egy tanár neve= ") or "Albatrosz Aladin"
def osszegzes(beTanar, tanarok, oraszamok):
    ossz0raszam=0
    for i in range(len(tanarok)):
        if tanarok[i]==beTanar:
            ossz0raszam+=oraszamok[i]
    return ossz0raszam
print(f"A tanár heti óraszáma: {osszegzes(beTanar, tanarok, oraszamok)}")

print("5. feladat")
def eldontes(beO, beT, t, o):
    i=0
    while i<len(tantargyak) and not beTantargy==tantargyak[i] and beOsztaly.split(". ")[0]==osztalyok[i].split(". ")[0] and "x" in osztalyok[i]:
        i+=1
    return i<len(tantargyak)
    
beOsztaly=input("Osztály= ") or "9.a"     
beTantargy=input("Tantárgy= ") or "matematika"
if eldontes(beOsztaly, beTantargy, tantargyak, osztalyok):
    print("Csoportbontásban tanulják.")
else:
    print("Nem csoportbontásban tanulják.")


print("6. feladat")
tanarokEgyedi=[]
def megszamol(tanarok):
    for tanar in tanarok:
        if tanar not in tanarokEgyedi:
            tanarokEgyedi.append(tanar)
    return len(tanarokEgyedi)
        
print(f"Az iskolában {megszamol(tanarok)} tanár tanít.")