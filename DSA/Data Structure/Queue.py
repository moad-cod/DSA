class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    def is_empty(self):
        return not self.items
    def size(self):
        return len(self.items)
    def search(self, item):
        return item in self.items

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.size())
print(queue.search(10))
print(queue.search(50))
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.size())