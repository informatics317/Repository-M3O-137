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
text0 = text0.strip()
print(text0)
text0 = text0.lower()
print(text0)
text0 = text0.replace('!', '.')
text0 = text0.split('.')
text1 = text0[0]
text1 = text1.split()
print(text1.count('python'))
text2 = ' '.join(text1)
print(text2.startswith("python"))
print(text2.endswith("language"))
print(len(text2), text2.count('a'), text2.find('data'))
text3 = '-'.join(text1)
print(Counter(text1))
text = """
    Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""
import string
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.replace(' ', '')
    return text
print(clean_text(text))











