#Iterations

#Given an integer n, write a python application which returns
# a times table grid for all the integers between 1 and n.
#The grid should be separated by tabs and new lines.

n = int(input("Choose an integer"))

line = ''

for row in range(1, n+1):
    for column in range(1,n+1):
        line = line + str(row*column) + "\t"
    line = line + '\n'

print(line)