class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    def is_empty(self):
        return not self.items
    def size(self):
        return len(self.items)
    def search(self, item):
        return item in self.items


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.size())
print(stack.search(10))
print(stack.search(50))
print(stack.peek())   
print(stack.pop())   
print(stack.pop())    
print(stack.size())