import stdio
import sys

# Accept m1 (float), m2 (float) and r (float) as command-line arguments.
m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])

# Set d based on the equations provided.
f = 6.674e-11 * ((m1 * m2) / r ** 2)

# Write f to standard output.
stdio.writeln(f)
