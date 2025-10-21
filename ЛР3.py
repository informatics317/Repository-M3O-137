from random import *
from logging import*

basicConfig(level=DEBUG, filename='py_log.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

def massif(num):
    for i in range(5001):
        num.append(randint(1, 1000))
    return num


'''1 Пузырьковая сортировка'''
def bubble_sort(nums):
    info('1 The beginning of bubble sorting')
    flag = 1
    obmen = 0
    proxod = 0
    while flag == 1:
        flag = 0
        proxod += 1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                flag = 1
                obmen += 1
    debug(f'Passage {proxod}')
    debug(f'Number of swap {obmen}')
    info('1 The end of bubble sorting')

a = []
print('1) Исходный a:', massif(a))
bubble_sort(a)
print('Пузырьковая сортировка:', a)

print()


'''2 Сортировка выборкой'''
def selection_sort(nums):
    info('2 The beginning of sorting by selection')
    obmen = 0
    proxod = 0
    for i in range(len(nums)):
        proxod += 1
        min_elem = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_elem]:
                min_elem = j
                obmen += 1
        nums[i], nums[min_elem] = nums[min_elem], nums[i]
    debug(f'Passage {proxod}')
    debug(f'Number of swap {obmen}')
    info('2 End of selection sorting')

b = []
print('2) Исходный b:', massif(b))
selection_sort(b)
print('Сортировка выборкой:', b)

print()


'''3 Сортировка вставками'''
def insertion_sort(nums):
    info('3 The beginning of sorting by inserts')
    obmen = 0
    proxod = 0
    for i in range(1, len(nums)):
        proxod += 1
        insert = nums[i]
        j = i -1
        while j >= 0 and nums[j] > insert:
            nums[j+1] = nums[j]
            obmen += 1
            j -= 1
        nums[j+1] = insert
    debug(f'Passage {proxod}')
    debug(f'Number of swap {obmen}')
    info('3 End of insertion sorting')

c = []
print('3) Исходный c:', massif(c))
insertion_sort(c)
print('Сортировка вставками:', c)

print()


'''4 Пирамидальная сортировка'''
def  heapify(nums, size, root_index):
    largest = root_index
    left = (2 * root_index) + 1
    right = (2 * root_index) + 2

    if left < size and nums[left] > nums[largest]:
        largest = left

    if right < size and nums[right] > nums[largest]:
        largest = right

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, size, largest)

def pyramid_sorting(nums):
    info('4 The beginning of pyramid sorting')
    n = len(nums)
    for i in range(n, -1, -1):
       heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    info('4 The end of pyramid sorting')

d = []
print('4) Исходный d:', massif(d))
pyramid_sorting(d)
print('Сортировка вставками:', d)

print()


'''5 Сортировка слиянием'''
def merge(left_list, right_list):
    new_list = []
    left_index = right_index = 0
    left_len, right_len = len(left_list), len(right_list)

    for i in range(left_len + right_len):
        if left_index < left_len and right_index < right_len:
            if left_list[left_index] <= right_list[right_index]:
                new_list.append(left_list[left_index])
                left_index += 1
            else:
                new_list.append(right_list[right_index])
                right_index += 1

        elif left_index == left_len:
            new_list.append(right_list[right_index])
            right_index += 1

        elif right_index == right_len:
            new_list.append(left_list[left_index])
            left_index += 1
    return new_list

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)

e = []
print('5) Исходный e:', massif(e))
info('5 Start of merge sorting')
e = merge_sort(e)
info('5 End of merge sorting')
print('Сортировка слиянием:', e)

print()


'''6 Быстрая сортировка'''
def partition(nums, low, high):
    opora = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < opora:
            i += 1
        j -= 1
        while nums[j] > opora:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)

f = []
print('6) Исходный f:', massif(f))
info('6 The beginning of quick sorting')
quick_sort(f)
info('6 End of quick sorting')
print('Быстрая сортировка:', f)

print()


'''7 Встроенные функции сортировки'''
g = []
print('7) Исходный g:', massif(g))
info('7.1 The beginning of the function sort()')
g.sort()
info('7.1 End of function sort()')
print('Функция sort():', g)

print()

h = []
print('Исходный h:', massif(h))
info('7.2 The beginning of the function sorted()')
h = sorted(h)
info('7.2 End of function sorted()')
print('Функция sorted():', h)


