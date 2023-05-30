class Queue :
    def __init__(self, capacity=10):
        self.arr = [0]*capacity
        self.capacity = capacity
        self.size = 0
        self.front = 0
        self.back = 0

    def add(self,val):
        if self.size == self.capacity :
            print("Queue is full")

        self.arr[self.back] = val
        self.back = (self.back + 1) % self.capacity
        self.size += 1

    def remove(self):
        if self.size ==0 :
            print("Queue is empty")

        result = self.arr[self.front]
        self.front = (self.front-1) % self.size
        self.length -= 1
        return result

class Dequeue :
    def __init__(self, capacity=10):
        self.arr = [0]*capacity
        self.capacity = capacity
        self.size = 0
        self.front = 0
        self.back = 0

    def add(self,val):
        if self.size == self.capacity :
            print("Queue is full")

        self.arr[self.front] = val
        self.front = (self.front + 1) % self.capacity
        self.size += 1

    def remove(self):
        if self.size ==0 :
            print("Queue is empty")

        result = self.arr[self.front]
        self.front = (self.front-1) % self.size
        self.length -= 1
        return result

    def remove_back(self):
        if self.size ==0 :
            print("Queue is empty")

        result = self.arr[self.back]
        self.back = (self.back+1) % self.size
        self.length -= 1
        return result
