#Task:
#Write a program which will do the following:
#Create a list which contains the first name of everyone in your cohort and store it in a variable called team.
#Add your trainer to the list without manually editing it.
#Print the list to the terminal.
#Print only the 5th person in the list to your terminal

team = ['Sebastian', 'Ahmed', 'Aidan', 'Baki','Ben','Daniel','Feruza','George','Hassan','Lelyzaveta','Ira','James','Santiago','Joseph','Juliana','Kenan','Leon','Lewis','Martyn','Nabil']

team.append('Ryan')

print(team)

print(team[4])

##################

#Task:
#Create a new Python file and write a program that does the following:
#Asks for an input from the user as a mark.
#If the mark is greater that 85 print "Distinction"
#If the mark is between 65 and 85 print "Pass"
#Anything else print "Fail"

#Assignment grade

a_grade = float(input("What is your assignment grade out of 50?: "))

#Exam grade

e_grade = float(input("What is your exam grade out of 100?: "))

#Practical grade

p_grade = float(input("What is your practical grade out of 25?: "))

#Average grade

av_grade = (((a_grade / 50) + (e_grade / 100) + (p_grade / 25)) * 100) / 3

if av_grade >= 80:
    print('Distinction', av_grade)
elif av_grade >= 65 and av_grade <= 80: 
    print('Pass', av_grade)
else:
    print('Fail', av_grade)