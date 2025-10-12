'''1'''
# import math
# a = int(10)
# b = float(12.35)
# print(a+b, a-b, a*b, a/b)
# print(type(a/b))
# R = 5
# print('Площадь круга =', round(math.pi*R**2, 2))


'''2'''
# text = ' Hello, Python! '
# text = text.strip()
# print(text)
# text = text.replace('!', '?')
# print(text)
# text = text.upper()
# print(text)
# text = text.lower().replace('?', '!')
# print(text)


'''3'''
# import copy
# numbers = [7, 2, 5]
# numbers.append(4)
# print('2)', numbers)
# numbers.insert(1, 10)
# print('3)', numbers)
# numbers.extend([1, 1, 1])
# print('4)', numbers)
# numbers.remove(7)
# print('5)', numbers)
# pop = numbers.pop()
# print('6)', pop)
# numbers.sort()
# print('7)', numbers)
# numbers.reverse()
# print('8)', numbers)
# m = numbers.count(2)
# print('9)', m)
# n = numbers.index(1)
# print('10)', n)
# new = numbers.copy()
# print('11)',new)
# new1 = copy.deepcopy(numbers)
# print(new1)
# numbers.clear()
# print(numbers)


'''4'''
# t = (1, 2, 3)
# try:
#     t[1] = 100
#     print(t)
# except:
#     print('Кортеж неизменяем')
# d = (4, 5)
# t2 = t + d
# print(t2)
# print(t2.count(3))
# print(t2.index(4))
# print(t)


'''5'''
# values = [3, 1, 3, 2, 1, 5, 2]
# unique_values = set(values)
# print(unique_values)
# print(len(unique_values))
# other = {2, 4, 5}
# print('1)', unique_values & other)
# print('2)', unique_values | other)
# print('3)', unique_values - other)
# print(other - unique_values)


'''6'''
# scores = {'Alice': 85, 'Bob': 90}
# scores['Charlie'] = 78
# print(scores)
# scores['Bob'] = 95
# print(scores)
# print(scores.get('Dave', 'не найден'))
# print(scores.get('Alice', 'не найден'))
# del scores['Alice']
# print(scores)
# print(len(scores))
# print(scores.keys())
# print(scores.values())


'''7'''
from collections import*
text0 = """
    Python is a powerful programming language.
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""
text0 = text0.strip().lower()
print('1)', text0)
text = text0 = text0.replace('!', '.').replace('\n', '').replace('  ', '')
print('2)', text0)
text0 = text0.split('.')
text0 = [a for a in text0 if a!= '']
text1 = text0[0]
print('1-ое предложение:', text1)
text1 = text1.split()
print('5)', text1)
print('6)', text1.count('python'))
text2 = ' '.join(text1)
print('7)', 'startswith:', text2.startswith("python"), 'endswith:', text2.endswith("language"))

print('8)', len(str(text0)), str(text0).count('a'), str(text0).find('data'))
text3 = text.split()
text3 = '-'.join(text3)
print('9)', text3)
print('10)', Counter(text.split()))
text = """
    Python is a powerful programming language.
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""
import string
def clean_text(text):
    text = text.strip()
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.replace(' ', '')
    return text
print('11)', clean_text(text))











