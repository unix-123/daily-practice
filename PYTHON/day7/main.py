# s1 = {2 , 4, 6}
# s2 = {4, 6, 8}
# print(s1.union(s2))  # Union of s1 and s2
# s3 = s1.intersection(s2)  # Intersection of s1 and s2
# s1.update(s2)  # Update s1 with elements from s2
# print(s3)  # Print the intersection result
# s1 = {2 , 4, 6}
# s2 = {4, 6, 8}
# s3 = s1.difference(s2)  # Difference of s1 and s2
# print(s3)  # Print the difference result
# print(s1.issubset(s2))  # Check if s1 is a subset of s2
# print(s1.issuperset(s2))  # Check if s1 is a superset of s2
# dict = {
#     "unix" : "hey there",
#     7 : "aayush",
#     5 : "payal"
# }
# print(dict[5])
# print(dict)
# print(dict.keys())
# print(dict.values())
# print(dict.keys())
# print(dict.items())
# ep1 = {
#     "name" : "aayush",
#     "age" : 20,
#     "city" : "New York"
# }
# ep2 = {
#     "name" : "payal",
#     "age" : 25,
#     "city" : "Los Angeles"
# }   
# ep2.update(ep1)
# ep1.pop("age")
# print(ep1)
# del ep2["city"]
# print(ep2)
# for i in range(int(input("Enter range: "))):
#     print(i)
#     if i < 5:
#         print("less than 5")
#     else:
#         print("equal to 5")

# a = input("enter the number:")
# print("multiplication table of", a)
# try:
#     for i in range(1, 11):
#         print(a, "x", i, "=", int(a) * i)
# except Exception as e:
#     print("sorry my fault")

# finally:
#     print("thank you for using my program")

# questions = [
#     ["What is the capital of India?", "Delhi", "Mumbai", "Kolkata", "Chennai", 1],
#     ["Who is the Prime Minister of India?", "Narendra Modi", "Rahul Gandhi", "Amit Shah", "Arvind Kejriwal", 1],
#     ["Which language are we learning?", "Java", "Python", "C++", "HTML", 2],
#     ["What is 2 + 2?", "3", "4", "5", "6", 2]
# ]

# levels = [1000, 5000, 10000, 20000]

# money = 0

# for i in range(len(questions)):
#     question = questions[i]

#     print("\n", question[0])
#     print("1.", question[1])
#     print("2.", question[2])
#     print("3.", question[3])
#     print("4.", question[4])

#     answer = int(input("Enter your answer (1-4): "))

#     if answer == question[5]:
#         print("Correct answer!")
#         money = levels[i]
#         print("You won Rs.", money)
#     else:
#         print("Wrong answer!")
#         break

# print("Your total winning amount is Rs.", money)


# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Harry, awesome!")
#     index += 1
for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("Harry, awesome!")