import stdio
import sys

# Accept n1 (int), n2 (int) and y2 (float) as command-line arguments.
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
p = float(sys.argv[3])

# Create variable q by subtracting 1 the value of p
q = 1-p

# Set p1 and p2 based on the equations provided.
p1 = (1 - (p/q) ** n2) / (1 - (p/q) ** (n1+n2))
p2 = (1 - (q/p) ** n1) / (1 - (q/p) ** (n1+n2))

# Write "p1 "space" p2" to standard output.
stdio.writeln(str(p1) + " " + str(p2))
