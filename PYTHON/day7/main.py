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
for i in range(int(input("Enter range: "))):
    print(i)
    if i < 5:
        print("less than 5")
    else:
        print("equal to 5")