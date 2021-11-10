nevek = ['Zoli', 'András', 'Kálmán', 'Béla', 'Géza']
print(nevek)

for nev in nevek:
    print(nev, end = ' ')

print()

for i in range(len(nevek)):
    print(nevek[i], end = ' ')

# range(szam) -> előállítja a számokat 0tól a szam-ig
# range(5) -> [0, 1, 2, 3, 4]
# len(adatszerkezet) -> adatszerkezet elemszáma

print()
magassagok = []
for i in range(len(nevek)):
    magassagok.append(int(input(f'{nevek[i]} magassága: ')))

sum = 0
for m in magassagok:
    sum += m
atlag = sum / len(magassagok)
print(f'átlagmagasság: {atlag} cm')

maxi = 0
for i in range(1, len(magassagok)):
    if magassagok[maxi] < magassagok[i]:
        maxi = i
print(f'legnagyoo magasság: {magassagok[maxi]}')
print(f'indexe {maxi}')
print((f'legmagasabb ember: {nevek[maxi]}'))

for i in range(len(magassagok) - 1):
    for j in range(i + 1, len(magassagok)):
        if magassagok[i] < magassagok[j]:
            sm = magassagok[i]
            sn = nevek[i]
            magassagok[i] = magassagok[j]
            nevek[i] = nevek[j]
            magassagok[j] = sm
            nevek[j] = sn

for i in range(len(nevek)):
    print(f'{nevek[i]}: {magassagok[i]} cm')