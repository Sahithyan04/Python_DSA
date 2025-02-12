class Node:
	def __init__(self ,Data):
		self.data = Data
		self.right = None
		self.left = None
class BinSearchTree:
	def __init__(self):
		self.root = None
	def Insert(self, key):
		if self.root is None:
			self.root = Node(key)
		else:
			self.InsertRecur(self.root ,key)
	def InsertRecur(self, node, key):
		if key < node.data:
			if node.left is None:
				node.left = Node(key)
			else:
				self.InsertRecur(node.left, key)
		else:
			if node.right is None:
				node.right = Node(key)
			else:
				self.InsertRecur(node.right, key)
	def InOrder(self ,node):
		if node :
			self.InOrder(node.left)
			print(node.data,end= '->')
			self.InOrder(node.right)
bintre = BinSearchTree()
bintre.Insert(5)
bintre.Insert(4)
bintre.Insert(1)
bintre.Insert(7)
bintre.Insert(9)
bintre.Insert(2)
bintre.InOrder(bintre.root)
print("\n")
