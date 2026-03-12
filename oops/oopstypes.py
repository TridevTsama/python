#Encapsulation
class Student:
    def __init__(self):
        self.__marks = 0   # private variable

    def set_marks(self, m):
        self.__marks = m

    def get_marks(self):
        return self.__marks


s = Student()
s.set_marks(85)
print(s.get_marks())

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())

#Single Inheritence
class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()   
d.bark()
#Multiple Inheritence
class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def talent(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()
c.talent()
#Multi Level Inheritence 
class Device:
    def power_on(self):
        print("Device powered on")

class Mobile(Device):
    def call(self):
        print("Making a call")

class Smartphone(Mobile):
    def internet(self):
        print("Using internet")

s = Smartphone()
s.power_on()
s.call()
s.internet()
#Hierarchical Inheritance Example 
class Shape:
    def display(self):
        print("This is a shape")

class Circle(Shape):
    def draw_circle(self):
        print("Drawing circle")

class Square(Shape):
    def draw_square(self):
        print("Drawing square")

c = Circle()
s = Square()

c.display()
s.display()
#Hybrid Inheritence
class A:
    def show(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

class C(A):
    def print_msg(self):
        print("Class C")

class D(B, C):
    pass

d = D()
d.show()
d.display()
d.print_msg()
