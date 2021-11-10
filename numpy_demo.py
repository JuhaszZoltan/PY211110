import numpy
n = ['A', 'B', 'C', 'D', 'E']
m = [180, 170, 160, 190, 150]
max_index = m.index(numpy.max(m))
print(f'A legmagasabb {n[max_index]}')