#Sample Quiz Template (Submission only)
#Last updated: 2016/12/04

#Imports excel file
import csv, random

#Global variables 
count = 0
score = 0
student_answers = []

#Reads excel file and saves the information into the questions variable
def read_questions():
	global count
	questions = []
	
	with open("Sample.csv", 'rb') as sample_questions:
		reader = csv.reader(sample_questions)
		for row in reader:
			count += 1
			questions.append(row)
	
	return questions
	return count

#Converts the excel data containing the questions, choices and answers into a testable format
#Currently written to accomodate multiple choice questions composed of 4 choices
#Column 0: Question, Column 1-4: Choices, Column 5-6: Correct letter answers (upper and lowercase)
#1 point is earned for every correct answer
def quiz(questions, R):
	global score
	global student_answers
	prompt = '> '
	QR = questions[R][0]
	A1 = questions[R][1]
	A2 = questions[R][2]
	A3 = questions[R][3]
	A4 = questions[R][4]
	correct_answer = questions[R][5]
	correct_answer2 = questions[R][6]
	
	print "%s \n %s \n %s \n %s \n %s" %(QR, A1, A2, A3, A4)
	
	answer = raw_input(prompt)
	student_answers.append(answer)
	
	if answer == correct_answer or answer == correct_answer2:
		score = score + 1
		print "Correct! \n Score: %s" %score
	else:
		print "Sorry, the correct answer is %s" %correct_answer
		print "Score: %s" %score 
	
	return student_answers
	return score

#Runs through the quiz based on user input.
def main():
	global count
	global score
	global student_answers
	prompt = '> '

	print "Please enter your name."
	name = raw_input(prompt)

	print "Please enter your student number."
	student_number = raw_input(prompt)

	questions = read_questions() 
	num = count - 1

	print "This is a quiz to test your knowledge on (insert subject here)."
	print "There will be %s of multiple choice questions." %num
	print "Would you like to begin? (Press Y to continue.)"

	begin = raw_input(prompt)
	
#Runs through the quiz questions
	if begin == "Y" or begin == "y":
		for R in range(1,count):
			quiz(questions, R)
		
		summary = "You answered %s out of %s questions correctly!" %(score, num)
		print summary
		print "Would you like to save your answers for reference? (Press Y to continue.)"
		save = raw_input(prompt)

#Writes user answers to a file so they have a copy either for their own reference or for submission purposes
		if save == "Y" or save == "y":
			print "Save file as..."
			student_answers_str = str(student_answers)
			filename = raw_input(prompt)+'.txt'
			
			file = open(filename, "w") 
			file.write(name)
			file.write("\n")
			file.write(student_number)
			file.write("\n")
			file.write(student_answers_str)
			file.write("\n")
		else:
			print "Answers have not been saved."

		print "For more practice, create your own questions in Excel and run it in this program!"
	
	else:
		print "Okay. Maybe later!"

if __name__ == "__main__":
	main()


	

