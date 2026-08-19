import heapq
class PriorityQueue:
    def __init__(self):
        self.items = []
    def enqueue(self, item, priority):
        heapq.heappush(self.items, (priority, item))
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        priority, item = heapq.heappop(self.items)
        return item
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        priority, item = self.items[0]
        return item
    def is_empty(self):
        return not self.items
    def size(self):
        return len(self.items)
    def search(self, item):
        return any( element == item for priority, element in self.items )

queue = PriorityQueue()

queue.enqueue("Task A", 3)
queue.enqueue("Task B", 1)
queue.enqueue("Task C", 2)

print(queue.items)

print(queue.size())
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

