# Stack Implementation Using List

class Stack:

    # Constructor

    def __init__(self):
        self.s = []


    # Length Of Stack

    def length(self):
        return len(self.s)


    # Push Element

    def push(self, value):
        self.s.insert(0, value)


    # Check Top Element

    def peek(self):

        if len(self.s) == 0:
            raise Exception("Stack is Empty")

        return self.s[0]


    # Pop Element

    def pop(self):

        if len(self.s) == 0:
            raise Exception("Stack is Empty")

        return self.s.pop(0)


    # Check If Stack Is Empty

    def is_empty(self):
        return len(self.s) == 0


# Create Stack Object

stk = Stack()


# Check Pop On Empty Stack

try:
    print(stk.pop())

except Exception as e:
    print(e)


# Push Elements

stk.push(10)
stk.push(20)
stk.push(30)


# Peek Top Element

print(stk.peek())


# Pop Elements

print(stk.pop())
print(stk.pop())
print(stk.pop())


# Check Stack Is Empty

print(stk.is_empty())


# Check Stack Length

print(stk.length())



######HOMEWORK######
# Stack Implementation Using Append And Pop

class Stack:

    # Constructor

    def __init__(self):
        self.s = []


    # Length Of Stack

    def length(self):
        return len(self.s)


    # Push Element

    def push(self, value):
        self.s.append(value)


    # Peek Top Element

    def peek(self):

        if len(self.s) == 0:
            raise Exception("Stack is Empty")

        return self.s[-1]


    # Pop Element

    def pop(self):

        if len(self.s) == 0:
            raise Exception("Stack is Empty")

        return self.s.pop()


    # Check If Stack Is Empty

    def is_empty(self):
        return len(self.s) == 0


# Create Stack Object

stk = Stack()


# Push Elements

stk.push(10)
stk.push(20)
stk.push(30)


# Peek

print(stk.peek())


# Pop

print(stk.pop())
print(stk.pop())
print(stk.pop())


# Check Empty

print(stk.is_empty())


# Check Length

print(stk.length())