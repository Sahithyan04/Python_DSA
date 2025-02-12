from collections import deque
class Node:
    def __init__(self ,data):
        self.data = data
        self.left = None
        self.right = None
class BinTree:
    def __init__(self ,data):
        node = Node(data)
        self.root = node
    def InOrder(self ,node):
        if node :
            self.InOrder(node.left)
            print(node.data,end= '->')
            self.InOrder(node.right)
    def PostOrder(self ,node):
        if node :
            self.PostOrder(node.left)
            self.PostOrder(node.right)
            print(node.data,end= '->')
    def PreOrder(self ,node):
        if node :
            print(node.data,end= '->')
            self.PreOrder(node.left)
            self.PreOrder(node.right)
    def BreathFirstSearch(self ,node):
        opt_stack = deque()
        if node:
            opt_stack.append(self.root)
        while opt_stack:
            opt = opt_stack.popleft()
            print(opt.data,end="->")
            if opt.left :
                opt_stack.append(opt.left)
            if opt.right :
                opt_stack.append(opt.right)
        

tre = BinTree(2)
tre.root.left = Node(8)
tre.root.right = Node(7)
tre.root.left.left = Node(4) 
tre.root.left.right = Node(3)
tre.BreathFirstSearch(tre.root)
print("\n")
tre.InOrder(tre.root)
print("\n")
tre.PostOrder(tre.root)
print("\n")
tre.PreOrder(tre.root)
'''             2
           8        7
        4     3   '''  
