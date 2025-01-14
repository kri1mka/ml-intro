import numpy as np
import re


#1 Your task is to make a function that can take any non-negative integer as an argument 
#and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
def task1 (number):
    b = sorted(str(number), reverse = True)
    return int(''.join(b))

def task2 (number):
    b = ''
    for i in str(number):
        b += str(int(i)**2)
    return int(b)

def task3 (arr):
    b = 0
    for i in arr:
        b ^= i
    return b 

def task4 (number): 
    count = 0
    while number >= 10:
        i = 1
        while number > 0:
            i *= number % 10 
            number //= 10 
        number = i 
        count += 1
    return count

def task5 (str):
    a = sorted(str.lower())
    duplicates = []
    p = 0
    for i in a:
        if a.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
            p += 1
    return p, duplicates

def task6 (massiv):
    a = " "
    if len(massiv) == 0:
        a = "no one likes this"
    elif len(massiv) == 1:
        a = massiv[0] + " likes this"
    elif len(massiv) == 2:
        a = massiv[0] + " and " + massiv[1] + " like this"
    elif len(massiv) == 3:
        a = massiv[0] + ", " + massiv[1] + " and " + massiv[2] + " like this"
    elif len(massiv) >= 4:
        others = str(len(massiv) - 2)
        a = massiv[0] + ", " + massiv[1] + " and " + others + " others like this"
    return a

def task7 (map):
    list = []
    while map:
        for i in map[0]:
            list.append(i)
        map.pop(0)
        if not map:
            break
                    
        for j in map:
            list.append(j[-1])
            j.pop()

        for k in range(len(map[-1]) -1, -1, -1):
            list.append(map[-1][k])
        map.pop()
        if not map:
            break

        for l in reversed(map):
            list.append((l[0]))
            l.pop(0)
    return list

def task8 (str):
    no = "aeiouAEIOU"
    result_string = ""
    for char in str:
        if char not in no:
            result_string += char
    return result_string

def task9 (pin):
    return len(pin) in (4, 6) and pin.isdigit()

def task10 (text):
    text = text.replace("-", " ").replace("_", " ")
    words = text.split()
    return "".join([w.capitalize() if w != words[0] else w for w in words])

def task11 (str):
    str2 = ""
    result = ""
    i = len(str)
    while i > 0:
        if i >= 2:
            str2 = str[:2]
            result += str2 + " "
            str = str[2:]
            i = len(str)
        elif i == 1:
            result += str[-1] + "_"
            break
    res = result.split()
    return res

def task12 (url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')


m_a = np.array([[1, 2, 3, 4]
                ,[5, 6, 2, 7]
                ,[9, 1, 8, 3]
                ,[2, 4, 6, 7]])

mass = ["Alex", "Jacob", "Mark", "Max" ]
arr = [0, 1, 1, 1, 0]
mynumber = input('Your number: ')
mynumber1 = 25
mystr = input('Your word: ')
pin = "-16520"
camel = "the_stealth_warrior"
url = "https://www.cnet.com"

result1 = task1(mynumber)
result2 = task2(mynumber)
result3 = task3(arr)
result4 = task4(mynumber1)
result5 = task5(mystr)
result6 = task6(mass)
result7 = task7(m_a)
result8 = task8(mystr)
result9 = task9(pin)
result10 = task10(camel)
result11 = task11(mystr)
result12 = task12(url)

print('Task1: ', result1)
print('Task2: ', result2)
print('Task3: ', result3)
print('Task4: ', result4)
print('Task5: ', result5)
print('Task6: ', result6)
print('Task7: ', result7)
print('Task8: ', result8)
print('Task9: ', result9)
print('Task10: ', result10)
print('Task11: ', result11)
print('Task12: ', result12)