def hello():
  print("hello")

hello()

sales1 = 6000
profit1 = 2000
ad1 = 1000
# rajeev.sales

sales2 = 6000
profit2 = 2000
ad2 = 1000
# vikrant.sales

sales3 = 6000
profit3 = 2000
ad3 = 1000


# RailwayForm   ---> Class [blueprint]
# harry --> harry ki info wala form --> Object [entity]
# tom --> tom ki info wala form --> Object [entity]
# shubham -- shubham ki info wala form --> Object [entity]
# shubham.changeName("Shubhi")
# class Unix:
#   name = "Unix"
#   occupation = "Hacker"
#   networth = 100
# a = Unix()
# print(a.name)
# print(a.occupation)
# print(a.networth)
# 
# class Person:

#   def __init__(self, name, occ):
#     print("Hey I am a person")
#     self.name = name
#     self.occ = occ

#   def info(self):
#     print(f"{self.name} is a {self.occ}")


# a = Person("Harry", "Developer")
# b = Person("Divya", "HR")

# a.info()
# b.info()

# # print(a.name)
# # a.name = "Divya"
# # a.occ = "HR"
# # a.info()

# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thanks for using this function")
#     return mfx


# @greet
# def hello():
#     print("Hello World")


# hello()

class MyClass:

    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value / 10


obj = MyClass(10)

obj.ten_value = 67

print(obj.ten_value)

obj.show()