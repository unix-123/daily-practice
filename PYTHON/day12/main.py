# class Library:
#     def __init__(self, books):
#         self.books = books

#     def showBooks(self):
#         print("The books available in the library are:")
#         for book in self.books:
#             print(book)

#     def addBook(self, book):
#         self.books.append(book)
#         print(f"{book} has been added to the library.")

#     def lendBook(self, book):
#         if book in self.books:
#             self.books.remove(book)
#             print(f"You have borrowed {book}.")
#         else:
#             print("Sorry, this book is not available in the library.")

#     def returnBook(self, book):
#         self.books.append(book)
#         print(f"{book} has been returned to the library.")


# library = Library([
#     "Python",
#     "Rich Dad Poor Dad",
#     "Harry Potter",
#     "C++ Basics",
#     "Algorithms by CLRS"
# ])

# while True:
#     print("\nWelcome to the library!")
#     print("1. Display Books")
#     print("2. Lend a Book")
#     print("3. Add a Book")
#     print("4. Return a Book")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         library.showBooks()

#     elif choice == "2":
#         book = input("Enter the name of the book you want to lend: ")
#         library.lendBook(book)

#     elif choice == "3":
#         book = input("Enter the name of the book you want to add: ")
#         library.addBook(book)

#     elif choice == "4":
#         book = input("Enter the name of the book you want to return: ")
#         library.returnBook(book)

#     elif choice == "5":
#         print("Thank you for using the library!")
#         break

#     else:
#         print("Invalid choice. Please try again.")
# class Employee:
#   company = "Apple"
#   def show(self):
#     print(f"The name is {self.name} and company is {self.company}")

#   @classmethod
#   def changeCompany(cls, newCompany):
#     cls.company = newCompany


# e1 = Employee()
# e1.name = "Harry"
# e1.show()
# e1.changeCompany("Tesla")
# e1.show()
# print(Employee.company)
class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  @classmethod
  def fromStr(cls, string):
    return cls(string.split("-")[0], int(string.split("-")[1]))

e1 = Employee("Harry", 12000)
print(e1.name)
print(e1.salary)

string = "John-12000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))

person = Person.from_string("John Doe, 30")
print(person.name, person.age)