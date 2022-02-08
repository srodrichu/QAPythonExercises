#The program should take the students
#name, homework score(/25), assessment
#score(/50) and final exam score(/100) as
#inputs, and output their name and final ICT
#grade as a percentage.

## Functions

def grading(name, hw_score, a_score, ex_score):

    hw_perc = hw_score / 25
    a_perc = a_score / 50
    ex_perc = ex_score / 100

    average_perc = ((hw_perc + a_perc + ex_perc) / 3) * 100

    print(f"Name: {name}, Final grade (%): {average_perc}")

grading('Sebastian', 22, 45, 75)

