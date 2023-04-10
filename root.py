import stdio
import sys

# Accept k (int), c (float) and epsilon (float) as command-line argument.
k = int(sys.argv[1])
c = float(sys.argv[2])
epsilon = float(sys.argv[3])

# set t equal to c
t = c

# as long as the absolute value of (1-c/t^3) is > than epsilon carry out the equation
while abs(1 - c/t**k) > epsilon:
    t = t - (t**k - c)/(k*t**(k-1))

# write t to standard output
stdio.writeln(t)
