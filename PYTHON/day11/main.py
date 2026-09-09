# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def showDetails(self):
#         print(f"The name of Employee: {self.id} is {self.name}")


# class Programmer(Employee):
#     def showLanguage(self):
#         print("The default language is Python")


# e1 = Employee("Rohan Das", 400)
# e1.showDetails()


# e2 = Programmer("Harry", 4100)
# e2.showDetails()
# e2.showLanguage()

# class Student:
#     def __init__(self):
#         self._name = "Harry"

#     def _funName(self):      # protected method
#         return "CodeWithHarry"


# class Subject(Student):       # inherited class
#     pass


# obj = Student()
# obj1 = Subject()

# print(dir(obj))

# # calling by object of Student class
# print(obj._name)
# print(obj._funName())

# # calling by object of Subject class
# print(obj1._name)
# print(obj1._funName())

# import random
# print(random.randint(-1,1))
import random

def check(comp, user):
  if comp == user:
    return 0

  if comp == 0 and user == 1:
    return -1

  if comp == 1 and user == 2:
    return -1

  if comp == 2 and user == 0:
    return -1

  return 1


comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for water and 2 for Gun:\n"))

score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)

if score == 0:
  print("Its a draw")
elif score == -1:
  print("You Lose")
else:
  print("You Won")