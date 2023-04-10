import math
import stdio
import sys

# Accept x1 (float), y1 (float), x2 (float) and y2 (float) as command-line arguments.
x1 = math.radians(float(sys.argv[1]))
y1 = math.radians(float(sys.argv[2]))
x2 = math.radians(float(sys.argv[3]))
y2 = math.radians(float(sys.argv[4]))

# Set d based on the equations provided.
d = 6359.83 * math.acos((math.sin(x1)*math.sin(x2))+(math.cos(x1)*math.cos(x2)*math.cos(y1 - y2)))

# Write d to standard output.
stdio.writeln(d)
