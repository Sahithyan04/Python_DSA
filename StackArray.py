class StackArray:
 def __init__(self , size=0):
  self.items = []
  if size == 0 or size == None:
   self.size = 7
  else:
   self.size = size

 def push(self ,data):
  if self.length() < self.size :
   self.items.append(data)
   print("Element Succesfully Added")
  else:
   print("Stack Overflow")
 def pop(self):
  return self.items.pop() if not self.is_empty() else None
 def peek(self):
  return self.items[-1] if not self.is_empty() else None
 def is_empty(self):
  return len(self.items) == 0
 def length(self):
  return len(self.items)
 def output(self):
  return self.items

# list1 = StackArray(3)
# list1.push(9)
# list1.push(5)
# list1.push(1)
# list1.push(7)
# list1.push(99)
# list1.pop()
# list1.length()
# list1.output()


class Node:
 
 def __init__(self,data):
  self.data = data
  self.next = None
class StackLinkedList:
 def __init__(self):
  self.head = None
  self.size = 0
 def push(self ,data):
  new_node = Node(data)
  new_node.next = self.head
  self.head = new_node
  self.size += 1
 def pop(self):
  if self.isEmpty():
   raise IndexError("Nothing to pop")
  else:
    popped =  self.head.data 
    self.head = self.head.next
    self.size -= 1
  return popped
 def peek(self):
  if self.isEmpty():
   raise IndexError("Nothing to Peek")
  return self.head.data
 def length(self):
  return self.size
 def isEmpty(self):
  return self.head == None
 def output(self):
  temp = self.head
  while temp:
   print(temp.data,end="-->")
   temp = temp.next
  
lstack = StackLinkedList()
lstack.push(1)
lstack.push(2)
lstack.push(3)
lstack.push(4)
lstack.push(5)
lstack.pop()
print(lstack.peek())
print(lstack.output())