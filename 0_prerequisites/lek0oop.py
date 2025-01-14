import numpy as np

#Classy Extensions !
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self, name):
        result = "{} makes a noise".format(name)
        return result

class Cat(Animal):
    def speak(self):
        return self.name + ' meows.'
  
c = Cat("Max")
print(c.speak())


#Classy Classes !
class Person:
    def __init__(self, name,age):
        self.info = "{}s age is {}".format(name, age)

print('\n')
name = input("Input name: ")
age = input("Input age: ")

a = Person(name, age)
print(a.info)


#Interactive Dictionary !
class Dictionary:
    def __init__(self):
        self.dictionary = {}
    
    def newentry(self, fruit, descrip):
        self.dictionary[fruit] = descrip

    def look(self, fruit):
        return self.dictionary.get(fruit, "Can't find entry for " + fruit)

d = Dictionary()

d.newentry('Apple', 'A fruit that grows on trees')
d.newentry('Banana', 'A yellow fruit')

print('\n')
print(d.look('Apple'))
print(d.look('Banana'))


#Who has the most money? !
class Student:

    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def countmoney(students):
        max_money = 0
        ind_max = ""

        for student in students:
            total = (5 * student.fives) + (10 * student.tens) + (20 * student.twenties)

            if total > max_money:
                max_money = total
                ind_max = student.name
                all_same = False
            elif total == max_money:
                all_same = True

        if all_same:
            return 'all'
        else:
            return ind_max

            
tom = Student("Tom", 4, 2, 2)
ann = Student("Ann", 2, 2, 1)
s = Student("Some Student", 0, 0, 0)
print(s.countmoney([tom, ann]))


#Vector class !
class Vector:
    def __init__(self,arr):
        self.arr=arr

    def __str__(self):
        return str(tuple(self.arr)).replace(' ','')
    
    def add(self,v2):
        self.check_length(v2)
        return Vector([self.arr[a]+v2.arr[a] for a in range(len(self.arr))])

    def subtract(self,v2):
        self.check_length(v2)
        return Vector([self.arr[a]-v2.arr[a] for a in range(len(self.arr))])

    def dot(self,v2):
        self.check_length(v2)
        return sum(self.arr[a]*v2.arr[a] for a in range(len(self.arr)))

    def norm(self):
        return sum(a**2 for a in range(len(self.arr)))**.5

    def equals(self,v2):
        self.check_length(v2)
        return sum(1 for a in self.arr if a not in v2.arr)==0

    def check_length(self,v2):
        if len(self.arr)!=len(v2.arr):return('Vectors are of different lengths.')

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

print(a.add(b))      # should return a new Vector([4, 6, 8])
print(a.subtract(b)) # should return a new Vector([-2, -2, -2])
print(a.dot(b))      # should return 1*3 + 2*4 + 3*5 = 26
print(a.norm())      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)

