fajl=open("egyszamjatek.txt", "r")
#sdkjfhsdkfjh
jatekos=[]
for sor in fajl:
    rekord=sor.rstrip().split()
    Fszam=len(rekord)-1
    for i in range(Fszam):
        rekord[i]=int(rekord[i])
    jatekos.append(rekord)
fajl.close()
Jszam=len(jatekos)
print("3. feladat: Játékosok száma: ", Jszam)
print("4. feladat: Fordulók száma: ", Fszam)
voltEgyes = False
for i in range(Jszam):
    if jatekos[i][0]==1:
        voltEgyes=True
        break;
if voltEgyes:
    print("5. feladat: Az egyes fordulóban volt egyes tipp")
else:
    print("5. feladat: Az egyes fordulóban NEM volt egyes tipp")
tippek=[jatekos[i][j] for i in range(Jszam) for j in range(Fszam)]
maxtipp=max(tippek)
print("6. feladat: A legnagyobb tipp a fordulók során: ", maxtipp)
sorszam=input("Kérem a forduló sorszámát [1-"+str(Fszam)+"]")
sorszam=int(sorszam)
sz=100*[0]
for i in range(Jszam):
    szam=jatekos[i][sorszam-1]
    sz[szam]+=1
nyertesTipp=0
for i in range(1, 100):
    if sz[i]==1:
        nyertesTipp = i;
        break;
if nyertesTipp>0:
    print("7. feladat: A nyertes tipp a megadott forduloban: ", nyertesTipp)
else:
    print("7. feladat: A megadottt forduloban nem volt nyertes. ")
#8. feladat:  a nyertes neve
nyertes=""
for i in range(Jszam):
    if jatekos[i][sorszam-1]==nyertesTipp:
        nyertes=jatekos[i][10]
if len(nyertes)!=0:
    print("8. feladat: A megadott fordulo nyertese: "+ nyertes)
else:
    print("A 8. feladat: a megadott forduloban nem volt nyertes. ")
if nyertesTipp>0:
    fajl=open("pythonnyertes.txt", "w")
    fajl.write("Fordulo sorszama: "+str(sorszam)+"\n")
    fajl.write("Nyertes tipp: "+str(nyertesTipp)+"\n")
    fajl.write("Nyertes jatekos: "+nyertes+"\n");
    fajl.close()
