class node :
	def __init__(self, question, reponses):
		self.question = question
		self.reponses = reponses
		self.next_nodes = []
	def append(self,question,reponses,previous_question):
		if previous_question != self.question:
			self.next_nodes.append(node(question, reponses))
		else:
			for i in self.next_nodes:
				i.append(question,reponses,previous_question)

	def delete(self,question):
		for i in self.next_nodes:
			if i.question == question:
				del i
			else:
				i.delete(question)

class tree :
	def __init__(self,first_question):
		self.first_node = node(first_question,[])
		self.current_node = self.first_node

	def append_question(self,question,reponses,previous_question): # Ajoute une question après une autre "previous_question"
		self.first_node.append(question,reponses,previous_question)

	def delete_question(self,question):
		if self.first_node.question == question:
			self.first_node = None
		else:
			self.first_node.delete(question)

	def get_question(self):
		return self.current_node.question

	def send_answer(self, reponse):
		for i in self.current_node.next_nodes:
			if reponse in i.reponses:
				self.current_node = i
				break
		return self.current_node.question
