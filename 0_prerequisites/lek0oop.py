import numpy as np

#Classy Extensions
class Animal:
    def __init__(self):
        self.name = ""

    def speak(self, name):
        result = "{} makes a noise".format(name)
        return result

class Cat(Animal):
    
    def speak(self, name):
        result = "{} meows".format(name)
        return result
  
name1 = "Pyshok"
name2 = "Mr Whiskers"
animal = Animal()
cat = Cat()
print(animal.speak(name1))
print(cat.speak(name2))


#Classy Classes
class Person:
    def __init__(self, name,age):
        self.info = "{}s age is {}".format(name, age)

print('\n')
name = input("Input name: ")
age = input("Input age: ")

a = Person(name, age)
print(a.info)


#Interactive Dictionary
class Dictionary:
    def __init__(self):
        self.dictionary = {}
    
    def newentry(self, fruit, descrip):
        self.dictionary[fruit] = descrip

    def look(self, fruit):
        return self.dictionary.get(fruit, "can't find entry for " + fruit)

d = Dictionary()

d.newentry('Apple', 'A fruit that grows on trees')
d.newentry('Banana', 'A yellow fruit')

print('\n')
print(d.look('Apple'))
print(d.look('Banana'))


#Who has the most money?
class Student:
    def __init__(self):
        self.students = {}

    def initialize(self, name, fives, tens, twenties):
        self.students[name] = (int(fives), int(tens), int(twenties))

    def countmoney(self):
        max_money = 0
        ind_max = None
        all_same = True

        for name, (fives, tens, twenties) in self.students.items():
            total = (5 * fives) + (10 * tens) + (20 * twenties)
            
            if total > max_money:
                max_money = total
                ind_max = name
                all_same = False
            elif total == max_money:
                all_same = True
                continue
        if all_same:
            return 'all'
        else:
            return ind_max
        
s = Student()

s.initialize('Max', '5', '3', '2') #95
s.initialize('Maria', '4', '2', '2') #80
s.initialize('Maria', '4', '2', '1') #60
print('\n')
print(s.countmoney())


#Vector class
class Vector:
    def __init__(self):
        self.array = ([])
    
    def add(self, n1, n2):
        if len(n1) != len(n2):
            return 'Error'
        else:
            sum = n1 + n2
            return sum
    
    def substract(self, n1, n2):
        if len(n1) == len(n2):
            substract = n1 - n2
            return substract
        else:
            return 'error'
    
    def dot(self, n1, n2):
        if len(n1) == len(n2):
            dotr = np.dot(n1, n2)
            return dotr
        else:
            return 'error'
    
    def norm(self, n1):
        norm = np.linalg.norm(n1)
        return norm
    

a = Vector()

v1 = np.array([1,2,3])
v2 = np.array([3,4,5])
v3 = np.array([5,6,7,8])

print('\n')
print('sum = ', a.add(v1, v2))
print('substract = ', a.substract(v1, v2))
print('dot = ', a.dot(v1, v2))
print('norm = ', a.norm(v1))
print('add = ', a.add(v1, v3))