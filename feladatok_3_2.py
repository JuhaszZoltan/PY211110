import random as rnd
import numpy as np

szamok = []
for n in range(20):
    szamok.append(rnd.randint(50, 150))
szamok.sort()

print(f'számok rendezve: {szamok}')
osszzeg = sum(szamok)
print(f'számok összege: {osszzeg}')
atlag = np.average(szamok)
print(f'számok átlaga: {atlag}')