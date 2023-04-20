class Node:
	def __init__(self, data):
		self.data = data
		self.left_node = None
		self.right_node = None

class Tree:
	def __init__(self, data):
		self.data = Node(data)
	def size(self, node):
		if node == None:
			return 0
		else:
			return 1 + self.size(node.left_node) + self.size(node.right_node)
	def append(self, data):
		current_node = self.data
		if data < current_node.data:
			if current_node.left_node == None:
				current_node.left_node = Node(data)
				return
			else:
				current_node.left_node.append(data)
		else:
			if current_node.right_node == None:
				current_node.right_node = Node(data)
				return
			else:
				current_node.right_node.append(data)
