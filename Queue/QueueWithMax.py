from Queue.Queue import Queue, Dequeue


class QueueWithMax :
    def __init__(self):
        self.queue = Queue()
        self.maxQueue = Dequeue()
    def enqueue(self, val):
        self.queue.add(val)
        while self.maxQueue.back < val :
            self.maxQueue.remove_back()

        self.maxQueue.add(val)

    def dequeue(self):
        if self.maxQueue.front == self.queue.front :
            self.maxQueue.remove()
        self.queue.remove()