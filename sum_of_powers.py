import stdio
import sys

# Accept n (int) and k (int) as command-line argument.
n = int(sys.argv[1])
k = int(sys.argv[2])

# set total to 0
total = 0

# For each value of i from [1, n], set total to its current value times i^k
for i in range(1, n+1):
    total += i**k

# Write total to standard output
stdio.writeln(total)
