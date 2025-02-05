class Node:
 def __init__(self ,data):
  self.data = data
  self.next = None
class LinkedQueue:
 def __init__(self):
  self.head = None
  self.rear = None
 def enqueue(self ,data):
  new_node = Node(data)
  if self.rear == None:
   self.head = self.rear = new_node
  else:
   
   self.rear.next = new_node
   self.rear = new_node 

 def dequeue(self):
  if self.head is None:
   return "Empty Queue"
  
  data = self.head.data
  self.head = self.head.next
  if self.head is None:
   self.rear = None
  return data
  
 def result(self):
  current = self.head
  while current :
   print(current.data,end="=>")
   current = current.next
  return
lst1  = LinkedQueue()
lst1.enqueue(2)
lst1.enqueue(4)
lst1.enqueue(6)
print(lst1.dequeue())
print(lst1.dequeue())
print(lst1.dequeue())

lst1.enqueue(2)
lst1.enqueue(4)
lst1.enqueue(6)


lst1.result()
print('\n')