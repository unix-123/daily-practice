# list = [ 1 , 6, 3, 5, 7, 8]
# print(list)
# list.append(11)
# print(list)
# list.sort(reverse=False)
# print(list)
# print(list.index(5))
# print(list.count(3))
# a=list.copy()
# a[2]=0
# print(a)
# list.insert(2,7)
# print(list)
# a=[12, 15 , 19]
# list.extend(a)
# print(list)

# tup = (2,5,7)
# print(type(tup), tup)
# tup = ( 3 , 4, 7 ,5 , 6 , 8)
# res = tup.count(3)
# print(res)
# res = tup.index(3)
# print(res)
# res = tup.index(1, 3, 4)
# print(res)

# import time
# t= time.strftime('%H:%M:%S')
# h= int(time.strftime('%H'))
# print(h)
# if h>0 and h < 12:
#     print("Good morning my dear")
# elif h <= 17:
#     print("Good afternoon my dear")
# else:
#     print("Good evening and good night everyone")
# name="UNIX"
# country="INDIA"
# print(f"hey this is {name} and I am from {country}")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
number = int(input("Enter a number: "))
print(f"Factorial of {number} is {factorial(number)}")
    
