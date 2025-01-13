import numpy as np


#1 Your task is to make a function that can take any non-negative integer as an argument 
#and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
def task1 (number):
    b = sorted(number, reverse = True)
    return b

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
    while number > 10:
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

def task7 (arr): #решить!!
    n = m_a.shape
    arr1 = []
    arr1.append(arr[0])
    for j in arr:
        arr1.append([j[-1:-1]])
    return arr1

def task8 (str):
    no = "aeiouAEIOU"
    result_string = ""
    for char in str:
        if char not in no:
            result_string += char
    return result_string

def task9 (str):
    if len(str) == 6 or len(str) == 4 and str.isdigit():
        a = True
    else:
        a = False
    return a

def task10 (str):
    x = ""
    str2 = str.title()
    x = str2.replace("_", " ")
    x = str2.replace("-", " ")

    no = " "
    result = ""
    for char in x:
        if char not in no:
            result += char
    return result



m_a = np.array([[1, 2, 3, 4]
                ,[5, 6, 2, 7]
                ,[9, 1, 8, 3]
                ,[2, 4, 6, 7]])

mass = ["Alex", "Jacob", "Mark", "Max" ]
arr = [0, 1, 1, 1, 0]
mynumber = input('Your number: ')
mynumber1 = 999
mystr = input('Your word: ')
pin = "916520"
camel = "the-stealth-warrior"

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