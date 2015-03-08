from Question import Question
# Takes in a filepath and returns a list of question objects

def read(filepath):
	myFile = open(filepath, 'r')
	contents = myFile.read()

	questions = parseQuestions(contents)
	return makeQuestions(questions)

def parseQuestions(contents):
	questions = []
	question = ""
	flag = False
	
	for i in range(len(contents)):
		if(contents[i] == '\t'):
			continue
		if(contents[i-1] != '$' and contents[i] == '{'):
			flag = True
		elif(flag == True and contents[i] != '}'):
			question += contents[i]
		elif(contents[i] == '}' and (contents[i-1].isalpha() or contents[i-1] == ']')):
			question += contents[i]
		else:
			flag = False
			if(question != ""):
				questions.append(question)
				question = ""

	return questions

def makeQuestions(questions):
	questionList = []
	for question in questions:
		sections = question.split('\n')
		for each in sections:
			if(each == ""):
				sections.remove(each)
		myQuestion = Question()
		condition = "True" in sections or "False" in sections
		if(len(sections) > 2 and not condition):
			myQuestion.setType(0)
		elif(len(sections) == 3):
			myQuestion.setType(1)
		else:
			myQuestion.setType(2)

		myQuestion.setQuestion(sections[0])
		for i in range(1,len(sections[1:])+1):
			if('#' in sections[i]):
				sections[i] = sections[i][0:len(sections[i])-2]
				myQuestion.setCorrect(sections[i])

		myQuestion.setAnswers(sections[1:])
		questionList.append(myQuestion)
	return questionList