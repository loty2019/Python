import stdio
import sys

# Accept t (float) and v (float) as command-line arguments.
t = float(sys.argv[1])
v = float(sys.argv[2])

# Set w based on the equations provided.
w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v ** 0.16

# Write w to standard output.
stdio.writeln(w)
