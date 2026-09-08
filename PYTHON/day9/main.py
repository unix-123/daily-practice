# x = 4
# print(x)

# def hello():
#     x = 5
#     print(f"The local x is {x}")
#     print("Hello harry")

# print(f"The global x is {x}")
# hello()
# print(f"The global x is {x}")

# READING A FILE

# f = open('myfile.txt', 'r')
i = 0
# while True:
#   i = i + 1
#   line = f.readline()
#   if not line:
#     break
#   m1 = int(line.split(",")[0])
#   m2 = int(line.split(",")[1])
#   m3 = int(line.split(",")[2])
#   print(f"Marks of student {i} in Maths is: {m1*2}")
#   print(f"Marks of student {i} in English is: {m2*2}")
#   print(f"Marks of student {i} in SST is: {m3*2}")

#   print(line)

# f = open('myfile2.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()
# with open('file.txt', 'r') as f:
#     print(type(f))

#     # Move to the 10th byte in the file
#     f.seek(10)

#     # Read the next 5 bytes
#     data = f.read(5)

#     print(data)
#     with open('file.txt', 'r') as f:

#     data = f.read(10)

#     current_position = f.tell()

#     print(current_position)
#     with open('sample.txt', 'w') as f:
#     f.write('Hello World!')

# with open('sample.txt', 'r') as f:
#     print(f.read())
#     f.truncate(5)
# def double(x):
#   return x*2

# def appl(fx, value):
#   return 6 + fx(value)

# double = lambda x: x * 2
# cube = lambda x: x * x * x
# avg = lambda x, y, z: (x + y + z) / 3

# print(double(5))
# print(cube(5))
# print(avg(3, 5, 10))
# print(appl(lambda x: x * x , 2))
def cube(x):
    return x * x * x
print(cube(5))
    