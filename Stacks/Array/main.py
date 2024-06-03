class Stack:
    def __init__(self, Capacity = 1):
        self.top = -1
        self.Capacity = Capacity
        self.Arr = [None] * Capacity


    def push(self, data):
        if self.Capacity == self.top + 1:
            print("Stack overflow")
            return
        self.top = self.top + 1
        self.Arr[self.top] = data


    def pop(self):
        if self.top = -1:
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
                self.A = newArray
            return temp


