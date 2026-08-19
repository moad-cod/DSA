# Stage 1
class Node_1:
    def __init__(self, data):
        self.data = data
        self.next = None
    
# Creates nodes
node1 = Node_1(10)
node2 = Node_1(20)
node3 = Node_1(30)
node4 = Node_1(40)

# Implement the refereneces
node1.next = node2
node2.next = node3
node3.next = node4

# Implement the Head
head = node1

# The start
current = head

while current:
    print(current.data, end=" --> ")
    current = current.next
    
print(None)