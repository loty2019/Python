import stdio

# create list that contains all inputs
# create Sum to track the sum of all the number in the list
a = stdio.readAllInts()
Sum = 0

# repeat for the whole list the sum of the square of the number at index i
for i in range(len(a)):
    Sum += a[i]*a[i]

# write to standard output the Sum
stdio.writeln(Sum)
