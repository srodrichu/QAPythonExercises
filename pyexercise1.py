# Create a python file that will input your first name, last name and outputs "Hello [firstname] [lastname]"

firstName = input("Please enter your first name: ")
secondName = input("Please enter your second name: ")

name = firstName, secondName

print("Hello " + name)


# Integers and floaters

number1 = input("Enter whole number: ")
number2 = input("Enter decimal number: ")

integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))

print(number1)
print(number2)
print(round_number)

# Booleans
    
    # Pet

name = "Pep Guardogiola"
age = 3
bark = True
tweet = False

print("My pet is called", name, ", He is", age, "years old.")
print("Statement:", name, "barks.", bark)
print("Statement:", name, "tweets.", tweet)