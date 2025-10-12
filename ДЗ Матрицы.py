from random import *

def fill_matrix(size=None, range_=(0, 10)):
    if size is not None:
        rows, cols = size
        min_, max_ = range_
        matrix = [[randint(min_, max_) for _ in range(cols)] for _ in range(rows)]
        return matrix

new_matrix = fill_matrix(size=(10, 10), range_=(-50, 50))
print('Новая матрица:')
for row in new_matrix:
    print(row)

