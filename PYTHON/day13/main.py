# class Person:
#   def __init__(self, name, age):
#       self.name = name
#       self.age = age
#       self.version = 1


# p = Person("John", 30)
# print(p.__dict__)

# print(help(Person))

# class Employee:
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id

# class Programmer(Employee):
#   def __init__(self, name, id, lang):
#     super().__init__( name, id)
#     self.lang = lang

# rohan = Employee("Rohan Das", "420")
# harry = Programmer("Harry", "2345", "Python")
# print(harry.name)
# print(harry.id)
# print(harry.lang)

# from emp import Employee

# e = Employee("Harry")
# print(str(e))
# print(repr(e))
# # print(e.name)
# # print(len(e))
# e()