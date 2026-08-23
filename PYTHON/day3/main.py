name = "UNIX, hey hello how are you doing today?"
subject = "python"
print("My name is " + name)
len1 = len(subject)
print(len1)
print(subject[0:4])
print(subject[-4:-2])

a="UNIX here, how are you my friend?"
print(len(a))
print(a.upper())
print(a.lower())
print(a.replace("here","the great"))
print(a.split(" "))
print(a.count("e"))
print(a.find("o"))
print(a.isalnum())
print(a.isspace())
print(a.isprintable())
print(a.istitle())
print(a.title())

age = int(input("my age is: "))
print("my age is: " , age)
if age<=18:
    print("cannot drive")
elif age>=60:
    print("cannot drive")
else:
    print("can drive")

import time
timestamp=time.strftime("%H:%M:%S")
print("Current Time is: ",timestamp)
print("Current hour is: ",time.strftime("%H"))
print("Current minute is: ",time.strftime("%M"))
print("Current second is: ",time.strftime("%S"))

