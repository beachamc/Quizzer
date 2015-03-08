
class Question:
	

	def __init__(self):
		self.types = ["multiple_choice", "true/fase", "fill_in_the_blank"]

	def setType(self, mytype):
		self.type = self.types[mytype]

	def setQuestion(self, question):
		self.question = question

	def setAnswers(self, answers):
		self.answers = answers

	def setCorrect(self, correct):
		self.correct = correct

	def getType(self):
		return self.type

	def getQuestion(self):
		return self.question

	def getAnswers(self):
		return self.answers

	def getCorrect(self):
		return self.correct

	def toString(self):
		print("Type: " + self.type)
		print("Question: " + self.question)
		if(self.type != "fill_in_the_blank"):
			for i in range(len(self.answers)):
				print('\t' + chr(i+97) + ". " + str(self.answers[i]))
		print ("")

	def toStringAnswer(self):
		print("Type: " + self.type)
		print("Question: " + self.question)
		if(self.type != "fill_in_the_blank"):
			for i in range(len(self.answers)):
				print('\t' + chr(i+97) + ". " + str(self.answers[i]))
		print("Correct Answer = " + str(self.correct))
		print ("")