class StackWithMax :
    def __init__(self):
        self.stack = []
        self.maxStack = []

    def add(self, num):
        if len(self.maxStack) == 0 or self.maxStack[-1] <= num :
            self.maxStack.append(num)

        self.stack.append(num)

    def pop(self):
        top = self.stack.pop()
        if top == self.maxStack[-1] :
            self.maxStack.pop()

        return top

    def max(self):
        if len(self.maxStack) > 0 :
            return self.maxStack[-1]

