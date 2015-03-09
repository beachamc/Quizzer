from filereader import read
from random import shuffle
import getch
import os
from subprocess import call
import platform


def main():
	selections = selectQuizzes()
	questions = []
	print("Do you want to turn on Learning Mode? (y/n)")
	learningMode = getch.getch()
	if (learningMode.lower() == 'y'):
		learningMode = True
	for i in range(len(selections)):
		questions += read(os.path.join('Quizzes', selections[i]))
	if(len(questions) > 0):
		print(str(len(questions)) + " questions.")
		shuffle(questions)
		correct = 0
		total = 0
		osClear()
		scoreboard(correct, total, questions)
		print("")
		while(len(questions) > 0):
			total += 1
			question = questions.pop()
			question.toString()
			if(question.getType() != "fill_in_the_blank"):
				char = getch.getch()
				if (len(question.getAnswers()) <= ord(char)-97):
					print("Sorry, that is not a choice. Please try again.")
				while(len(question.getAnswers()) <= ord(char)-97):
					char = getch.getch()
				if(question.getAnswers()[ord(char)-97].lower() == question.getCorrect().lower()):
					osClear()
					correct += 1
					scoreboard(correct, total, questions)
					print("Correct" + "\n")
					print("")
				else:
					osClear()
					if(learningMode == True):
						questions.append(question)
						shuffle(questions)
					scoreboard(correct, total, questions)
					print("Incorrect")
					print("Answer: " + question.getCorrect() + "\n")
					print("")
			else:
				answer = raw_input()
				if(question.getCorrect().lower() == answer.lower()):
					osClear()
					correct += 1
					scoreboard(correct, total, questions)
					print("Correct \n")
					print("")
				else:
					osClear()
					if(learningMode == True):
						questions.append(question)
						shuffle(questions)
					scoreboard(correct, total, questions)
					print("Incorrect")
					print("Answer: " + question.getCorrect() + "\n")
					print("")
					
		score = round(float(correct) / total, 4)
		print ("Score: " + str(score * 100)) + "%"
	else:
		print("No Quizzes Found")


def osClear():
	if(platform.system() == 'Windows'):
		call(["cls"])
	else:
		call(["clear"])

def selectQuizzes():
	quizzes = []
	selections = []
	for file in os.listdir("Quizzes"):
		if(file.endswith(".txt")):
			quizzes.append(file)
	if(len(quizzes) > 0):
		print("Type the numbers, separated by commas for the quizzes you wish to take or type all for all quizzes.")
		for i in range(1,len(quizzes)+1):
			print (str(i) + " " + quizzes[i-1])
		selections = raw_input().split(',')
		if(selections == ['all']):
			selections.remove('all')
			for each in quizzes:
				selections.append(each)
		else:
			for i in range(len(selections)):
				selections[i] = quizzes[int(selections[i])-1]

	return selections


def scoreboard(correct, total, questions):
	left = len(questions)
	if(total == 0):
		score = 0
	else:
		score = round(float(correct) / total, 4)
	print("Correct: " + str(correct) + " | Questions Answered: " + str(total) + " | Questions Left: " + str(left) + " | Score: " + str(score * 100) + "%")
	print("")


if __name__ == '__main__':
	main()