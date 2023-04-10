import math
import stdio
import sys

# Accept O1 (float), n1 (float) and n2 (float) as command-line arguments.
O1 = float(sys.argv[1])
n1 = float(sys.argv[2])
n2 = float(sys.argv[3])

# Set O2 based on the equations provided.
O2 = math.asin((math.sin(math.radians(O1)) * n1) / n2)

# Write O2  in degrees to standard output.
stdio.writeln(math.degrees(O2))
