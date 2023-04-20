class linked_list:
	def __init__(self, first_data): # first_data est la première donnée de la liste
		self.first_node = Node(first_data) # first_node est le premier noeud de la liste

	def append(self,data): # Ajoute une donnée à la fin de la liste
		current_node = self.first_node
		while current_node.next_node != None:
			current_node = current_node.next_node
		current_node.next_node = Node(data)

	def insert_first(self, data): # Ajoute une donnée au début de la liste
		new_node = Node(data)
		new_node.next_node = self.first_node
		self.first_node = new_node

	def size(self): # Donne la taille de la liste
		current_node = self.first_node
		size = 0
		while current_node != None:
			size += 1
			current_node = current_node.next_node
		return size

	def insert(self, indice, data): # Insert une donnée à un indice précis
		if indice == 0:
			self.insert_first(data)
		else:
			current_node = self.first_node
			for i in range(indice-1):
				current_node = current_node.next_node
			new_node = Node(data)
			new_node.next_node = current_node.next_node
			current_node.next_node = new_node

class Node: # Un noeud est une donnée et un pointeur vers le noeud suivant
	def __init__(self,data):
		self.data = data
		self.next_node = None
# Done But not tested 100%
