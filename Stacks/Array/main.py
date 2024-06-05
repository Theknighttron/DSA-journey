import random

class Stack:
    def __init__(self, Capacity = 1):
        """
        Creatin new array with initial capacity of one
        With the top element equal to zero
        """
        self.Capacity = Capacity
        self.Arr = [None] * Capacity
        self.top = -1


    def push(self, data):
        """
        Check if the stack is full
        Add the new element to the stack
        And make change the top to point to the new added element
        """
        if self.Capacity == self.top + 1:
            print("Stack overflow")
            return
        self.top = self.top + 1
        self.Arr[self.top] = data


    def pop(self):
        """
        Check if the stack is empty
        Get the element from the top of the stack then decrement the top by 1
        """
        if self.top == -1:
            print("Stack underflow")
            return
        temp = self.Arr[self.top]
        self.top = self.top - 1
        if self.top < self.Capacity // 2:
            print("Trying to resize: Decrease")
            self.Capacity = self.Capacity // 2
            newArray = [None] * self.Capacity
            for i in range(0, self.top + 1):
                newArray[i] = self.Arr[i]
            self.Arr = newArray
        return temp

    def peek(self):
        """
        Check if the stack is empty
        Return the element at the current top position
        """
        if self.top == -1:
            print("Stack underflow")
            return
        return self.Arr[self.top]


    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.Capacity == self.top + 1

stack = Stack()
for i in range(10):
    stack.push(random.randint(1,21))
for i in range (12):
    temp = stack.pop()
    if temp is not None:
        print(temp)
