import random as rnd
#            0        1       2        3         4
nevek = ['András', 'Béla', 'Cecil', 'Dénes', 'Elemér']

# lista elem száma = utolsó index + 1
# utolsó index = eéemszám - 1


print(nevek[2]) #OP -> Cecil

nevek[0] = 'Zoltán'

masik_lista = []
# masik_lista[0] = 'Tibor' # -> HIBA (out of range)

# helyette:
masik_lista.append('Tibor')
# megnöveli a lista hosszát, majd az új üres helyre besteszi
# a paraméterben lévő objektumot

nevek.append('Kálmán')
# -> kálmán a 5ös indezű (azaz a 6. elem) lesz a listában

nevek_hossza = len(nevek)
# len() -> visszaadja az összetett adatszerkezet hosszát
# (aka. elemszámát)
print(nevek_hossza)