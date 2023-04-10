import math
import stdio
import sys

# Accept x (float) and Phi (float) as command-line arguments.
x = float(sys.argv[2])
Phi = float(sys.argv[1])

# Set y based on the equations provided.
y = math.log((1 + math.sin(math.radians(Phi))) / (1 - math.sin(math.radians(Phi)))) / 2

# Write x "space" y to standard output.
stdio.writeln(str(x) + " " + str(y))
