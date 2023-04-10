import math
import stdio
import sys

# Accept L (float) and t (float) as command-line arguments.
L = float(sys.argv[1])
t = float(sys.argv[2])

# Set p based on the equations provided.
p = math.exp(-L * t)

# Write p to standard output.
stdio.writeln(p)
