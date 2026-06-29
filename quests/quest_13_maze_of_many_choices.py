# variable to store score from user's input
score = int(input("Enter score between 0-100: "))
# condition to check if the score is between 100 and 90, then output print 'A'
if score <=100 and score >= 90 :
	print ("A")
# Another condition to check if the score is between 89 and 80, then output print 'B'
elif score <= 89 and score >= 80:
	print ("B")
	
# condition to check if the score is between 79 and 70, then output print 'C'
elif score <=79 and score >= 70:
	print ("C")
# condition to check if the score is less 70, then output print 'Needs Improvement'
elif score<70 :
	 print ("Needs Improvement")
	# statement to be executed when none of the conditions above were met!
else: print ("Invalid Input, please enter numbers only from 0-100")
