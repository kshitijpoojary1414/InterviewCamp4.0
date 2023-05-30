class Stack :
    def find(self, stack, n):
        temp = []
        top = None
        while len(stack) > 0 :
            top = stack.pop()
            temp.push(top)
            if top == n :
                break
        while len(temp) > 0 :
            stack.append(temp.pop())

        return -1 if top is None else top

# Queue using two stacks
class Queue :
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, num):
        self.s1.push(num)

    def dequeue(self):
        if len(self.s2) == 0 :
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())

        if len(self.s2) == 0 :
            return None

        return self.s1.pop()







